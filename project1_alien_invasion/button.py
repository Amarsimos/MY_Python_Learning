import pygame.font

class Button():
    def __init__(self,ai_settings,screen,msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.botton_color = (0,0,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.prep_msg(msg)

    #信息显示
    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.botton_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.rect.centerx
        self.msg_image_rect.centery = self.rect.centery

    def draw_button(self):
        self.screen.fill(self.botton_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        