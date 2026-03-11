from levels.levelsource import LevelSource


class Level1(LevelSource):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.game.finish_flag.rect.x = 5000

        spawnpoint1x = self.levelsource.spawnpoint1x
        spawnpoint2x = self.levelsource.spawnpoint2x

        # spawns monsters
        self.cat_x_spawnpoint1 = [spawnpoint1x - 700, spawnpoint1x - 850, spawnpoint1x - 1000]
        self.cat_x_spawnpoint2 = [spawnpoint2x + 650, spawnpoint2x + 800, spawnpoint2x + 950]
        self.cat_x_startspawn = [649, 804, 932, 1159]
        self.cat_x_firstspawn = [1684, 1793]

        # spawns platforms
        self.platform_x_startspawn = [500, 940, 1400, 2300, 3000, 3650, 4250, 4700]
        self.platform_y_startspawn = [500, 300, 400, 500, 400, 500, 300, 400]

        # spawns bounceddd
        self.bounce_x_startspawn = [720, 1620, 2000, 2740, 3200, 4100, 4550]
        self.bounce_y_startspawn = [400, 500, 400, 500, 300, 400, 500]

        # 10 lignes de 5 pièces écartées de 40px puis ecart de 83px
        self.money_x = [200, 240, 280, 320, 360, 443, 483, 523, 603, 643, 726, 766, 806, 846, 886, 969, 1009, 1049, 1089, 1129, 1169, 1252, 1292, 1332, 1372, 1412, 1495, 1535, 1575, 1615, 1655, 1738, 1778, 1818, 1858, 1898, 1981, 2021, 2061, 2101, 2141, 2224, 2264, 2304, 2344, 2384, 2467, 2507, 2547, 2587, 2627, 2710, 2750, 2790, 2830, 2870, 2953, 2993, 3033, 3073, 3113, 3196, 3236, 3276, 3316, 3356, 3439, 3479, 3519, 3559, 3599, 3682, 3722, 3762, 3802, 3842, 3925, 3965, 4005, 4045, 4085, 4168, 4208, 4320, 4360, 4400, 4440, 4480, 4563, 4603, 4643, 4683, 4723, 4806, 4846, 4886, 4926, 4966]
        self.money_y = [600, 600, 600, 600, 600, 600, 600, 490, 490, 600, 400, 400, 400, 600, 600, 290, 290, 290, 600, 600, 600, 600, 600, 600, 600, 400, 400, 600, 600, 600, 500, 600, 600, 600, 600, 600, 600, 400, 400, 400, 600, 600, 600, 600, 490, 490, 600, 600, 600, 600, 600, 600, 600, 490, 490, 600, 600, 600, 400, 400, 600, 600, 290, 290, 600, 600, 600, 600, 600, 600, 600, 490, 490, 600, 600, 600, 600, 600, 600, 600, 600, 400, 600, 290, 600, 600, 600, 600, 600, 490, 490, 600, 400, 400, 600, 600, 600, 600, 600, 600]
