import pygame
from random import randint
from terrain.movable_platform import MovablePlatform


class SpawnMovablePlatform:
    def __init__(self, game):
        self.game = game
        self.all_movable_platforms = pygame.sprite.Group()
        self.movable_platforms_spawn = 0
    
    def spawn_movable_platform(self):
        # ajouter une movable_plateforme au groupe et lui donner les bonnes coordonnées
        self.movable_platform = MovablePlatform(self)
        self.movable_platform.rect.y = randint(int(self.game.data.screen_height / 100) - 3, int(self.game.data.screen_height / 100) - 2) * 100
        self.all_movable_platforms.add(self.movable_platform)
        self.movable_platforms_spawn += 1

