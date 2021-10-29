import pygame
from pygame.sprite import Sprite

class RedTank(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting

        self.image = pygame.image.load('Red1.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # memposisiikan alien di pojok kiri atas

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x -= (self.setting.red_ship_speed * self.setting.fleet_direction)

        self.rect.x = self.x


class BlueTank(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting

        self.image = pygame.image.load('Blue1.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # memposisiikan alien di pojok kiri atas

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x -= (self.setting.blue_ship_speed * self.setting.fleet_direction)

        self.rect.x = self.x


class GreenTank(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting

        self.image = pygame.image.load('Green1.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # memposisiikan alien di pojok kiri atas

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x -= (self.setting.green_ship_speed * self.setting.fleet_direction)
        self.rect.x = self.x