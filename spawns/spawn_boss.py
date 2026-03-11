import pygame
from monsters.boss import Boss


class SpawnBoss:
    def __init__(self, game):
        self.game = game
        self.all_boss = pygame.sprite.Group()
        
    def spawn_boss(self):
        self.boss = Boss(self.game)
        self.all_boss.add(self.boss)
