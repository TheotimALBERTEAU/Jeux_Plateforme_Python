import pygame
from spawns.spawn_boss import SpawnBoss


class RemoveBoss:
    def __init__(self, game):
        self.spawnboss = SpawnBoss(game)

    def remove_boss(self, boss):
        self.spawnboss.all_boss.remove(boss)
