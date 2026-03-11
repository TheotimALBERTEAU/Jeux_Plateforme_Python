from terrain.ground import Ground
import pygame


class SpawnGround:
    def __init__(self, game):
        self.game = game
    
    
    def spawn_ground(self):
        self.ground = Ground(self.game)
        self.all_ground = pygame.sprite.Group()
        self.ground.rect.x = 0
        self.all_ground.add(self.ground)
