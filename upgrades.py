import pygame
from settings import img_org


class Upgrades(pygame.sprite.Sprite):
    def __init__(self, screen, upgrade, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.bg = img_org["upgrade_bg_images"]  # blocked, unblocked, hover
        self.current = self.bg[0]
        self.upgrade = upgrade
        self.screen = screen
        self.x = x
        self.y = y
        self.width = int(self.upgrade.getImage().get_width() * scale)
        self.height = int(self.upgrade.getImage().get_height() * scale)
        self.image = pygame.transform.scale(self.upgrade.getImage(), (self.width, self.height))
        self.rect = self.current.get_rect()
        self.rect.center = (self.x+ int(self.current.get_width() / 2+2), self.y+ int(self.current.get_height() / 2))
        self.cost = self.upgrade.getCost()
        self.overlay = pygame.Surface((self.width, self.height))
        self.overlay.set_alpha(0)
        self.transparency = 50
        self.unlocked = False
        self.money_reached = False
        self.unlock_met = upgrade.getUnlockValue()

    def getCost(self):
        return self.upgrade.getCost()


    def effect(self):
        return self.upgrade.getEffect()

    def draw(self, count, x_inc):
        self.overlay.fill((50, 50, 50))
        if self.unlocked:
            # whether buy-able or not
            if count - self.cost >= 0:
                self.money_reached = True
            else:
                self.money_reached = False

            if not self.money_reached:
                self.current = self.bg[0]
                self.overlay.set_alpha(self.transparency)
            elif self.money_reached:
                self.current = self.bg[1]
                self.overlay.set_alpha(0)


            self.rect.center = (self.x + int(self.current.get_width() / 2 + 2)+x_inc, self.y + int(self.current.get_height() / 2))
            self.screen.blit(self.current, (self.rect.x, self.rect.y))
            self.screen.blit(self.image, (self.rect.x+5, self.rect.y+5))
            self.screen.blit(self.overlay, (self.x+5+x_inc, self.y+5))

        else:
            if self.upgrade.checkUnlock(self.unlock_met):
                self.unlocked = True
