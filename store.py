import pygame
import math
from settings import settings

magnitude = ['', ' Thousand', ' Million', ' Billion', ' Trillion']


def number_exchange(count, num):
    count = float(count)
    idx = max(0, min(len(magnitude) - 1,
                     int(math.floor(0 if count == 0 else math.log10(abs(count)) / 3))))
    if count < 1000:
        return '{:.0f}{}'.format(count / 10 ** (3 * idx), magnitude[idx])
    elif num == 3:
        return '{:.3f}{}'.format(count / 10 ** (3 * idx), magnitude[idx])
    elif num == 2:
        return '{:.2f}{}'.format(count / 10 ** (3 * idx), magnitude[idx])
    elif num == 1:
        return '{:.1f}{}'.format(count / 10 ** (3 * idx), magnitude[idx])
    else:
        return '{:.0f}{}'.format(count / 10 ** (3 * idx), magnitude[idx])


class Store(pygame.sprite.Sprite):
    def __init__(self, screen, images, prices, multiplier, seen, scale, font, x, y):
        pygame.sprite.Sprite.__init__(self)

        # colors
        self.green = (0, 200, 0)
        self.red = (174, 0, 0)
        self.screen = screen

        # font
        font_name = pygame.font.match_font(font)
        self.font_size = 14
        self.font = pygame.font.Font(font_name, self.font_size)
        self.price_text = self.font.render("", True, self.red)

        # location / dimensions
        self.x = x
        self.y = y
        self.width = int(images[0].get_width() * scale)
        self.height = int(images[0].get_height() * scale)

        # sprites
        self.blocked = pygame.transform.scale(images[0], (self.width, self.height))
        self.greyed = pygame.transform.scale(images[2], (self.width, self.height))
        self.unblocked = pygame.transform.scale(images[1], (self.width, self.height))
        self.overlay = pygame.Surface((self.width, self.height))
        self.rect = self.blocked.get_rect()
        self.rect.topleft = (self.x, self.y)

        # price values
        self.price_current = prices[0]
        self.increase_per = prices[1]
        self.multiplier = multiplier

        # other
        self.overlay.set_alpha(0)
        self.transparency = 35
        self.money_reached = False
        self.unlocked = False
        self.seen = seen

    def draw(self, cost, count, seen_point, total_cookies):
        pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(pos)
        if self.seen:
            # hover effect
            if hit:
                self.overlay.set_alpha(self.transparency)
                self.overlay.fill((50, 50, 50), special_flags=pygame.BLEND_RGB_ADD)
            else:
                self.overlay.set_alpha(0)
                self.overlay.fill((50, 50, 50), special_flags=pygame.BLEND_RGB_SUB)

            # whether buy-able or not
            if count - cost >= 0:
                self.money_reached = True
            else:
                self.money_reached = False

            # unlocks
            if count >= cost / 2:
                self.unlocked = True

            color = self.red
            # blit different images/text (blocked/red, greyed/red, unblocked/green)
            if not self.unlocked:
                self.screen.blit(self.blocked, (self.rect.x, self.rect.y))
            elif not self.money_reached:
                self.screen.blit(self.greyed, (self.rect.x, self.rect.y))
            else:
                self.screen.blit(self.unblocked, (self.rect.x, self.rect.y))
                color = self.green

            sig = 0
            if cost > 1000 and cost < 10000:
                sig = 1
            self.price_text = self.font.render(number_exchange(cost, sig), True, color)
            price_rect = self.price_text.get_rect()
            price_rect.topleft = (self.x + 60, self.y + 22)
            self.screen.blit(self.price_text, price_rect)
            self.screen.blit(self.overlay, (self.rect.x, self.rect.y))
        else:
            if total_cookies > seen_point:
                self.seen = True
