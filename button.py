import pygame.font

class Button():
    def __init__(self, size, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #设置按钮的尺寸和其他属性
        self.width, self.height = 100, 50
        self.button_color = (0, 0, 255, 255)
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont("simsunnsimsun", 48)

        #创建按钮rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.bottom = self.screen_rect.bottom/2
        self.rect.left = self.screen_rect.right/2 - 50

        #按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                               self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.top = self.rect.top + 5
        self.msg_image_rect.left = self.rect.left + 5

    def draw_bottun(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
