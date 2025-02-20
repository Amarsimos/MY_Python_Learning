import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.centery = self.screen_rect.centery

        #存储飞船的位置小数
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.bottom = float(self.rect.bottom)
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动方向更新飞船位置"""
        #移动飞船
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
            # self.rect.centerx += 1.5
        if self.moving_left and self.rect.left > 0:
            # self.center -= 2
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
            # self.rect.centerx += 1.5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
            # self.rect.centerx += 1.5
        #更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image,self.rect)
    
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom-self.rect.height/2