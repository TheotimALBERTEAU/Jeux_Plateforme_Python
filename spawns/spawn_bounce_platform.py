import pygame
from random import randint
from terrain.bounce_platform import BouncePlatform
from data import *

class SpawnBouncePlatform:
    def __init__(self, game):
        self.game = game
        self.all_bounce_platforms = pygame.sprite.Group()
        self.bounce_platforms_spawn = 0

    def spawn_bounce_platform(self):
        # ajouter une bounce_plateforme au groupe et lui donner les bonnes coordonnées
        self.bounce_platform = BouncePlatform(self)
        self.bounce_platform.rect.y = randint(int(self.game.data.screen_height / 100) - 3, int(self.game.data.screen_height / 100) - 2) * 100
        self.all_bounce_platforms.add(self.bounce_platform)
        self.bounce_platforms_spawn += 1

