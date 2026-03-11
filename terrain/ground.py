import pygame
from data import *


class Ground(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load('assets/platforms/ground.jpg')
        self.image = pygame.transform.scale(self.image, (10000, 90))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = game.data.screen_height - 90
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y + 10, 6000, 180)
