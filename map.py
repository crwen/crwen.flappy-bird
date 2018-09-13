import pygame

class map():

    def __init__(self, screen):
        self.screen = screen
        self.bg1 = pygame.image.load("background.png")
        self.bg2 = pygame.image.load("background.png")

        self.bg1_rect = self.bg1.get_rect()
        self.bg2_rect = self.bg2.get_rect()
        self.screen_rect = screen.get_rect()

        self.bg1_rect.x = 0
        self.bg2_rect.x = self.screen_rect.right


    def move(self):
        screen_rect = self.screen.get_rect()
        self.bg1_rect.x -= 1
        self.bg2_rect.x -= 1

        if self.bg1_rect.x <= -self.screen_rect.right:
            self.bg1_rect.x = 0
            self.bg2_rect.x = self.screen_rect.right
        #if self.bg2_rect.x <= -self.screen_rect.right:
          #  self.bg2_rect.x = 0
            

    def draw(self):
        self.screen.blit(self.bg1, (self.bg1_rect.x, 0))
        self.screen.blit(self.bg2, (self.bg2_rect.x, 0))

