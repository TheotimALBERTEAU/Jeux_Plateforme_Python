import pygame
import random


class Bob(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.max_health = 1
        self.health = 1
        self.attack = 1
        self.image = pygame.image.load('assets/monsters/bob.jpg')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.velocity = 1
        self.hitbox_right = pygame.Rect(0, 0, 0, 0)
        self.hitbox_left = pygame.Rect(0, 0, 0, 0)
        self.hitbox_top = pygame.Rect(0, 0, 0, 0)
        self.hitbox_below = pygame.Rect(0, 0, 0, 0)
        self.flying = False
        self.flycount = 7

    def forward(self, game):
        
        # verif si pas de collisions -> peut avancer
        if not game.check_collision_right():
            self.rect.x -= self.velocity

    def fly(self):
        
        # fonction pour "voler"
        # verif si il peut voler
        if self.flycount >= 0 and self.flying:
            self.rect.y -= (self.flycount * abs(self.flycount)) * 0.5
            self.flycount -= 1
        # sinon -> arrete de "voler" et monter
        else:
            self.flycount = 7
            if self.rect.y <= 100:
                self.flying = False

    def update_y(self, game):
        
        # variable pour toutes les collisions
        check_collision = game.check_collision_ground(self) or game.check_collision_platform(self) or game.check_collision_movable_platform(self) or game.check_collision_bounce_platform(self)
        
        # si il ne vole pas => redescendre
        if not self.flying:
            self.rect.y += (not check_collision) * 2
