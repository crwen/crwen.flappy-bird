import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, screen, pika):
        super(Bullet, self).__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0, 15, 3)

        #self.rect = self.image.get_rect()
        #self.mask = pygame.mask.from_surface(self.image)
        
        self.rect.centerx = pika.rect.centerx
        self.rect.top = pika.rect.top + 15


        #用小数表示子弹位置
        self.x = float(self.rect.x)
        self.color = 255, 0, 0 
        
        self.speed = 3

    def update(self):

        self.x += self.speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        #self.screen.blit(self.image, self.rect)
        
