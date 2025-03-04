import json
class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = self.load_high_score()

    def load_high_score(self):
        filename = 'high_score.json'
        try:
            with open(filename, 'r') as f:
                high_score = json.load(f)
                return high_score
        except FileNotFoundError:
            with open(filename, 'w') as f:
                json.dump(0, f)
            high_score = 0
            return high_score

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        self.level = 1

    