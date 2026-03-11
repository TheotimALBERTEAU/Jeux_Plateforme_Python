import pygame


class Data:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720

        self.warning_font = pygame.font.Font(None, 40)
        self.warning_text = 'ATTENTION : changer votre resolution recommencera votre partie en cours !'
        self.choice = 'Voulez-vous quand même continuer ?'
        self.warning_surface = self.warning_font.render(self.warning_text, True, (255, 107, 0))
        self.choice_surface = self.warning_font.render(self.choice, True, (255, 107, 0))
        self.warning_rect = self.warning_surface.get_rect(center = (self.screen_width / 2, self.screen_height / 2 - 25))
        self.choice_rect = self.choice_surface.get_rect(center = (self.screen_width / 2, self.screen_height / 2 + 25))