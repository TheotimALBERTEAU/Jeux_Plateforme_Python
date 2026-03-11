import pygame
from data import *


class HomeScreen:

    def __init__(self, game):
        self.game = game
        self.start_button = pygame.image.load('./assets/buttons/start_button.jpg')
        self.start_button = pygame.transform.scale(self.start_button, (400, 150))
        self.start_button_rect = self.start_button.get_rect()
        self.start_button_rect.x = self.game.data.screen_width / 2 - 200
        self.start_button_rect.y = self.game.data.screen_height / 2 - 75
        self.start_button_hitbox = pygame.Rect(self.start_button_rect.x, self.start_button_rect.y, 400, 150)

        self.skins_button = pygame.image.load('./assets/buttons/skins_button.jpg')
        self.skins_button = pygame.transform.scale(self.skins_button, (100, 100))
        self.skins_button_rect = self.skins_button.get_rect()
        self.skins_button_rect.x = self.start_button_rect.x + 425
        self.skins_button_rect.y = self.game.data.screen_height / 2 - 50
        self.skins_button_hitbox = pygame.Rect(self.skins_button_rect.x, self.skins_button_rect.y, 100, 100)

    def reload(self):
        self.start_button_rect.x = self.game.data.screen_width / 2 - 200
        self.start_button_rect.y = self.game.data.screen_height / 2 - 75
        self.start_button_hitbox = pygame.Rect(self.start_button_rect.x, self.start_button_rect.y, 400, 150)
        self.skins_button_rect.x = self.start_button_rect.x + 425
        self.skins_button_rect.y = self.game.data.screen_height / 2 - 50
        self.skins_button_hitbox = pygame.Rect(self.skins_button_rect.x, self.skins_button_rect.y, 100, 100)
    
    def home_screen(self, screen):
        # met en ordre et affiche elements de l'ecran d'accueil
        bg_home = pygame.image.load('./assets/backgrounds/background_home.jpg')
        bg_home = pygame.transform.scale(bg_home, (self.game.data.screen_width, self.game.data.screen_height))
        logo = pygame.image.load('./assets/objects/logo3.jpg')
        logo_rect = logo.get_rect()
        logo_rect.x = self.game.data.screen_width / 2 - 280
        logo_rect.y = 70

        screen.blit(bg_home, (0, 0))
        screen.blit(logo, (logo_rect))
        screen.blit(self.start_button, self.start_button_rect)
        screen.blit(self.skins_button, self.skins_button_rect)
