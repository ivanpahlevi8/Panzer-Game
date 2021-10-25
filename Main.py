import sys
import pygame
from Setting import Settings
from ContainerInterface import ContainerInterface
from TankAllies import TankAllies
from TankAllies import DirtyRoad
from TankAllies import River
from TankAllies import TankOpening
from Bullet import Bullet
from InterfaceActivation import InterfaceActivation

class MainClass :
    def __init__(self):
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.setting.display_width = self.screen.get_rect().width
        self.setting.display_height = self.screen.get_rect().height
        pygame.display.set_caption('Panzer War')

        self.containerInterface = ContainerInterface(self)
        self.tankAllies = TankAllies(self)
        self.tankOpening = TankOpening(self)
        self.dirty_road = pygame.sprite.Group()
        self.river = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.activation = InterfaceActivation()

        self._create_fleet_road()
        self._create_fleet_river()


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
                self._check_play_button(mouse_event)
                self._check_exit_button(mouse_event)

    def _check_play_button(self, mouse_event):
        button = self.containerInterface.play_button_rect.collidepoint(mouse_event)

        if button and not self.activation.game_active:
            self.activation.game_active = True
            self.screen.fill((0, 0, 0))
            self.tankOpening.active = False
            self.tankAllies.active = True
            self.containerInterface.menu_present = False

    def _check_exit_button(self, mouse_event):
        button = self.containerInterface.exit_button_rect.collidepoint(mouse_event)

        if button and not self.activation.game_active:
            sys.exit()


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

    def _menu_present(self):
        self.activation.game_active = False
        self.tankAllies.active = False
        self.containerInterface.menu_present = True
        self.tankOpening.active = True
        self.tankOpening.update_ship()

    def _create_fleet_road(self):
        new_road = DirtyRoad()
        road_width = new_road.rect.width
        road_height = new_road.rect.height

        availabel_road_x = self.setting.display_width // road_width + 1
        availabel_road_y = self.setting.display_height // road_height + 1

        for y in range(availabel_road_y):
            for x in range(availabel_road_x):
                self._create_road(x, y)
    
    def _create_fleet_river(self):
        new_river = River()
        river_height = new_river.rect.height
        
        available_river_y = self.setting.display_height // river_height + 1
        
        for y in range (available_river_y):
            self._create_river(y)
        
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

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)
        self.dirty_road.draw(self.screen)
        self.river.draw(self.screen)
        self.tankAllies.blitme()
        self.tankOpening.blit_me()
        """
        ^self.screen.fill harus ditampilkan terlebih dahulu karena fill untuk mengisi background dari layar
        ^Kemudia layar dapat diisi dengan gambar tank
        ^fill ditempatkan diawal karena agar gambar tank tidak tertutupi
        """

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.containerInterface.draw_container()

        pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()
        # Menghapus peluru yang telah di gambar jika peluru telah melewati batas layar
        for bullet in self.bullets.copy():
            if bullet.rect.bottom >= self.setting.display_width:
                self.bullets.remove(bullet)

    def _update_tank_opening(self):
        self._check_direction_tank_opening()

    def _check_direction_tank_opening(self):
        if self.tankOpening.check_edges():
            self._change_direction_tank_opening()

    def _change_direction_tank_opening(self):
        self.setting.edges_tank_opening *= -1

    def run_game(self):
        while True:
            self._check_event()
            if self.activation.game_active:
                self._update_bullets()
                self.tankAllies.blitme()
                self.tankAllies.update_ship()

            if not self.activation.game_active:
                self.containerInterface.menu_present = True
                self.tankOpening.update_ship()
                self._update_tank_opening()

            self.tankOpening.blit_me()
            self._update_screen()


if __name__ == '__main__':
    ai = MainClass()
    ai.run_game()