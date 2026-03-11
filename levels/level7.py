from levels.levelsource import LevelSource


class Level7(LevelSource):
    def __init__(self, game):
        super().__init__(game)
        self.game = game

        # spawns monsters
        self.cat_x_spawnpoint1 = []
        self.cat_x_spawnpoint2 = []
        self.cat_x_startspawn = []
        self.cat_x_firstspawn = []
        
        self.bob_x_spawnpoint1 = []
        self.bob_x_spawnpoint2 = []
        self.bob_x_startspawn = []
        self.bob_x_firstspawn = []
        
        # spawns platforms
        self.platform_x_startspawn = [200, 475]
        self.platform_y_startspawn = [520, 320]
        
        # spawns bounce
        self.bounce_x_startspawn = [50, 310]
        self.bounce_y_startspawn = [450, 400]
        
        # spawns movable
        self.movable_x_startspawn = []
        self.movable_y_startspawn = []

        self.money_x = []
        self.money_y = []
