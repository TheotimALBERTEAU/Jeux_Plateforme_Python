import pygame
from overworld.level_data import LevelData

class Levels:
    def __init__(self, game, levelsource, current_level, screen, create_overworld):
        self.create_overworld = create_overworld
        self.leveldata = LevelData(game, screen)
        self.game = game
        self.level_source = levelsource
        # level setup
        self.screen = screen
        self.current_level = current_level
        self.level_data = self.leveldata.levels[self.current_level]
    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.game.nb_screen = 4
        elif keys[pygame.K_RETURN]:
            self.game.create_overworld(self.current_level, self.level_data['unlock'], self.screen)
            self.game.nb_screen = 4
    
    def run(self, screen):
        self.level_source.run(screen)
