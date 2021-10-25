import pygame

class Settings:
    def __init__(self):
        self.display_width = 1200
        self.display_height = 800
        self.ship_speed = 7.0
        self.bg_color = (100, 239, 213)

        #Setting for bullet
        self.bullet_color = (0, 0, 0)
        self.bullet_speed = 10.0
        self.bullet_width = 15
        self.bullet_height = 3

        self.edges_tank_opening = 1

    def get_ship_speed(self):
        return self.ship_speed

