from data import *


class LevelData:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen

        level_0 = {'node_pos' : (self.game.data.screen_width / 11.63, self.game.data.screen_height / 1.8), 'unlock' : 1}
        level_1 = {'node_pos' : (self.game.data.screen_width / 4.27, self.game.data.screen_height / 3.27), 'unlock' : 2}
        level_2 = {'node_pos' : (self.game.data.screen_width / 2.67, self.game.data.screen_height / 1.18), 'unlock' : 3}
        level_3 = {'node_pos' : (self.game.data.screen_width / 2.09, self.game.data.screen_height / 2.06), 'unlock' : 4}
        level_4 = {'node_pos' : (self.game.data.screen_width / 1.45, self.game.data.screen_height / 3.43), 'unlock' : 5}
        level_5 = {'node_pos' : (self.game.data.screen_width / 1.32, self.game.data.screen_height / 1.8), 'unlock' : 6}
        level_6 = {'node_pos' : (self.game.data.screen_width / 1.12, self.game.data.screen_height / 1.5), 'unlock' : 6}

        self.levels = {
            0 : level_0,
            1 : level_1,
            2 : level_2,
            3 : level_3,
            4 : level_4,
            5 : level_5,
            6 : level_6,
        }
    