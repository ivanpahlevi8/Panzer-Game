import pygame
from pygame.sprite import Sprite
from InterfaceActivation import InterfaceActivation


class TankAllies(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = ai_game.setting
        self.image = pygame.image.load('Allies1.png')
        self.activation = InterfaceActivation()

        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        #gerak dari panzer
        self.move_up = False
        self.move_right = False
        self.move_left = False
        self.move_down = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.active = False

    def blitme(self):
        if self.active:
            self.screen.blit(self.image, self.rect)

    def update_ship(self):
        if self.move_up and self.rect.y > 80:
            self.y -= self.setting.get_ship_speed()
        elif self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.get_ship_speed()
        elif self.move_left and self.rect.left > 0:
            self.x -= self.setting.get_ship_speed()
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.get_ship_speed()

        self.rect.x = self.x
        self.rect.y = self.y


class TankOpening:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.setting = ai_game.setting
        self.activation = InterfaceActivation()
        self.image1 = pygame.image.load('Red1.png')
        self.image2 = pygame.image.load('Blue1.png')
        self.image3 = pygame.image.load('Green1.png')

        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect3 = self.image3.get_rect()

        self.rect1.midright = (self.setting.display_width - 20, self.setting.display_height / 2)
        self.rect2.midright = (self.setting.display_width - 20, self.setting.display_height / 2 + 200)
        self.rect3.midright = (self.setting.display_width - 20, self.setting.display_height / 2 - 200)

        self.x1 = float(self.rect1.x)
        self.x2 = float(self.rect2.x)

        self.x3 = float(self.rect3.x)

        self.active = True

    def blit_me(self):
        if self.active:
            self.screen.blit(self.image1, self.rect1)
            self.screen.blit(self.image2, self.rect2)
            self.screen.blit(self.image3, self.rect3)

    def check_edges(self):
        premis1 = self.rect1.right >= self.screen_rect.right and self.rect2.right >= self.screen_rect.right and self.rect3.right >= self.screen_rect.right
        premis2 = self.rect1.left <= 0 and self.rect2.left <= 0 and self.rect3.left <= 0

        if premis1 or premis2:
            return True

    def update_ship(self):
        self.x1 = self.x1 + self.setting.tank_opening_speed * self.setting.edges_tank_opening
        self.x2 = self.x2 + self.setting.tank_opening_speed * self.setting.edges_tank_opening
        self.x3 = self.x3 + self.setting.tank_opening_speed * self.setting.edges_tank_opening

        self.rect1.x = self.x1
        self.rect2.x = self.x2
        self.rect3.x = self.x3

class DirtyRoad(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('dirty-road.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

class River(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('river2.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

class Highway(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('highway.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

class Cobblestone(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('cobble.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)