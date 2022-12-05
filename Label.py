import pygame

from Rectangle import Rectangle


class Label(Rectangle):

    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        self.mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
