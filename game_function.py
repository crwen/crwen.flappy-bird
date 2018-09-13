import sys
import pygame
from pip import pip_g

from random import *
#from button import Button
from bullet import Bullet

def fire_bullet(screen, pika, bullets):

    new_bullet = Bullet(screen, pika)
    bullets.add(new_bullet)

def update_bullets(screen, pika, bullets):
    #更新子弹
    bullets.update()

    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.left >= 800:
            bullets.remove(bullet)

def check_keydown_event(event, bo, pika, bullets, screen):
    """响应案件"""
    if event.key == pygame.K_LEFT:
        bo.moving_left = True
    elif event.key == pygame.K_RIGHT:
        bo.moving_right = True
    elif event.key == pygame.K_UP:
        bo.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(screen, pika, bullets)
    if event.key == pygame.K_w:
        pika.moving_up = True
    elif event.key == pygame.K_s:
        pika.moving_down = True

def check_keyup_event(event, bo, pika):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        bo.moving_right = False
    elif event.key == pygame.K_LEFT:
        bo.moving_left = False
    elif event.key == pygame.K_UP:
        bo.moving_up = False
    if event.key == pygame.K_w:
        pika.moving_up = False
    elif event.key == pygame.K_s:
        pika.moving_down = False

def check_event(bo, screen, pika, bullets):
    """响应按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, bo, pika)

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, bo, pika, bullets, screen)

def update_screen(screen, bo, bg, p1, p2, *scores, size, pips, gameover, height, game_over):
    screen.fill((0, 0, 0))
    bg.move()
    bg.draw()
    

    bo.blitme()
    bo.update()
    p2.blitme()
    p1.blitme()
    p1.move()
    p2.move()
    if p1.rect1.centerx == bo.rect.centerx or p2.rect1.centerx == bo.rect.centerx:
        scores += 10
    score = Button(size, screen, str(scores), 60, 40, (220, 220, 220), (0, 255, 255, 255))
    score.draw_button()

    if bo.centery > height - 10:
        screen.blit(gameover, (200, 100))
    
        

    
    pygame.display.flip()
