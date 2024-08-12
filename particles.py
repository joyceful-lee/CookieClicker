import pygame
import random


class Particle(pygame.sprite.Sprite):
    def __init__(self, groups, pos, image, scale, color, direction, speed):
        super().__init__(groups)
        self.rect = None
        self.image = None
        self.pos = pos
        self.color = color
        self.direction = direction
        self.speed = speed
        self.width = int(image.get_width() * scale)
        self.height = int(image.get_height() * scale)
        self.alpha = 255
        self.fade_speed = 450

        self.create_image(image)

    def create_image(self, image):
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.image.get_rect(center=self.pos)

    def move(self, dt):
        self.direction += pygame.math.Vector2(0, random.uniform(.01, 0))
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def fade(self, dt, rain):
        if rain:
            self.fade_speed = 150
        self.alpha -= self.fade_speed * dt
        self.image.set_alpha(self.alpha)

    def check_pos(self, screen_width, screen_height):
        if (self.pos[0] < -50 or self.pos[0] > screen_width + 50 or
                self.pos[1] < -50 or self.pos[1] > screen_height + 50):
            self.kill()

    def update(self, dt, screen_width, screen_height, rain):
        if rain:
            self.direction += (0, 1)
            self.pos += self.direction * self.speed * dt
            self.rect.center = self.pos
        else:
            self.move(dt)
        self.fade(dt, rain)
        self.check_pos(screen_width, screen_height)


