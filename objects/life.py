import pygame

class Life(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.start_life = 5
        self.current_life = self.start_life - self.game.lost_life
        self.max_life = 5
        self.image = pygame.image.load('assets/objects/life.jpg')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.x = 65
        self.all_lifes = pygame.sprite.Group()

    def draw(self):
        self.life = Life(self.game)
        self.all_lifes.add(self.life)
        self.life.rect.x = self.x
        self.x += 30
