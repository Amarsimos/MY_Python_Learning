import sys
import pygame
import time
import game_fun as gf

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien  
from game_stats import GameStats
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # screen = pygame.display.set_mode((800, 600))
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    # 创建按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建游戏统计信息
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen,ship, aliens)
    #设置背景颜色
    # bg_color = (230, 230, 230)


    #游戏主循环 
    while  True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)#参数传入的顺序一定要统一,否则会报错
        # time.sleep(0.01)
        # print(1)
        if stats.game_active:
            ship.update()
            # print(len(bullets))
            gf.update_bullets(ai_settings, screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings, screen,stats,sb,ship,aliens,bullets,play_button)


run_game()