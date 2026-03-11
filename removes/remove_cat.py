import pygame
from spawns.spawn_cat import SpawnCat


class RemoveCat:
    def __init__(self, game):
        self.spawncat = SpawnCat(game)
    
    def remove_cat(self, cat):
        # supprimer le monstre qui doit mourir
        self.spawncat.all_cats.remove(cat)
        self.spawncat.nb_cat -= 1
