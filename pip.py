import pygame
from random import *


class pip_g(pygame.sprite.Sprite):
    def __init__(self, screen, size):
        super(pip_g, self).__init__()

        self.screen = screen
        self.size = size
        self.pip1 = pygame.image.load("pipe-green.png").convert_alpha()
        self.pip1 = pygame.transform.rotate(self.pip1, 180)
        self.pip2 = pygame.image.load("pipe-green.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.pip1)
        self.mask = pygame.mask.from_surface(self.pip2)
        self.rect = self.pip1.get_rect()
        self.rect2 = self.pip2.get_rect()

        self.rect.centerx = randint(800, 900)
        self.rect.y = randint(-self.rect.height/2, 0)
        self.rect2.centerx = self.rect.centerx
        self.rect2.y = self.rect.height + self.rect.y + 200
        

        


    def move(self):
        if self.rect.centerx >= -26:
            self.rect.centerx -= 1
            self.rect2.centerx  -= 1

            
        else:
            self.reset()


    def reset(self):
        self.rect.centerx = randint(800, 900)
        self.rect.y = randint(-self.rect.height, 0)
        self.rect2.centerx = self.rect.centerx
        self.rect2.y = self.rect.height + self.rect.y + 200
        
        self.x1 = float(self.rect.centerx)
        self.x2 = float(self.rect2.centerx)

    def blitme(self):
        self.screen.blit(self.pip1, self.rect)
        self.screen.blit(self.pip2, self.rect2)



class pip_r(pygame.sprite.Sprite):
    def __init__(self, screen, size):
        super(pip_r, self).__init__()

        self.screen = screen
        self.size = size
        
        self.pip1 = pygame.image.load("pipe-red.png").convert_alpha()
        self.pip1 = pygame.transform.rotate(self.pip1, 180)
        self.pip2 = pygame.image.load("pipe-red.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.pip1)
        self.rect = self.pip1.get_rect()
        self.rect2 = self.pip2.get_rect()

        self.rect.centerx = randint(1000, 1100)
        self.rect.y = randint(-self.rect.height/2, 0)
        self.rect2.centerx = self.rect.centerx
        self.rect2.y = self.rect.height + self.rect.y + 200
        
        self.x1 = float(self.rect.centerx)
        self.x2 = float(self.rect2.centerx)


    def move(self):
        if self.rect.centerx >= -26:
            self.rect.centerx -= 1
            self.rect2.centerx  -= 1
            
        else:
            self.reset()


    def reset(self):
        self.rect.centerx = randint(1000, 1100)
        self.rect.y = randint(-self.rect.height, 0)
        self.rect2.centerx = self.rect.centerx
        self.rect2.y = self.rect.height + self.rect.y + 200
        
        self.x1 = float(self.rect.x)
        self.x2 = float(self.rect2.x)

    def blitme(self):
        self.screen.blit(self.pip1, self.rect)
        self.screen.blit(self.pip2, self.rect2)


