import sys
import time

import pygame
from Setting import Settings
from ContainerInterface import ContainerInterface, SettingInterface, LevelInterface
from TankAllies import TankAllies
from TankAllies import DirtyRoad
from TankAllies import River
from TankAllies import TankOpening
from TankAllies import Highway
from TankAllies import Cobblestone
from TankEnemies import RedTank, BlueTank, GreenTank
from GameScore import ScoreBoard
from Bullet import Bullet
from InterfaceActivation import InterfaceActivation, GameStats

'''
    NEXT PROJECT :
    1. MENGATASI LAGGING DENGAN MENURUNKAN BERAT FILE GAMBAR MAPS DI MAPS 1 
    2. MENGATUR SCORE DAN KONDISI KETIKA TANK MUSH HABIS, TANK MUSUH MENCAPAI LAYAR PALING KIRI,
       DAN TANK MUSUH BERTABRAKAN DENGAN TANK ALLIES
    
'''

class MainClass :
    def __init__(self):
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.setting.display_width = self.screen.get_rect().width
        self.setting.display_height = self.screen.get_rect().height
        pygame.display.set_caption('Panzer War')

        #All Clases Instance
        self.containerInterface = ContainerInterface(self)
        self.settingInterface = SettingInterface(self)
        self.levelInterface = LevelInterface(self)
        self.tankAllies = TankAllies(self)
        self.tankOpening = TankOpening(self)
        self.dirty_road = pygame.sprite.Group()
        self.highway = pygame.sprite.Group()
        self.cobblestone = pygame.sprite.Group()
        self.river = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.activation = InterfaceActivation()

        #Game Statistic
        self.stats = GameStats(self)
        self.sb = ScoreBoard(self)

        # Tank Enemies
        self.red_tank = pygame.sprite.Group()
        self.green_tank = pygame.sprite.Group()
        self.blue_tank = pygame.sprite.Group()

        #Creating Maps
        self._create_fleet_road()
        self._create_fleet_river()
        self._create_fleet_highway()
        self._create_fleet_cobble()
        
        # For Button In Maps1, Maps2, and Maps3
        self.maps1 = True
        self.maps2 = False
        self.maps3 = False
        self.button_maps1 = False
        self.button_maps2 = False
        self.button_maps3 = False
        self.clock = pygame.time.Clock()
        self.time = time

        self.SHOOT_SOUND = pygame.mixer.Sound('fire.wav')
        self.SHOOT_SOUND.set_volume(0.2)
        self.EXPLODE_SOUND = pygame.mixer.Sound('explode.wav')
        self.EXPLODE_SOUND.set_volume(0.2)
        self.IDLE_SOUND = pygame.mixer.Sound('idle.wav')
        self.IDLE_SOUND.set_volume(0.6)
        self.CLICK_SOUND = pygame.mixer.Sound('click.wav')
        self.CLICK_SOUND.set_volume(0.8)
        self.LEVEL_SOUND = pygame.mixer.Sound('up.wav')
        self.LEVEL_SOUND.set_volume(1.0)

        self._create_fleet_red_tank()

        # Enemy Tank
        # self._create_fleet_red_tank()

    # This Part For Event in Game
    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_event(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_event = pygame.mouse.get_pos()
                #FOR MAIN CONTAINER
                #Jika settingInterface dan level Inteface tidak aktiv maka main meu bisa di gunakan dan sebaliknya
                if not self.settingInterface.setting_present and not self.levelInterface.level_present:
                    self._check_play_button(mouse_event)
                    self._check_exit_button(mouse_event)
                    self._check_setting_button(mouse_event)
                    self._check_level_button(mouse_event)

                #From Setting Interface
                if not self.containerInterface.menu_present and not self.levelInterface.level_present:
                    self._check_back_button(mouse_event)
                    self._check_button_maps1(mouse_event)
                    self._check_button_maps2(mouse_event)
                    self._check_button_maps3(mouse_event)

                #FROM LEVEL INTERFACE
                if not self.containerInterface.menu_present and not self.settingInterface.setting_present:
                    self._check_back_rect(mouse_event)
                    self._check_level1_rect(mouse_event)
                    self._check_level2_rect(mouse_event)
                    self._check_level3_rect(mouse_event)

    #MAIN CONTAINER
    def _check_play_button(self, mouse_event):
        button = self.containerInterface.play_button_rect.collidepoint(mouse_event)
        self.CLICK_SOUND.play()
        if button and not self.activation.game_active:
            self.activation.game_active = True
            self.screen.fill((0, 0, 0))
            self.tankOpening.active = False
            self.tankAllies.active = True
            self.containerInterface.menu_present = False
            self._create_fleet_red_tank()
            self._create_fleet_blue_tank()
            self._create_fleet_green_tank()
            self.sb.prep_score()
            self.sb.prep_ship()

    def _check_exit_button(self, mouse_event):
        button = self.containerInterface.exit_button_rect.collidepoint(mouse_event)
        self.CLICK_SOUND.play()
        if button and not self.activation.game_active:
            sys.exit()

    def _check_setting_button(self, mouse_event):
        button = self.containerInterface.setting_button_rect.collidepoint(mouse_event)
        self.CLICK_SOUND.play()
        if button and not self.settingInterface.setting_present:
            self.settingInterface.setting_present = True
            self.containerInterface.menu_present = False
            
    def _check_level_button(self, mouse_event):
        button = self.containerInterface.level_button_rect.collidepoint(mouse_event)
        self.CLICK_SOUND.play()
        if button and not self.levelInterface.level_present:
            self.settingInterface.setting_present = False
            self.containerInterface.menu_present = False
            self.levelInterface.level_present = True
    
    #For Level Interface
    def _check_back_rect(self, mouse_event):
        button = self.levelInterface.back_rect.collidepoint(mouse_event)
        self.CLICK_SOUND.play()
        if button and self.levelInterface.level_present:
            self.levelInterface.level_present = False
            self.containerInterface.menu_present = True

    def _check_level1_rect(self, mouse_event):
        button = self.levelInterface.level1_rect.collidepoint(mouse_event)
        self.CLICK_SOUND.play()
        if button and self.levelInterface.level_present:
            self.setting.level_game = "EASY"
            self.levelInterface.level_color = (144, 238, 144)
            if self.maps1:
                self.setting.ship_speed = 7.0
                self.setting.bullet_speed = 10.0
            else:
                self.setting.ship_speed = 3.0
                self.setting.bullet_speed = 5.0
                self.setting.red_ship_speed = 2.0
                self.setting.blue_ship_speed = 1.5
                self.setting.green_ship_speed = 1.0

    def _check_level2_rect(self, mouse_event):
        button = self.levelInterface.level2_rect.collidepoint(mouse_event)
        self.CLICK_SOUND.play()
        if button and self.levelInterface.level_present:
            self.setting.level_game = "MEDIUM"
            self.levelInterface.level_color = (251, 160, 122)
            self.setting.ship_speed = 3.0
            self.setting.bullet_speed = 5.0
            self.setting.red_ship_speed = 2.0
            self.setting.blue_ship_speed = 1.5
            self.setting.green_ship_speed = 1.0

    def _check_level3_rect(self, mouse_event):
        button = self.levelInterface.level3_rect.collidepoint(mouse_event)
        self.CLICK_SOUND.play()
        if button and self.levelInterface.level_present:
            self.setting.level_game = "HARD"
            self.levelInterface.level_color = (250, 69, 1)
            self.setting.ship_speed = 3.0
            self.setting.bullet_speed = 5.0
            self.setting.red_ship_speed = 2.0
            self.setting.blue_ship_speed = 1.5
            self.setting.green_ship_speed = 1.0
    
    # From Setting Interface
    def _check_back_button(self, mouse_event):
        button = self.settingInterface.button_back.collidepoint(mouse_event)
        self.CLICK_SOUND.play()
        if button and self.settingInterface.setting_present:
            self.settingInterface.setting_present = False
            self.containerInterface.menu_present = True

    def _check_button_maps1(self, mouse_event):
        button = self.settingInterface.button_maps1.collidepoint(mouse_event)
        self.CLICK_SOUND.play()
        if button and self.settingInterface.setting_present and not self.button_maps1:
            for road in self.highway.copy():
                self.highway.remove(road)

            for road in self.cobblestone.copy():
                self.cobblestone.remove(road)

            self._create_fleet_road()
            self._create_fleet_river()
            self.button_maps1 = True
            self.button_maps2 = False
            self.button_maps3 = False
            self.maps1 = True
            self.maps2 = False
            self.maps3 = False

    def _check_button_maps2(self, mouse_event):
        button = self.settingInterface.button_maps2.collidepoint(mouse_event)
        self.CLICK_SOUND.play()
        if button and self.settingInterface.setting_present and not self.button_maps2:
            for road in self.dirty_road.copy():
                self.dirty_road.remove(road)

            for road in self.river.copy():
                self.river.remove(road)

            for road in self.cobblestone.copy():
                self.cobblestone.remove(road)

            for road in self.highway.copy():
                self.highway.remove(road)

            self._create_fleet_highway()
            self.button_maps1 = False
            self.button_maps2 = True
            self.button_maps3 = False
            self.maps1 = False
            self.maps2 = True
            self.maps3 = False

    def _check_button_maps3(self, mouse_event):
        button = self.settingInterface.button_maps3.collidepoint(mouse_event)
        self.CLICK_SOUND.play()
        if button and self.settingInterface.setting_present and not self.button_maps3:
            for road in self.dirty_road.copy():
                self.dirty_road.remove(road)

            for road in self.river.copy():
                self.river.remove(road)

            self._create_fleet_cobble()
            self.button_maps1 = False
            self.button_maps2 = False
            self.button_maps3 = True
            self.maps1 = False
            self.maps2 = False
            self.maps3 = True

    def _check_key_down_event(self, event):
        if event.key == pygame.K_UP:
            self.tankAllies.move_up = True
        elif event.key == pygame.K_RIGHT:
            self.tankAllies.move_right = True
        elif event.key == pygame.K_LEFT:
            self.tankAllies.move_left = True
        elif event.key == pygame.K_DOWN:
            self.tankAllies.move_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_key_up_event(self, event):
        if event.key == pygame.K_UP:
            self.tankAllies.move_up = False
        elif event.key == pygame.K_RIGHT:
            self.tankAllies.move_right = False
        elif event.key == pygame.K_LEFT:
            self.tankAllies.move_left = False
        elif event.key == pygame.K_DOWN:
            self.tankAllies.move_down = False
        elif event.key == pygame.K_q:
            self._menu_present()
    # Part For Event Above

    # To Make Menu In Game
    def _menu_present(self):
        self.activation.game_active = False
        self.tankAllies.active = False
        self.containerInterface.menu_present = True
        self.tankOpening.active = True
        self.tankOpening.update_ship()
        for redTank in self.red_tank.copy():
            self.red_tank.remove(redTank)
        for blueTank in self.blue_tank.copy():
            self.blue_tank.remove(blueTank)
        for greenTank in self.green_tank.copy():
            self.green_tank.remove(greenTank)

    #To Make A Map In Game
    def _create_fleet_road(self):
        new_road = DirtyRoad()
        road_width = new_road.rect.width
        road_height = new_road.rect.height

        availabel_road_x = self.setting.display_width // road_width + 1
        availabel_road_y = self.setting.display_height // road_height + 1

        for y in range(availabel_road_y):
            for x in range(availabel_road_x):
                self._create_road(x, y)

    def _create_fleet_cobble(self):
        new_road = Cobblestone()
        road_width = new_road.rect.width
        road_height = new_road.rect.height

        availabel_road_x = self.setting.display_width // road_width + 1
        availabel_road_y = self.setting.display_height // road_height + 1

        for y in range(availabel_road_y):
            for x in range(availabel_road_x):
                self._create_cobble(x, y)

    def _create_fleet_highway(self):
        new_road = Highway()
        road_width = new_road.rect.width
        road_height = new_road.rect.height

        availabel_road_x = self.setting.display_width // road_width + 1
        availabel_road_y = self.setting.display_height // road_height + 1

        for y in range(availabel_road_y):
            for x in range(availabel_road_x):
                self._create_highway(x, y)

    def _create_fleet_river(self):
        new_river = River()
        river_height = new_river.rect.height
        
        available_river_y = self.setting.display_height // river_height + 1
        
        for y in range (available_river_y):
            self._create_river(y)

    def _create_cobble(self, num_x, num_y):
        new_road = Cobblestone()
        road_width = new_road.rect.width
        road_height = new_road.rect.height

        new_road.x = road_width * num_x
        new_road.y = road_height * num_y

        new_road.rect.x = new_road.x
        new_road.rect.y = new_road.y

        self.cobblestone.add(new_road)

    def _create_highway(self, num_x, num_y):
        new_road = Highway()
        road_width = new_road.rect.width
        road_height = new_road.rect.height

        new_road.x = road_width * num_x
        new_road.y = road_height * num_y

        new_road.rect.x = new_road.x
        new_road.rect.y = new_road.y

        self.highway.add(new_road)

    def _create_road(self, num_x, num_y):
        new_road = DirtyRoad()
        road_width = new_road.rect.width
        road_height = new_road.rect.height

        new_road.x = road_width * num_x
        new_road.y = road_height * num_y

        new_road.rect.x = new_road.x
        new_road.rect.y = new_road.y

        self.dirty_road.add(new_road)
        
    def _create_river(self, num_y):
        new_river = River()
        river_height = new_river.rect.height
        
        new_river.x = (self.setting.display_width / 2) - 100
        new_river.y = river_height * num_y
        
        new_river.rect.x = new_river.x
        new_river.rect.y = new_river.y
        
        self.river.add(new_river)
    # To Make A map Above

    # TO MAKE AN ENEMYS
    def _create_fleet_red_tank(self):
        new_red_tank = RedTank(self)
        red_tank_height = new_red_tank.rect.height

        available_river_y = self.setting.display_height // red_tank_height

        for y in range(available_river_y - 5):
            self._create_red_tank(y)

    def _create_red_tank(self, num_y):
        new_red_tank = RedTank(self)
        red_tank_height = new_red_tank.rect.height

        new_red_tank.x = (self.setting.display_width) - 100
        new_red_tank.y = ((red_tank_height) * num_y) + 100

        new_red_tank.rect.x = new_red_tank.x
        new_red_tank.rect.y = new_red_tank.y

        self.red_tank.add(new_red_tank)

    def _create_fleet_blue_tank(self):
        new_blue_tank = BlueTank(self)
        blue_tank_height = new_blue_tank.rect.height

        available_river_y = self.setting.display_height // blue_tank_height

        for y in range(available_river_y - 5):
            self._create_blue_tank(y)

    def _create_blue_tank(self, num_y):
        new_blue_tank = BlueTank(self)
        blue_tank_height = new_blue_tank.rect.height

        new_blue_tank.x = (self.setting.display_width) - 250
        new_blue_tank.y = ((blue_tank_height) * num_y) + 100

        new_blue_tank.rect.x = new_blue_tank.x
        new_blue_tank.rect.y = new_blue_tank.y

        self.blue_tank.add(new_blue_tank)

    def _create_fleet_green_tank(self):
        new_green_tank = GreenTank(self)
        green_tank_height = new_green_tank.rect.height

        available_river_y = self.setting.display_height // green_tank_height

        for y in range(available_river_y - 5):
            self._create_green_tank(y)

    def _create_green_tank(self, num_y):
        new_green_tank = GreenTank(self)
        green_tank_height = new_green_tank.rect.height

        new_green_tank.x = (self.setting.display_width) - 400
        new_green_tank.y = ((green_tank_height) * num_y) + 100

        new_green_tank.rect.x = new_green_tank.x
        new_green_tank.rect.y = new_green_tank.y

        self.green_tank.add(new_green_tank)

    def _update_tank(self):
        self._check_left_tank()

        for redTank in self.red_tank.sprites():
            redTank.update()
        for blueTank in self.blue_tank.sprites():
            blueTank.update()
        for greenTank in self.green_tank.sprites():
            greenTank.update()

        self._check_tank_collide()



    def _check_left_tank(self):
        screen = self.screen.get_rect()

        for red in self.red_tank.sprites():
            if red.rect.midleft <= screen.midleft:
                self._check_ship_hit()
                break

        for blue in self.blue_tank.sprites():
            if blue.rect.midleft <= screen.midleft:
                self._check_ship_hit()
                break

        for green in self.green_tank.sprites():
            if green.rect.midleft <= screen.midleft:
                self._check_ship_hit()
                break

    def _check_tank_collide(self):

        if pygame.sprite.spritecollideany(self.tankAllies, self.red_tank): #jika kapal collide dengan salah satu dari alien
            self.EXPLODE_SOUND.play()
            print("Red Hit")
            self._check_ship_hit()
        elif pygame.sprite.spritecollideany(self.tankAllies, self.blue_tank):
            self.EXPLODE_SOUND.play()
            self._check_ship_hit()
        elif pygame.sprite.spritecollideany(self.tankAllies, self.green_tank):
            self.EXPLODE_SOUND.play()
            self._check_ship_hit()

    def _check_ship_hit(self):

        for red in self.red_tank.sprites():
            self.red_tank.remove(red)


        for blue in self.blue_tank.sprites():
            self.blue_tank.remove(blue)

        for green in self.green_tank.sprites():
            self.green_tank.remove(green)

        for bullet in self.bullets.sprites():
            self.bullets.remove(bullet)

        self.tankAllies.center_ship()


        if self.stats.ships_left > 0:
            self.time.sleep(1)
            self._create_fleet_red_tank()
            self._create_fleet_blue_tank()
            self._create_fleet_green_tank()
            self.stats.ships_left -= 1
            print(self.stats.ships_left)
            self.sb.prep_ship()
            self.sb.show_score()

        else:
            self.scene_exit = False
            time = 14000
            '''
            while not self.scene_exit:
                self.levelInterface.game_over_present = True
                self.levelInterface.draw_container()

                pygame.display.update()

                passed_time = self.clock.tick(60)
                print(passed_time)
                time -= passed_time
                if time <= 0:
                    self.sceneExit = True
                    print("Done man")
                    break
            '''
            self.levelInterface.game_over_present = True
            self.levelInterface.draw_container()
            # if you want to updating something new in screen you have to flip it
            # i use flip because after delay for 2 second, the programs doesnt access the update screen method that i wrote
            # in below this section. So i need to re write the display flip only for this section because it cannot
            # access the display update while the profram stop
            pygame.display.flip()
            print("start")
            pygame.time.wait(2000)
            print("stop")
            self.levelInterface.game_over_present = False
            self._create_fleet_red_tank()
            self._create_fleet_blue_tank()
            self._create_fleet_green_tank()
            self.activation.game_active = False
            self.tankAllies.active = False
            self.containerInterface.menu_present = True
            self.tankOpening.active = True
            self.tankOpening.update_ship()
            self.stats.ships_left = self.setting.ship_limit
            self.stats.score = 0
            self.stats.level = 1
            self.sb.prep_ship()
            self.sb.show_score()

    # To Make A Bullet When You Pressed Space
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        self.SHOOT_SOUND.play()

    def _update_bullets(self):
        self.bullets.update()
        self._check_bullet_collide()
        # Menghapus peluru yang telah di gambar jika peluru telah melewati batas layar
        for bullet in self.bullets.copy():
            if bullet.rect.bottom >= self.setting.display_width:
                self.bullets.remove(bullet)

    def _check_bullet_collide(self):
        collisions_red = pygame.sprite.groupcollide(self.bullets, self.red_tank, True, True)
        collisions_blue = pygame.sprite.groupcollide(self.bullets, self.blue_tank, True, True)
        collisions_green = pygame.sprite.groupcollide(self.bullets, self.green_tank, True, True)
        # collision merupakan dictionary yang menyimpan alien yang mengalami collision dengan peluru

        #Red Tank
        if collisions_red:
            self.EXPLODE_SOUND.play()
            for red_tank in collisions_red.values():
                self.stats.score += self.setting.red_tank_point * len(red_tank)
                self.red_tank.remove(red_tank)
            self.sb.prep_score()
            self.sb.check_high_score()

        #Blue Tank
        if collisions_blue:
            self.EXPLODE_SOUND.play()
            for blue_tank in collisions_blue.values():
                self.stats.score += self.setting.blue_tank_point * len(blue_tank)
            self.sb.prep_score()
            self.sb.check_high_score()

        #Green Tank
        if collisions_green:
            self.EXPLODE_SOUND.play()
            for green_tank in collisions_green.values():
                self.stats.score += self.setting.green_tank_point * len(green_tank)
            self.sb.prep_score()
            self.sb.check_high_score()

        #Check Jumlah Tank Musuh
        if not self.red_tank and not self.blue_tank and not self.green_tank:  # jika alien habis pada layar
            self.LEVEL_SOUND.play()
            self.bullets.empty()
            self._create_fleet_red_tank()
            self._create_fleet_blue_tank()
            self._create_fleet_green_tank()
            self.setting.ship_speed += 1
            self.stats.level += 1
            self.sb.prep_level()
            self.sb.show_score()

    #Bullet maker Above
        
    # Updating Event in Game
    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        if self.maps1:
            self.dirty_road.draw(self.screen)
            self.river.draw(self.screen)
            self.setting.tank_opening_speed = 18.0
        
        if self.maps2:
            self.highway.draw(self.screen)
            self.setting.tank_opening_speed = 2.0

        if self.maps3:
            self.cobblestone.draw(self.screen)
            self.setting.tank_opening_speed = 2.0
        
        self.tankAllies.blitme()
        self.tankOpening.blit_me()
        """
        ^self.screen.fill harus ditampilkan terlebih dahulu karena fill untuk mengisi background dari layar
        ^Kemudia layar dapat diisi dengan gambar tank
        ^fill ditempatkan diawal karena agar gambar tank tidak tertutupi
        """
        self.sb.show_score()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        #Tank Enemys
        if self.activation.game_active:
            self.red_tank.draw(self.screen)
            self.blue_tank.draw(self.screen)
            self.green_tank.draw(self.screen)
            self._update_tank()



        
        #For Menu Interface
        self.containerInterface.draw_container()
        self.settingInterface.draw_container()
        self.levelInterface.draw_container()

        if self.settingInterface.setting_present:
            self.containerInterface.menu_present = False

        pygame.display.flip()

    #This For Opening Tank When Game Paused
    def _update_tank_opening(self):
        self._check_direction_tank_opening()

    def _check_direction_tank_opening(self):
        if self.tankOpening.check_edges():
            self._change_direction_tank_opening()

    def _change_direction_tank_opening(self):
        self.setting.edges_tank_opening *= -1

    #Run Game
    def run_game(self):
        while True:
            self._check_event()
            if self.activation.game_active:
                self._update_bullets()
                self.tankAllies.blitme()
                self.tankAllies.update_ship()

            if not self.activation.game_active:
                self.tankOpening.update_ship()
                self._update_tank_opening()


            self.tankOpening.blit_me()
            self._update_screen()


if __name__ == '__main__':
    ai = MainClass()
    ai.run_game()