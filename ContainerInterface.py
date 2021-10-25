import pygame

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
        self.menu_present = False

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

