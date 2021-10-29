import pygame
from InterfaceActivation import InterfaceActivation

class ContainerInterface:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = ai_game.setting
        self.width = self.setting.display_width / 4
        self.height = self.setting.display_height / 2
        self.button_width = 200
        self.button_height = 50
        self.menu_width = 300
        self.menu_height = 70
        self.color = (175, 238, 239)
        self.frame_color = (152, 251, 153)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.container_rect = pygame.Rect(0, 0, self.width, self.height)
        self.container_menu_rect = pygame.Rect(0, 0, self.menu_width, self.menu_height)
        self.play_button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.exit_button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.level_button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.setting_button_rect = pygame.Rect(0, 0, self.button_width, self.button_height)

        self.container_rect.center = (self.screen_rect.width / 2, self.screen_rect.height / 2)
        self.container_menu_rect.center = (self.screen_rect.width/2, (self.screen_rect.height/2) - (self.height/2) + 1.5 * (self.menu_height/2))
        self.play_button_rect.center = (self.screen_rect.width/2, (self.screen_rect.height/2) - (self.height/2) + 2 * (self.menu_height))
        self.exit_button_rect.center = (self.screen_rect.width/2, self.screen_rect.height/2 + 7)
        self.level_button_rect.center = (self.screen_rect.width/2, (self.screen_rect.height/2) + (self.height/2) - 2.5 * (self.button_height))
        self.setting_button_rect.center = (self.screen_rect.width/2, (self.screen_rect.height/2) + (self.height/2) - 2 * (self.button_height/2))

        self._prep_msg()
        self.menu_present = True

    def _prep_msg(self):
        #Prep digunakan untuk menggambar atau meulis suatu tulisan dengan merender menggunakan librarty pycharm
        self.menu_msg = self.font.render("MENU", True, self.text_color, self.frame_color)
        self.play_msg = self.font.render("PLAY", True, self.text_color, self.frame_color)
        self.exit_msg = self.font.render("EXIT", True, self.text_color, self.frame_color)
        self.level_msg = self.font.render("LEVEL", True, self.text_color, self.frame_color)
        self.setting_msg = self.font.render("SETTING", True, self.text_color, self.frame_color)

        self.menu_msg_rect = self.menu_msg.get_rect()
        self.play_msg_rect = self.play_msg.get_rect()
        self.exit_msg_rect = self.exit_msg.get_rect()
        self.level_msg_rect = self.level_msg.get_rect()
        self.setting_msg_rect = self.setting_msg.get_rect()

        self.menu_msg_rect.center = (self.screen_rect.width/2, (self.screen_rect.height/2) - (self.height/2) + 1.5 * (self.menu_height/2))
        self.play_msg_rect.center = (self.screen_rect.width/2, (self.screen_rect.height/2) - (self.height/2) + 2 * (self.menu_height))
        self.exit_msg_rect.center = (self.screen_rect.width/2, self.screen_rect.height/2 + 7)
        self.level_msg_rect.center = (self.screen_rect.width/2, (self.screen_rect.height/2) + (self.height/2) - 2.5 * (self.button_height))
        self.setting_msg_rect = (self.screen_rect.width/2 - 3 * (self.button_height/2), (self.screen_rect.height/2) + (self.height/2) - 2.5 * (self.button_height/2))

    def draw_container(self):
        if self.menu_present:
            self.screen.fill(self.color, self.container_rect)
            self.screen.fill(self.frame_color, self.container_menu_rect)
            self.screen.fill(self.frame_color, self.play_button_rect)
            self.screen.fill(self.frame_color, self.exit_button_rect)
            self.screen.fill(self.frame_color, self.level_button_rect)
            self.screen.fill(self.frame_color, self.setting_button_rect)
            self.screen.blit(self.menu_msg, self.menu_msg_rect)
            self.screen.blit(self.play_msg, self.play_msg_rect)
            self.screen.blit(self.exit_msg, self.exit_msg_rect)
            self.screen.blit(self.level_msg, self.level_msg_rect)
            self.screen.blit(self.setting_msg, self.setting_msg_rect)

class SettingInterface:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = ai_game.setting
        self.width = self.setting.display_width / 4
        self.height = self.setting.display_height / 2
        self.button_width = 200
        self.button_height = 50
        self.setting_width = 300
        self.setting_height = 70
        self.label_width = 385
        self.label_height = 70
        self.color = (62, 254, 255)
        self.frame_color = (48, 206, 209)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.container = pygame.Rect(0, 0, self.width, self.height)
        self.setting_label = pygame.Rect(0, 0, self.setting_width, self.setting_height)
        self.map_label = pygame.Rect(0, 0, self.label_width, self.label_height)
        self.button_maps1 = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.button_maps2 = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.button_maps3 = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.button_back = pygame.Rect(0, 0, self.button_width, self.button_height)

        self.container.center = (self.screen_rect.width / 2, self.screen_rect.height / 2)
        self.setting_label.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) - 2.5 * (self.setting_height))
        self.map_label.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) - 1.4 * (self.label_height))
        self.button_maps1.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) - 0.3 * (self.button_height))
        self.button_maps2.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) + 1.1 * (self.button_height))
        self.button_maps3.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) + 2.5 * (self.button_height))
        self.button_back.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) + 3.8 * (self.button_height))

        self.setting_present = False
        self._prep_msg()

    def _prep_msg(self):
        self.setting_label_msg = self.font.render("Setting", True, self.text_color, self.frame_color)
        self.map_label_msg = self.font.render("Choose Preferred Map", True, self.text_color, self.frame_color)
        self.button_maps1_msg = self.font.render("MAPS 1", True, self.text_color, self.frame_color)
        self.button_maps2_msg = self.font.render("MAPS 2", True, self.text_color, self.frame_color)
        self.button_maps3_msg = self.font.render("MAPS 3", True, self.text_color, self.frame_color)
        self.button_back_msg = self.font.render("BACK", True, self.text_color, self.frame_color)

        self.setting_label_msg_rect = self.setting_label_msg.get_rect()
        self.map_label_msg_rect = self.map_label_msg.get_rect()
        self.button_maps1_msg_rect = self.button_maps1_msg.get_rect()
        self.button_maps2_msg_rect = self.button_maps2_msg.get_rect()
        self.button_maps3_msg_rect = self.button_maps3_msg.get_rect()
        self.button_back_msg_rect = self.button_back_msg.get_rect()

        self.setting_label_msg_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) - 2.5 * (self.setting_height))
        self.map_label_msg_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) - 1.4 * (self.label_height))
        self.button_maps1_msg_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) - 0.3 * (self.button_height))
        self.button_maps2_msg_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) + 1.1 * (self.button_height))
        self.button_maps3_msg_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) + 2.5 * (self.button_height))
        self.button_back_msg_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) + 3.8 * (self.button_height))

    def draw_container(self):
        if self.setting_present:
            self.screen.fill(self.color, self.container)
            self.screen.fill(self.frame_color, self.setting_label)
            self.screen.fill(self.frame_color, self.map_label)
            self.screen.fill(self.frame_color, self.button_maps1)
            self.screen.fill(self.frame_color, self.button_maps2)
            self.screen.fill(self.frame_color, self.button_maps3)
            self.screen.blit(self.setting_label_msg, self.setting_label_msg_rect)
            self.screen.blit(self.map_label_msg, self.map_label_msg_rect)
            self.screen.blit(self.button_maps1_msg, self.button_maps1_msg_rect)
            self.screen.blit(self.button_maps2_msg, self.button_maps2_msg_rect)
            self.screen.blit(self.button_maps3_msg, self.button_maps3_msg_rect)
            self.screen.blit(self.button_back_msg, self.button_back_msg_rect)


class LevelInterface:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = self.screen.get_rect()
        self.activation = InterfaceActivation()
        self.width = self.setting.display_width / 4
        self.height = self.setting.display_height / 2
        self.button_width = 280
        self.button_height = 65
        self.label_width = 300
        self.label_height = 60
        self.color = (176, 224, 230)
        self.level1_color = (144, 238, 144)
        self.level2_color = (251, 160, 122)
        self.level3_color = (250, 69, 1)
        self.level_color = (144, 238, 144)
        self.frame_color = (135, 206, 235)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("Arial", 48)

        self.container = pygame.Rect(0, 0, self.width, self.height)
        self.level_label_rect = pygame.Rect(0, 0, self.label_width, self.label_height)
        self.level1_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.level2_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.level3_rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.level_screen_rect = pygame.Rect(0, 0, self.label_width + 50, self.label_height)
        self.border_rect = pygame.Rect(0, 0, self.setting.display_width, 5)
        self.back_rect = pygame.Rect(0, 0, self.button_width, self.button_height)

        self.container.center = (self.setting.display_width / 2, self.setting.display_height / 2)
        self.level_label_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) - 3 * (self.label_height))
        self.level1_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) - 1.5 * (self.label_height))
        self.level2_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2))
        self.level3_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) + 1.5 * (self.button_height))
        self.level_screen_rect.center = (self.screen_rect.width / 2, 40)
        self.border_rect.center = (self.screen_rect.width / 2, 70)
        self.back_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) + 2.8 * (self.button_height))

        self.level_present = False
        self._prep_msg()

    def _prep_msg(self):
        self.level_label_msg = self.font.render("Choose Level", True, self.text_color, self.frame_color)
        self.level1_rect_msg = self.font.render("LEVEL Easy", True, self.text_color, self.level1_color)
        self.level2_rect_msg = self.font.render("LEVEL Medium", True, self.text_color, self.level2_color)
        self.level3_rect_msg = self.font.render("LEVEL Hard", True, self.text_color, self.level3_color)
        self.level_screen_rect_msg = self.font.render(f"Level : {self.setting.level_game}", True, self.text_color, self.level_color)
        self.back_rect_msg = self.font.render("BACK", True, self.text_color, self.frame_color)

        self.level_label_msg_rect = self.level_label_msg.get_rect()
        self.level1_rect_msg_rect = self.level1_rect_msg.get_rect()
        self.level2_rect_msg_rect = self.level2_rect_msg.get_rect()
        self.level3_rect_msg_rect = self.level3_rect_msg.get_rect()
        self.level_screen_rect_msg_rect = self.level_screen_rect_msg.get_rect()
        self.back_rect_msg_rect = self.back_rect_msg.get_rect()

        self.level_label_msg_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) - 3 * (self.label_height))
        self.level1_rect_msg_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) - 1.5 * (self.label_height))
        self.level2_rect_msg_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2))
        self.level3_rect_msg_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) + 1.5 * (self.button_height))
        self.level_screen_rect_msg_rect.center = (self.screen_rect.width / 2, 40)
        self.back_rect_msg_rect.center = (self.screen_rect.width / 2, (self.screen_rect.height / 2) + 2.8 * (self.button_height))

    def draw_container(self):
        if self.level_present:
            self.screen.fill(self.color, self.container)
            self.screen.fill(self.frame_color, self.level_label_rect)
            self.screen.fill(self.level1_color, self.level1_rect)
            self.screen.fill(self.level2_color, self.level2_rect)
            self.screen.fill(self.level3_color, self.level3_rect)
            self.screen.blit(self.level_label_msg, self.level_label_msg_rect)
            self.screen.blit(self.level1_rect_msg, self.level1_rect_msg_rect)
            self.screen.blit(self.level2_rect_msg, self.level2_rect_msg_rect)
            self.screen.blit(self.level3_rect_msg, self.level3_rect_msg_rect)
            self.screen.blit(self.back_rect_msg, self.back_rect_msg_rect)


        self.screen.fill(self.level_color, self.level_screen_rect)
        self.screen.fill((0, 0, 0), self.border_rect)
        self.screen.blit(self.level_screen_rect_msg, self.level_screen_rect_msg_rect)
        self.level_screen_rect_msg = self.font.render(f"Level : {self.setting.level_game}", True, self.text_color, self.level_color)



