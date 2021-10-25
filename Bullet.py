import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color
        self.width = self.setting.bullet_width
        self.height = self.setting.bullet_height

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midright = (ai_game.tankAllies.x + ai_game.tankAllies.rect.width/2 + 70, ai_game.tankAllies.y - ai_game.tankAllies.rect.height/2 + 23)
        self.x = float(self.rect.x)

    def update(self):
        self.x = self.x + self.setting.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)