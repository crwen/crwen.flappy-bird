import pygame.font

class Scoreboard():
    """显示得分信息"""
    def __init__(self, screen, scores, x, y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.scores = scores
        self.x, self.y = x, y

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()


    def prep_score(self):
        """将得分渲染为一幅图像"""
        score_str = str(self.scores)
        self.score_image = self.font.render(score_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.x
        self.score_rect.top = self.y


    def show(self):
        self.screen.blit(self.score_image, self.score_rect)
