import pygame


class Icon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = pygame.Surface((20, 20))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)
    
    def update(self):
        self.rect.center = self.pos
