import pygame


class Animation:
    def __init__(self, game):
        self.game = game

    def animation_basic_skin(self):
        # changement d'image pour aspect plus réaliste
        if self.game.pressed.get(pygame.K_d):
            self.game.spawnplayer.player.image = pygame.image.load('assets/animations/basic_skin/capy_walk_right_1.jpg')
            self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))
            self.game.walkcount += 1
            if self.game.walkcount >= 20:
                self.game.walkcount = 5
            if self.game.check_collision_ground(self.game.spawnplayer.player) or self.game.check_collision_platform(self.game.spawnplayer.player) or self.game.check_collision_movable_platform(self.game.spawnplayer.player):
                self.game.spawnplayer.player.image = pygame.image.load(f'assets/animations/basic_skin/capy_walk_right_{int(self.game.walkcount / 5)}.jpg')
                self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))

        elif self.game.pressed.get(pygame.K_q):
            self.game.spawnplayer.player.image = pygame.image.load('assets/animations/basic_skin/capy_walk_left_1.jpg')
            self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))
            self.game.walkcount += 1
            if self.game.walkcount >= 20:
                self.game.walkcount = 5
            if self.game.check_collision_ground(self.game.spawnplayer.player) or self.game.check_collision_platform(self.game.spawnplayer.player) or self.game.check_collision_movable_platform(self.game.spawnplayer.player):
                self.game.spawnplayer.player.image = pygame.image.load(f'assets/animations/basic_skin/capy_walk_left_{int(self.game.walkcount / 5)}.jpg')
                self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))


    def animation_batman_skin(self):
        if self.game.pressed.get(pygame.K_d):
            self.game.spawnplayer.player.image = pygame.image.load('assets/animations/batman_skin/capy_walk_right_1.jpg')
            self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))
            self.game.walkcount += 1
            if self.game.walkcount >= 20:
                self.game.walkcount = 5
            if self.game.check_collision_ground(self.game.spawnplayer.player) or self.game.check_collision_platform(self.game.spawnplayer.player) or self.game.check_collision_movable_platform(self.game.spawnplayer.player):
                self.game.spawnplayer.player.image = pygame.image.load(f'assets/animations/batman_skin/capy_walk_right_{int(self.game.walkcount / 5)}.jpg')
                self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))

        elif self.game.pressed.get(pygame.K_q):
            self.game.spawnplayer.player.image = pygame.image.load('assets/animations/batman_skin/capy_walk_left_1.jpg')
            self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))
            self.game.walkcount += 1
            if self.game.walkcount >= 20:
                self.game.walkcount = 5
            if self.game.check_collision_ground(self.game.spawnplayer.player) or self.game.check_collision_platform(self.game.spawnplayer.player) or self.game.check_collision_movable_platform(self.game.spawnplayer.player):
                self.game.spawnplayer.player.image = pygame.image.load(f'assets/animations/batman_skin/capy_walk_left_{int(self.game.walkcount / 5)}.jpg')
                self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))

    def animation_launcher_skin(self):
        if self.game.pressed.get(pygame.K_d):
            self.game.spawnplayer.player.image = pygame.image.load('assets/animations/launcher_skin/capy_walk_right_1.jpg')
            self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))
            self.game.walkcount += 1
            if self.game.walkcount >= 20:
                self.game.walkcount = 5
            if self.game.check_collision_ground(self.game.spawnplayer.player) or self.game.check_collision_platform(self.game.spawnplayer.player) or self.game.check_collision_movable_platform(self.game.spawnplayer.player):
                self.game.spawnplayer.player.image = pygame.image.load(f'assets/animations/launcher_skin/capy_walk_right_{int(self.game.walkcount / 5)}.jpg')
                self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))

        elif self.game.pressed.get(pygame.K_q):
            self.game.spawnplayer.player.image = pygame.image.load('assets/animations/launcher_skin/capy_walk_left_1.jpg')
            self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))
            self.game.walkcount += 1
            if self.game.walkcount >= 20:
                self.game.walkcount = 5
            if self.game.check_collision_ground(self.game.spawnplayer.player) or self.game.check_collision_platform(self.game.spawnplayer.player) or self.game.check_collision_movable_platform(self.game.spawnplayer.player):
                self.game.spawnplayer.player.image = pygame.image.load(f'assets/animations/launcher_skin/capy_walk_left_{int(self.game.walkcount / 5)}.jpg')
                self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))

    def animation_flash_skin(self):
        if self.game.pressed.get(pygame.K_d):
            self.game.spawnplayer.player.image = pygame.image.load('assets/animations/flash_skin/capy_walk_right_1.jpg')
            self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))
            self.game.walkcount += 1
            if self.game.walkcount >= 8:
                self.game.walkcount = 2
            if self.game.check_collision_ground(self.game.spawnplayer.player) or self.game.check_collision_platform(self.game.spawnplayer.player) or self.game.check_collision_movable_platform(self.game.spawnplayer.player):
                self.game.spawnplayer.player.image = pygame.image.load(f'assets/animations/flash_skin/capy_walk_right_{int(self.game.walkcount / 2)}.jpg')
                self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))

        elif self.game.pressed.get(pygame.K_q):
            self.game.spawnplayer.player.image = pygame.image.load('assets/animations/flash_skin/capy_walk_left_1.jpg')
            self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))
            self.game.walkcount += 1
            if self.game.walkcount >= 8:
                self.game.walkcount = 2
            if self.game.check_collision_ground(self.game.spawnplayer.player) or self.game.check_collision_platform(self.game.spawnplayer.player) or self.game.check_collision_movable_platform(self.game.spawnplayer.player):
                self.game.spawnplayer.player.image = pygame.image.load(f'assets/animations/flash_skin/capy_walk_left_{int(self.game.walkcount / 2)}.jpg')
                self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))

    def animation_super_skin(self):
        if self.game.pressed.get(pygame.K_d):
            self.game.spawnplayer.player.image = pygame.image.load('assets/animations/super_skin/capy_walk_right_1.jpg')
            self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))
            self.game.walkcount += 1
            if self.game.walkcount >= 8:
                self.game.walkcount = 2
            if self.game.check_collision_ground(self.game.spawnplayer.player) or self.game.check_collision_platform(self.game.spawnplayer.player) or self.game.check_collision_movable_platform(self.game.spawnplayer.player):
                self.game.spawnplayer.player.image = pygame.image.load(f'assets/animations/super_skin/capy_walk_right_{int(self.game.walkcount / 2)}.jpg')
                self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))

        elif self.game.pressed.get(pygame.K_q):
            self.game.spawnplayer.player.image = pygame.image.load('assets/animations/super_skin/capy_walk_left_1.jpg')
            self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))
            self.game.walkcount += 1
            if self.game.walkcount >= 8:
                self.game.walkcount = 2
            if self.game.check_collision_ground(self.game.spawnplayer.player) or self.game.check_collision_platform(self.game.spawnplayer.player) or self.game.check_collision_movable_platform(self.game.spawnplayer.player):
                self.game.spawnplayer.player.image = pygame.image.load(f'assets/animations/super_skin/capy_walk_left_{int(self.game.walkcount / 2)}.jpg')
                self.game.spawnplayer.player.image = pygame.transform.scale(self.game.spawnplayer.player.image, (80, 48))
