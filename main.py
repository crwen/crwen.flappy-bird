#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame
import traceback
from random import *
from pygame.sprite import Group
from qiqiu import Qiqiu

import game_function as gf
from bobo import bobo, zhushou
from map import map
import pip
from button import Button
from scoreboard import Scoreboard
from ball import Ball


pygame.init()
size = width, height = 700, 400
screen = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("波波の仕事")

bg = map(screen)

clock = pygame.time.Clock()

pg = pip.pip_g(screen, size)

pr = pip.pip_r(screen, size)
pips = [pg, pr]


def main():
    #创建波波
    speed = 4
    bo = bobo(screen, speed, 50, 200)
    pika = zhushou(screen, bo.centerx, bo.centery)
    enemy = pygame.image.load("enemy.png")
    wuzang = pygame.image.load("huojiandui.png").convert_alpha()
    #创建管道
    p1 = pips[randint(0, len(pips) - 1)]
    p2 = pips[randint(0, len(pips) - 1)]
    p3 = pips[randint(0, len(pips) - 1)]
    p4 = pips[randint(0, len(pips) - 1)]

    #创建气球
    #qiqius = pygame.sprite.Group()
    qiqiu1 = Qiqiu(screen, bo)
    qiqiu2 = Qiqiu(screen, bo)
    qiqiu3 = Qiqiu(screen, bo)
    qiqiu4 = Qiqiu(screen, bo)

    #创建球
    balls = Ball(screen, bo)
    #开始按键
    words = "开始"
    word_frame = Button(size, screen, words)
    returns = "返回主屏幕"
    return_frame = Button(size, screen, returns)
    scores = 0
    #分数
    x = width - 20
    y = 20
    sb = Scoreboard(screen, scores, x, y)
    gameover = pygame.image.load("gameover.png")
    game_over = False

    image = pygame.image.load("background.png")
    stats = False
    delay = 100

    #创建子弹
    bullets = pygame.sprite.Group()
    while not game_over:
        moup=pygame.mouse.get_pressed()
        mou_pos=pygame.mouse.get_pos()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if stats:    
            screen.fill((255, 255, 255))

            #绘制背景
            bg.draw()
            bg.move()
            #绘制boob和pika
            bo.blitme()
            y1 = bo.centery
            pika.blitme()
            pygame.draw.rect(screen, (0, 0, 0), (bo.centerx, bo.centery, 2, pika.centery  - bo.centery))

            #绘制气球， 分数小于100，2个，大于100， 3个，大于200，4个
            p1.blitme()
            p2.blitme()
            qiqiu1.blitme()
            qiqiu1.move()
            qiqiu2.blitme()
            qiqiu2.move()
            if scores > 100:
                qiqiu3.blitme()
                qiqiu3.move()
            if scores > 200:
                qiqiu4.blitme()
                qiqiu4.move()

            
            gf.check_event(bo, screen, pika, bullets)
            bullets.update()


            gf.update_bullets(screen, pika, bullets)
            for bullet in bullets.sprites():
                bullet.draw_bullet()



            bo.update()
            y2 = bo.centery
            pika.update(bo.centery, y2 - y1, bo.centerx)
            x1 = p1.rect.centerx
            if bo.centerx == x1:
                scores += 10
            
            p1.move()
            x2 = p2.rect.centerx
            if bo.centerx == x2:
                scores += 10         
            
            p2.move()

            #扔球
            if balls.rect.x > -150 and balls.rect.y > -150:
                balls.update()
                balls.draw_ball()    
            else:
                pygame.sprite.Sprite.kill(balls)
                balls = Ball(screen, bo)
            #落地检测
            if bo.centery > height - 10:
                screen.blit(gameover, (200, 100))
                #打印死亡分数
                x = 400
                y = 180
                sb = Scoreboard(screen, scores, x, y)
                sb.show()
  
                game_over = True
            #碰撞检测
            if pygame.sprite.collide_mask(bo,p1) or pygame.sprite.collide_mask(bo, p2) \
            or pygame.sprite.collide_mask(pika, p1) or pygame.sprite.collide_mask(pika, p2):            
                screen.blit(gameover, (200, 100))
                #打印死亡分数
                x = 400
                y = 180
                sb = Scoreboard(screen, scores, x, y)
                sb.show()
                game_over = True

            
            
            if pygame.sprite.collide_mask(bo,qiqiu1) or pygame.sprite.collide_mask(bo,qiqiu2) \
            or pygame.sprite.collide_mask(bo,qiqiu3) or pygame.sprite.collide_mask(bo,qiqiu4):
                screen.blit(gameover, (200, 100))
                #打印死亡分数
                x = 400
                y = 180
                sb = Scoreboard(screen, scores, x, y)
                sb.show()
                game_over = True
            
            rect1 = bo.rect.clip(p1.rect2)
            rect2 = bo.rect.clip(p2.rect2)
            rect3 = pika.rect.clip(p1.rect2)
            rect4 = pika.rect.clip(p2.rect2)
            if (rect1.width > 10 and rect1.height > 10) or (rect2.width > 15 and rect2.width > 15) or \
               (rect3.width > 10 and rect3.height > 10) or (rect4.width > 10 and rect4.width > 10):
                screen.blit(gameover, (200, 100))
                #打印死亡分数
                x = 400
                y = 180
                sb = Scoreboard(screen, scores, x, y)
                sb.show()
                game_over = True


            if (qiqiu1.rect.centerx < 800 and pygame.sprite.spritecollide(qiqiu1,bullets,True)):
                scores += 10
                qiqiu1.reset()
            if (qiqiu2.rect.centerx < 800 and pygame.sprite.spritecollide(qiqiu2,bullets,True)):
                scores += 10
                qiqiu2.reset()                
            if (qiqiu3.rect.centerx < 800 and pygame.sprite.spritecollide(qiqiu3,bullets,True)):
                scores += 10
                qiqiu3.reset()
            if (qiqiu4.rect.centerx < 800 and pygame.sprite.spritecollide(qiqiu4,bullets,True)):
                scores += 10
                qiqiu4.reset()

                

        
            #球与鸟的碰撞
            if pygame.sprite.collide_mask(bo, balls):
                pygame.sprite.Sprite.kill(balls)
                #减速
                speed -= 0.5
                x = bo.centerx
                y = bo.centery
                bo = bobo(screen, speed, x, y)
                
                balls = Ball(screen, bo)
            
            #打印分数
            x = width - 20
            y = 20
            sb = Scoreboard(screen, scores, x, y)
            sb.show()

            screen.blit(enemy, (600, 300))
                        
            
            if p1.rect.centerx <= -26:
                pygame.sprite.Sprite.kill(p1)
                p1 = pips[randint(0, len(pips) - 1)]
            if p2.rect.centerx <= -26:
                pygame.sprite.Sprite.kill(p2)
                p2 = pips[randint(0, len(pips) - 1)]


            if game_over == True:
                for event in pygame.event.get():
    
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESC:
                            stats = False

                    
                    
            clock.tick(60)
        else:
            screen.blit(image, (0, 0))
            word_frame.draw_bottun()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if word_frame.rect.collidepoint(mouse_x, mouse_y):
                        stats = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:
                        stats = True
        pygame.display.flip()

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
