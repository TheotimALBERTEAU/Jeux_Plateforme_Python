import pygame


class Score:

    def __init__(self, game):
        self.start_score = 0
        self.current_score = 0

        self.font = pygame.font.Font(None, 30)
        self.surface = self.font.render(f'score : {self.current_score}', True, (255, 107, 0))
        self.rect = self.surface.get_rect()
        self.rect.x = game.data.screen_width - 125

    def add_score_cat(self):
        self.current_score += 50
    
    def add_score_bob(self):
        self.current_score += 75

    def add_score_boss(self):
        self.current_score += 500
