import pygame

class bobo():

    def __init__(self, screen, speed, x, y):
        self.screen = screen
        self.speed = speed

        #加载图片
        self.image = pygame.image.load("juzui.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        #将波波放在起始位置
        self.rect.centerx = x
        self.rect.bottom = y

        #在波波的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        

    def update(self):
        """根据移动标志调整飞船的位置"""
        screen_rect = self.screen.get_rect()
        
        if self.moving_right and self.rect.right < screen_rect.right:
            self.centerx += 2
        if self.moving_left and self.rect.left > 0:
            self.centerx -= 2
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.speed

        self.centery += 2


        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """在指定地方绘制波波"""
        self.screen.blit(self.image, self.rect)


class zhushou():

    def __init__(self, screen, x, y):
        self.screen = screen
      
        #加载图片
        self.image = pygame.image.load("pika.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.centerx = x
        self.rect.bottom = y
        self.y = y

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.centerx = x
        self.centery = y + 200
        #移动标志
        self.moving_down = False
        self.moving_up = False
        
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
    def update(self, y, gap, x):
        screen_rect = self.screen.get_rect()
        self.centerx = x;
        if self.moving_down and self.rect.top < screen_rect.height - 40:
            self.centery += 2

        if self.moving_up and self.rect.top > y:
            self.centery -= 2
        if self.rect.top <= screen_rect.height - 40:
            self.centery += gap

        


        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
