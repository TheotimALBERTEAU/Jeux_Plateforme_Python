import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('assets/objects/projectile.jpg')
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 45
        self.rect.y = player.rect.y + 20
        self.startx = self.rect.x

    def move(self):
        self.rect.x += self.velocity
