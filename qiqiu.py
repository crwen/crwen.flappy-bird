import pygame
from pygame.sprite import Sprite
from random import *


class Qiqiu(Sprite):

    def __init__(self, screen, bo):
        super(Qiqiu, self).__init__()
        self.screen = screen
        self.bo = bo

        self.red = pygame.image.load("qiqiu_red.png").convert_alpha()
        self.green = pygame.image.load("qiqiu_green.png").convert_alpha()
        self.blue = pygame.image.load("qiqiu_blue.png").convert_alpha()
        self.yellow = pygame.image.load("qiqiu_yellow.png").convert_alpha()
        
        self.images = [self.red, self.green, self.blue, self.yellow]
        self.image = self.images[randint(0, len(self.images)-1)]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.centerx = randint(bo.centerx + 300, 1000)
        self.rect.centery = randint(100, 400)


    def move(self):
        if self.rect.centerx >= -26:
            self.rect.centerx -= 1
        else:
            self.reset()

    def reset(self):
        self.image = self.images[randint(0, len(self.images) - 1)]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = 820
        self.rect.centery = randint(100, 400)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def draw(screen, bo, qiqius):
    new_qiqiu = Qiqiu(screen, bo)
    qiqius.add(new_qiqiu)

def updare_qiqiu(screen, qiqius):
    #更新气球
    qiqius.update

    #删除已消失的气球
    for qiqiu in qiqius.copy():
        if qiqiu.rect.left <= -20:
            qiqius.remove(qiqiu)
        
