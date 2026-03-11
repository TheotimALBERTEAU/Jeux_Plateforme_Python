import pygame


class Money(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load('assets/objects/money.jpg'), (15, 15))
        self.all_money = pygame.sprite.Group()

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = self.game.data.screen_height - 120
