# flappy bird

编程语言：python，使用的是pygame

### 游戏规则：
  游戏中有两个角色（一只鸟，一只皮卡丘（简称pika）），可以通过上，左，右键控制鸟，w，s键控制pika，按空格键可控制pika发射子弹击中气球。两个角色是同步移动的，但是当皮卡掉到地上就只能人为的把他拉上去。右下角还会不停地扔出一个精灵球（简称球吧）。其实就是将flappy bird 与打气球游戏结合在一起了。能力有限，做得非常简陋。因为感觉叫做flappy bird也没问题，所以名字就草率的决定叫flappy bird了。

### 游戏特点：
  地图的移动（好像也不是特点），其实也就是将两张一样的图片一起移动，你也可以贴几朵云，只是我懒得加。。。  
  碰撞检测：制作过程中做了许多碰撞检测（鸟，皮卡与管道，气球，地面以及球的碰撞的碰撞，子弹与气球的碰撞），完成后的我一度不想再做碰撞检测了。



```markdown


因为文件很乱，在这里我解释一下我的文件吧
main.py -- 主程序（我好像放了好多乱七八糟的东西）
map.py --  地图（主要是实现了地图的滚动）
ball.py -- 就是右下角仍的那个球
bobo.py -- 那只别扭的鸟
pika.py --  违和的金皮卡
bullet.py -- 子弹
pip.py  -- 管道
qiqiu.py -- 气球
scoreboard.py -- 记录分数
button.py  -- 制作按键（就是那个简陋的“开始”键）
game_function -- 游戏功能实现（虽然有好多被我移到main里去了）
剩下的基本就是图片了。。。


```


ball.py  
#其实这些障碍物的写法都差不多，我就只贴那个球的代码了
```markdown

import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self, screen, bo):
        super(Ball, self).__init__()
        self.screen = screen
        self.x = bo.centerx
        self.y = bo.centery
        self.ball = pygame.image.load("ball.png")   #加载图片
        self.mask = pygame.mask.from_surface(self.ball)  #mask属性可以罩住图片的透明部分

        self.rect = self.ball.get_rect()
        
        self.rect.centerx = 750
        self.rect.centery = 350

       
        self.speed = [2, 3]       #设置球的x，y方向的速度
        self.speed[1] = self.y/self.x * self.speed[0]

    def update(self):
        #if self.rect.x >= 0 or self.rect.y >= 0:
        self.rect.centerx -= 5
        self.rect.centery -= 2

    def draw_ball(self):
        self.screen.blit(self.ball, self.rect)  #将球在屏幕上画出来

```

接下来是game_function.py
```markdown
#名字都和前面介绍的一样，这里我就不解释了
import sys
import pygame
from pip import pip_g

from random import *
#from button import Button
from bullet import Bullet

def fire_bullet(screen, pika, bullets):
    #开火！！！
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
    """响应按下"""
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
           
```
能力有限，剩下代码我就不解释了。  
学习pygame推荐目光博客，讲解很清楚:http://eyehere.net/category/python/


pygaem新手，有许多错误或者不合适的地方还请见谅
