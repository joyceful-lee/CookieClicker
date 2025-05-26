import pygame

class UpgradeItem(pygame.sprite.Sprite):
    def __init__(self, image, unlock_value, unlock_type, cost, effects ,scale):
        pygame.sprite.Sprite.__init__(self)
        self.width = int(image.get_width() * scale)  # upgrade: image, unlock condition, cost, effect
        self.height = int(image.get_height() * scale)
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.unlock_value = unlock_value
        self.unlock_type = unlock_type
        self.cost = cost
        self.effects = effects
        self.unlocked = False

    def getUnlockValue(self):
        return self.unlock_value

    def getImage(self):
        return self.image

    def getCost(self):
        return self.cost

    def checkUnlock(self, current_value):
        if self.unlock_value <= current_value:
            return True
        return False

    def getEffect(self):
        return self.effects
