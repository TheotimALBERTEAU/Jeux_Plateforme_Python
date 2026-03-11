import pygame
from spawns.spawn_player import SpawnPlayer


class RemovePlayer:
    def __init__(self, game):
        self.spawnplayer = SpawnPlayer(game)

    def remove_player(self, player):
        self.spawnplayer.all_players.remove(player)
