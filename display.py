import random

import pygame


class Display(pygame.sprite.Sprite):
    def __init__(self, screen, image, divider, scale, x, y, index, isGrannie):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.width = int(image[1].get_width() * scale)
        self.height = int(image[1].get_height() * scale)
        self.bg = image[0]
        self.icon = pygame.transform.scale(image[1], (self.width, self.height))
        self.divider = divider
        self.rect = self.bg.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.unlocked = False
        self.count = 0
        self.index = index
        self.isGrannie = isGrannie
        self.list = []

    def three_row(self):
        x_increase = 0
        for i in range(self.count):
            if i % 3 == 0:
                self.screen.blit(self.list[i], (self.rect.x + x_increase, self.rect.y))
            x_increase += 5
            if self.rect.x + x_increase >= 570:
                break

        x_increase = 0
        for i in range(self.count):
            if i % 3 == 1:
                self.screen.blit(self.list[i], (self.rect.x + x_increase, self.rect.y + 5))
            x_increase += 5
            if self.rect.x + x_increase >= 570:
                break
        x_increase = 0
        for i in range(self.count):
            if i % 3 == 2:
                self.screen.blit(self.list[i], (self.rect.x + x_increase, self.rect.y + 10))
            x_increase += 5
            if self.rect.x + x_increase >= 570:
                break

    def two_row(self):
        x_increase = 5
        for i in range(self.count):
            if i % 2 == 0:
                self.screen.blit(self.icon, (self.rect.x + x_increase, self.rect.y+3))
            elif i % 2 == 1:
                self.screen.blit(self.icon, (self.rect.x + x_increase, self.rect.y+13))
            x_increase += 15
            if self.rect.x + x_increase >= 570:
                break

    def one_row(self):
        x_increase = 5
        for i in range(self.count):
            self.screen.blit(self.icon, (self.rect.x + x_increase, self.rect.y+3))
            x_increase += 30
            if self.rect.x + x_increase >= 570:
                break

    def draw(self, count, rows):
        self.count = count
        if self.unlocked:
            self.screen.blit(self.bg, (self.rect.x, self.rect.y))
            self.screen.blit(self.divider, (self.rect.x, self.rect.y + 55))

        if rows == 3:
            self.three_row()
        elif rows == 2:
            self.two_row()
        else:
            self.one_row()


    def unlock(self):
        self.unlocked = True
        return self.index

    def addToGrannie(self, index):
        num = random.randint(1, index)
        self.list.append(pygame.transform.scale(self.image[num], (self.width, self.height)))

