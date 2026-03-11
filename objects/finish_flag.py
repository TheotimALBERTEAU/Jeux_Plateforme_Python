import pygame
from data import *


class FinishFlag(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.image = pygame.image.load('assets/objects/finish_flag.jpg')
        self.image = pygame.transform.scale(self.image, (135, 267))
        self.rect = self.image.get_rect()
        self.rect.x = 5000
        self.rect.y = game.data.screen_height - 353
        self.hitbox = pygame.Rect(self.rect.x + 60, self.rect.y, 10, 267)
