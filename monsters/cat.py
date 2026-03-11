import pygame
from data import *


class Cat(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.max_health = 1
        self.health = 1
        self.image = pygame.image.load('assets/monsters/cat.jpg')
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.rect = self.image.get_rect()
        self.rect.y = self.game.data.screen_height - 200
        self.velocity = 2
        self.hitbox_right = pygame.Rect(0, 0, 0, 0)
        self.hitbox_left = pygame.Rect(0, 0, 0, 0)
        self.hitbox_top = pygame.Rect(0, 0, 0, 0)
        self.hitbox_below = pygame.Rect(0, 0, 0, 0)
        self.jumping = False
        self.jumpcount = 10


    def forward(self, game):

        # verif si pas de collisions -> peut avancer
        if not game.check_collision_right():
            self.rect.x -= self.velocity

    def jump(self):
        # change valeur de jumping pour pouvoir jump
        self.jumping = True

    def update_y(self, game):
        # fonction de jump (meme que le joueur)
        if self.jumpcount >= 0 and self.jumping:
            self.rect.y -= (self.jumpcount * abs(self.jumpcount)) * 0.5
            self.jumpcount -= 1
        else:
            self.jumpcount = 10
            self.jumping = False

        # variables collisions
        check_collision = game.check_collision_ground(self) or game.check_collision_platform(self) or game.check_collision_movable_platform(self) or game.check_collision_bounce_platform(self)

        # descente 
        self.rect.y += (not check_collision) * 10 - 0
