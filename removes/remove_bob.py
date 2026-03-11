import pygame
from spawns.spawn_bob import SpawnBob

class RemoveBob:
    def __init__(self, game):
        self.spawnbob = SpawnBob(game)
        
    def remove_bob(self, bob):
        # supprimer le monstre qui doit mourir
        self.spawnbob.all_bob.remove(bob)
        self.spawnbob.nb_bob -= 1
