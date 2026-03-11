import pygame
from spawns.spawn_platform import SpawnPlatform


class RemovePlatform:
    def __init__(self, game):
        self.spawnplatform = SpawnPlatform(game)

    def remove_platform(self, platform):
        self.spawnplatform.all_platforms.remove(platform)
