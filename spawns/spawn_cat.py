import pygame
from monsters.cat import Cat


class SpawnCat:
    def __init__(self, game):
        self.game = game
        self.all_cats = pygame.sprite.Group()
        self.nb_cat = 0
        self.cat_spawn = 0
    
    def spawn_cat(self):
        # ajouter un monstre1 au groupe et lui donner les bonnes coordonnées
        self.cat = Cat(self.game)
        self.all_cats.add(self.cat)
        self.nb_cat += 1
        self.cat_spawn += 1

        