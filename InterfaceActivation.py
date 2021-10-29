class InterfaceActivation:
    def __init__(self):
        self.menu_active = False
        self.game_active = False

    def get_game_active(self):
        return self.game_active


class GameStats():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.high_score = 0
        self.score = 0
        self.level = 1
        self.ships_left = self.setting.ship_limit

    def reset_stats(self):
        self.ships_left = self.setting.ship_limit
        self.score = 0
        self.level = 1
