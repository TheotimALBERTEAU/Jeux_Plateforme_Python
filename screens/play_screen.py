import pygame
from data import *


class PlayScreen:

    def __init__(self, game):
        self.game = game
        self.pause_button = pygame.image.load('./assets/buttons/pause_button.jpg')
        self.pause_button_rect = self.pause_button.get_rect()
        self.pause_button_rect.x = 0
        self.pause_button_hitbox = pygame.Rect(self.pause_button_rect.x, self.pause_button_rect.y, 50, 50)

    def play_screen(self, screen):
        # met en ordre et affiche elements de l'ecran de jeu
        bg_game = pygame.image.load('assets/backgrounds/background_game.jpg')
        bg_game = pygame.transform.scale(bg_game, (self.game.data.screen_width, self.game.data.screen_height))
        self.pause_button = pygame.transform.scale(self.pause_button, (50, 50))

        screen.blit(bg_game, (0, 0))
        screen.blit(self.pause_button, self.pause_button_rect)
