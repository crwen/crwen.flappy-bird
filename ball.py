import pygame
from pygame.sprite import Sprite



class Ball(Sprite):
    def __init__(self, screen, bo):
        super(Ball, self).__init__()
        self.screen = screen
        self.x = bo.centerx
        self.y = bo.centery
        self.ball = pygame.image.load("ball.png")
        self.mask = pygame.mask.from_surface(self.ball)

        self.rect = self.ball.get_rect()
        
        self.rect.centerx = 750
        self.rect.centery = 350

       
        self.speed = [2, 3]
        self.speed[1] = self.y/self.x * self.speed[0]

    def update(self):
        #if self.rect.x >= 0 or self.rect.y >= 0:
        self.rect.centerx -= 5
        self.rect.centery -= 2
        


    def draw_ball(self):
        self.screen.blit(self.ball, self.rect)
        
        
