import pygame
import random


class MovablePlatform(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.image = pygame.image.load('assets/platforms/movable_platform.jpg')
        self.image = pygame.transform.scale(self.image, (125, 66))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.x = [900, 1445, 2670, 3130, 4325]
        self.y = [285, 397, 385, 416, 272]
        self.velocity = 2
        self.iterations = 0
        self.hitbox = pygame.Rect(self.rect.x + 10, self.rect.y + 30, 105, 5)

    def move(self):
        # fonction de deplacement de la plateforme -> avance de 100 puis recule de 100
        if self.iterations < 100:
            self.rect.x += self.velocity
        else:
            self.rect.x -= self.velocity
        self.iterations += 1
        if self.iterations > 200:
            self.iterations = 0
