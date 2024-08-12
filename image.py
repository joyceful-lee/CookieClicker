import pygame


class Image(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, image, screen):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.initial = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.screen = screen
        self.size = self.image.get_size()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.state = 0
        self.clicked = False

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def cookieUpdate(self):
        pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(pos)
        xsize = self.size[0]
        ysize = self.size[1]

        if hit:
            xsize = self.size[0] * 1.05
            ysize = self.size[1] * 1.05
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                xsize = self.size[0] * .98
                ysize = self.size[1] * .98
                self.clicked = True
            elif pygame.mouse.get_pressed()[0] == 1:
                xsize = self.size[0] * 1.05
                ysize = self.size[1] * 1.05
                self.clicked = False
        else:
            xsize = self.size[0] * 1
            ysize = self.size[1] * 1

        self.image = pygame.transform.scale(self.initial, (xsize, ysize))
        self.rect = self.image.get_rect(center=(self.x, self.y))  # necessary to scale with respect to center
