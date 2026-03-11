import pygame
from spawns.spawn_movable_platform import SpawnMovablePlatform


class RemoveMovablePlatform:
    def __init__(self, game):
        self.spawnmovableplatform = SpawnMovablePlatform(game)

    def remove_movable_platform(self, movable_platform):
        self.spawnmovableplatform.all_movable_platforms.remove(movable_platform)
