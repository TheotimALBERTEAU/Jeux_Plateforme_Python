import pygame
from players.player import Player


class SpawnPlayer:
    def __init__(self, game):
        self.game = game
        self.all_players = pygame.sprite.Group()

    def spawn_player(self):
        # ajouter un player au groupe de tous les joueurs
        self.player = Player(self.game)
        self.all_players.add(self.player)
