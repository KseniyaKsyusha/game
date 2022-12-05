import pygame
import time


class Rectangle():
    '''класс прямоугольник'''

    def __init__(self, x=0, y=0, width=10, height=10, color=None, mw=pygame.display.set_mode((600, 600))):
        self.rect = pygame.Rect(x, y, width, height)  # прямоугольник
        self.fill_color = color
        self.mw = mw

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(self.mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):  # обводка существующего прямоугольника
        pygame.draw.rect(self.mw, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
