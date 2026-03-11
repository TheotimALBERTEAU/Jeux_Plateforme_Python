import pygame
from monsters.bob import Bob


class SpawnBob:
    def __init__(self, game):
        self.game = game
        self.all_bob = pygame.sprite.Group()
        self.nb_bob = 0
        self.bob_spawns = 0

    def spawn_bob(self):
        # ajouter un monstre2 au groupe et lui donner les bonnes coordonnées
        self.bob = Bob(self.game)
        self.all_bob.add(self.bob)
        self.nb_bob += 1
        self.bob_spawns += 1
