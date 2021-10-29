import pygame

class Settings:
    def __init__(self):
        self.display_width = 1200
        self.display_height = 800
        self.ship_speed = 5.0
        self.bg_color = (100, 239, 213)
        self.tank_opening_speed = 14.0
        self.ship_limit = 3

        #Setting for bullet
        self.bullet_color = (0, 0, 0)
        self.bullet_speed = 5.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.level_game = "EASY"

        self.edges_tank_opening = 1

        # Setting for enemies
        self.red_ship_speed = 5.0
        self.blue_ship_speed = 3.0
        self.green_ship_speed = 1.0
        self.fleet_direction = 1

        # POINT
        self.red_tank_point = 50
        self.blue_tank_point = 30
        self.green_tank_point = 10

    def get_ship_speed(self):
        return self.ship_speed

