import pygame
import ship
import settings

from pygame.sprite import Sprite

class Bullet(Sprite):
    # 子弹管理类
    def __init__(self, ai_settings, screen, ship):
        super(Bullet,self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.shot = False

    # 加载子弹图像
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update_u(self):
        # 更新子弹位置
        self.y -= self.speed_factor
        self.rect.y = self.y

    def update_r(self):
        self.x += self.speed_factor
        self.rect.x = self.x
        
    def get_shot_flag(self):
        # 开火
        return self.shot
    def put_shot_flag(self, flag):
        # 开火
        self.shot = flag


    def draw_bullet(self):
        # 绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)
