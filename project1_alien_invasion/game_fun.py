import sys
import pygame
import time

from bullet import Bullet
from alien import Alien
from random import randint
import json

def check_keydown_events(event,ai_settings, screen, ship,bullets,stats):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship,bullets)
        # bullets.put_shot_flag(True)
    elif event.key == pygame.K_q:
        save_high_score(stats)
        sys.exit()
       
def fire_bullet(ai_settings, screen, ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_up_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_up_bullet)
        new_right_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_right_bullet)

def check_keyup_events(event,ai_settings, screen, ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    # elif event.key == pygame.K_SPACE:
        # bullets.put_shot_flag(False)

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # print(event.key)
            check_keydown_events(event,ai_settings,screen,ship,bullets,stats)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen,ship,aliens)
        ship.center_ship()

def update_screen(ai_settings, screen,stats,sb,ship,aliens,bullets,play_button):
    #更新屏幕并切换到新屏幕
    #填充背景色
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    # screen.fill(bg_color)
    # while Bullet.shot_flag:
    #     new_bullet = Bullet(ai_settings, screen, ship)
    #     bullets.add(new_bullet)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    sb.show_score()
    #如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats,sb,ship,aliens,bullets):
    # bullets.update_u()  pygame.sprite.Group 类有一个内置的 update() 方法，它会自动对编组中的每个精灵（在这个项目中是 Bullet 对象）调用各自的 update() 方法
    bullets.update()
    for bullet in bullets.copy():
        # bullet.update_r()
        bullet.update_u()
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom  <= 0 or bullet.rect.right>= bullet.screen_rect.right:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings, screen,stats,sb,ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points *len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    
    
    
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        
        create_fleet(ai_settings, screen,ship,aliens)


def create_fleet(ai_settings, screen,ship,aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width) 
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen,aliens,alien_number,row_number)

def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    random_number = randint(-30,30) 
    alien.rect.x = alien.x + random_number
    # alien.rect.x = alien.x 
    alien.rect.y = alien.rect.height + random_number+ 2 * alien.rect.height * row_number
    # alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def check_aliens_bottom(ai_settings,stats,sb, screen, ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats, sb,screen, ship,aliens,bullets)
            break

def update_aliens(ai_settings,stats, screen,sb, ship,aliens,bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!!!")
    
        ship_hit(ai_settings,stats, screen, sb,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,stats, screen, sb,ship,aliens,bullets)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,sb, screen, ship,aliens,bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1

        aliens.empty()
        bullets.empty()

        sb.prep_ships()

        create_fleet(ai_settings, screen,ship,aliens)
        ship.center_ship()

        time.sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()



def save_high_score(stats):
    filename = "high_score.json"
    with open(filename, "w") as f:
        json.dump(stats.high_score, f)