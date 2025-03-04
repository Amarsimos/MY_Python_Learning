class Settings():
    def __init__(self):
        
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #飞船设置
        self.ship_limit = 3
        self.ship_speed_factor = 1.5

        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 1190
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 9

        #外星人设置
        self.fleet_drop_speed = 50
        self.alien_speed_factor = 0.1
        self.fleet_direction = 1

        #难度系数
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.1
        self.fleet_direction = 1

        #fleet_direction为1表示向右移，-1表示向左移
        self.fleet_direction = 1 
        self.score_scale = 1.5
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
