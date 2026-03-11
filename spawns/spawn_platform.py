import pygame
from random import randint
from terrain.platforms import Platform
from data import *


class SpawnPlatform:
    def __init__(self, game):
        self.game = game
        self.all_platforms = pygame.sprite.Group()
        self.platforms_spawn = 0

    def spawn_platform(self):
        # ajouter une plateforme au groupe et lui donner les bonnes coordonnées
        self.platform = Platform(self)
        self.all_platforms.add(self.platform)
        self.platforms_spawn += 1

