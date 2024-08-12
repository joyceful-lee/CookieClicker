import pygame

import store
from store import Store


class Text:
    def __init__(self, surface, font, size, color, x, y):

        font_name = pygame.font.match_font(font)
        self.surface = surface
        self.size = size
        self.font = pygame.font.Font(font_name, self.size)
        self.color = color
        self.x = x
        self.y = y

    def draw_text(self, text):
        text_surface = self.font.render(text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.surface.blit(text_surface, text_rect)

    def draw_stats(self, count, totalCount, auto):
        text = "Cookies in bank: " + store.number_exchange(count, 3)
        text_surface = self.font.render(text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.x+10, self.y+10)
        self.surface.blit(text_surface, text_rect)
        text = "Cookies baked (all time): " + store.number_exchange(totalCount, 3)
        text_surface = self.font.render(text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.x+10, self.y+30)
        self.surface.blit(text_surface, text_rect)
        text = "Cookies per second: " + store.number_exchange(auto, 3)
        text_surface = self.font.render(text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.x+10, self.y+50)
        self.surface.blit(text_surface, text_rect)
