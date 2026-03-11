import pygame
from data import *


class Node(pygame.sprite.Sprite):
    def __init__(self, pos, status, icon_speed, game):
        super().__init__()

        self.image = pygame.Surface((game.data.screen_width / 12.8 , game.data.screen_height / 16))
        
        if status == 'available':
            self.image.fill('red')
        else:
            self.image.fill('grey')
        self.rect = self.image.get_rect(center = pos)
        
        self.detection_zone = pygame.Rect(self.rect.centerx - (icon_speed / 2), self.rect.centery - (icon_speed / 2), icon_speed, icon_speed)
        