import pygame
from pygame.math import Vector2


def rotate_on_pivot(image, angle, pivot, origin):
    surf = pygame.transform.rotate(image, angle)

    offset = pivot + (origin - pivot).rotate(-angle)
    rect = surf.get_rect(center=offset)

    return surf, rect
class Cursor(pygame.sprite.Sprite):
    radius = 65
    def __init__(self, pivot, starting_angle, image, scale):
        self.pivot = pivot
        self.angle = 0

        offset = Vector2()
        offset.from_polar((self.radius, -starting_angle))

        self.pos = pivot + offset

        self.image_orig = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.image = self.image_orig
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, dt):
        self.angle += 30 * dt

        self.image, self.rect = rotate_on_pivot(self.image_orig, self.angle, self.pivot, self.pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
