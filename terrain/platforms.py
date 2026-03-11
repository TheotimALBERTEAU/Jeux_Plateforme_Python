import pygame
import random


class Platform(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load('assets/platforms/platform.jpg')
        self.image = pygame.transform.scale(self.image, (125, 66))
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 0
        self.y = [594, 504, 568, 424, 537, 322, 409, 250, 449, 581, 369, 546, 310, 213, 521]
        self.hitbox = pygame.Rect(self.rect.x + 10, self.rect.y + 30, 105, 5)
