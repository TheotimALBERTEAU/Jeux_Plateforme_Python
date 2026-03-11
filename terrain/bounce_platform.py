import pygame
import random


class BouncePlatform(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load('assets/platforms/bounce_platform2.jpg')
        self.image = pygame.transform.scale(self.image, (125, 66))
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 550
        self.y = [546, 504, 529, 591, 420, 600, 484]
        self.hitbox = pygame.Rect(self.rect.x + 10, self.rect.y + 30, 105, 5)