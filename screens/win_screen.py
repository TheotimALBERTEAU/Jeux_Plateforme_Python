import pygame


class WinScreen:
    def __init__(self, screen, game):
        self.game = game
        self.restart_button = pygame.image.load('./assets/buttons/restart_button.jpg')
        self.restart_button = pygame.transform.scale(self.restart_button, (400, 150))
        self.restart_button_rect = self.restart_button.get_rect()
        self.restart_button_rect.x = self.game.data.screen_width / 2
        self.restart_button_rect.y = self.game.data.screen_height / 3 + 50
        self.restart_button_hitbox = pygame.Rect(self.restart_button_rect.x, self.restart_button_rect.y, 400, 150)
        self.menu_button = pygame.image.load('./assets/buttons/levels_menu.jpg')
        self.menu_button = pygame.transform.scale(self.menu_button, (400, 150))
        self.menu_button_rect = self.menu_button.get_rect()
        self.menu_button_rect.x = self.game.data.screen_width / 2
        self.menu_button_rect.y = self.restart_button_rect.y + 200
        self.menu_button_hitbox = pygame.Rect(self.menu_button_rect.x, self.menu_button_rect.y, 400, 150)

    def reload(self):
        self.restart_button_rect.x = self.game.data.screen_width / 2
        self.restart_button_rect.y = self.game.data.screen_height / 3
        self.restart_button_hitbox = pygame.Rect(self.restart_button_rect.x, self.restart_button_rect.y, 400, 150)
        self.menu_button_rect.x = self.game.data.screen_width / 2
        self.menu_button_rect.y = self.restart_button_rect.y + 200
        self.menu_button_hitbox = pygame.Rect(self.menu_button_rect.x, self.menu_button_rect.y, 400, 150)

    def win_screen(self, screen):
        # met en ordre et affiche elements de l'ecran de victoire
        bg_win = pygame.image.load('assets/backgrounds/background_win.jpg')
        bg_win = pygame.transform.scale(bg_win, (self.game.data.screen_width, self.game.data.screen_height))

        screen.blit(bg_win, (0, 0))
        screen.blit(self.restart_button, self.restart_button_rect)
        screen.blit(self.menu_button, self.menu_button_rect)
