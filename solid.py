import pygame
from settings import settings


# use for GUI decoration

# transparency = 0 (transparent) - 255 (opaque)
class Solid(pygame.sprite.Sprite):
    def __init__(self, screen, color, transparency, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.Surface((width, height))
        self.image.set_alpha(transparency)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def scroll(self, startpos):
        pos = pygame.mouse.get_pos()
        settings['scroll_y'] = startpos[1] - pos[1]
        y_offset = settings["scroll_y"]
        self.screen.blit(self.image, (self.rect.x, self.rect.y+y_offset))

    def drawS(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y+settings['scroll_y']))
