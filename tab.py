import pygame


class Tab(pygame.sprite.Sprite):
    def __init__(self, screen, images, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        width = int(images[0].get_width() * scale)
        height = int(images[0].get_height() * scale)
        self.greyed = pygame.transform.scale(images[0], (width, height))
        self.hover = pygame.transform.scale(images[1], (width, height))
        self.size = self.greyed.get_size()
        self.rect = self.greyed.get_rect(bottomleft=(self.x, self.y))

    def draw(self):
        pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(pos)

        if hit:
            self.screen.blit(self.hover, (self.rect.x, self.rect.y))
        else:
            self.screen.blit(self.greyed, (self.rect.x, self.rect.y))
