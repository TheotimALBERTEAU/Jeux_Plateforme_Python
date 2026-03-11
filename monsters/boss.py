import pygame


class Boss(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.max_health = 10
        self.current_health = 10
        self.image = pygame.image.load('assets/monsters/boss.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = self.game.data.screen_height - 1000
        self.hitbox_right = pygame.Rect(self.rect.x + 350, self.rect.y + 5, 10, 395)
        self.hitbox_left = pygame.Rect(self.rect.x, self.rect.y + 5, 10, 395)
        self.hitbox_top = pygame.Rect(self.rect.x + 5, self.rect.y, 345, 10)
        self.hitbox_below = pygame.Rect(self.rect.x + 5, self.rect.y + 400, 345, 10)
        self.jumping = False
        self.jumpcount = 10
        self.velocity = 4
        self.iterations = 0
    
    def move(self):
        # fonction de deplacement de la plateforme -> avance de 100 puis recule de 100
        if self.iterations < 150:
            self.rect.x += self.velocity
        else:
            self.rect.x -= self.velocity
        self.iterations += 1
        if self.iterations > 300:
            self.iterations = 0

    def update_health_bar(self, screen):
        bar_pos = [self.rect.x, self.rect.y - 20, self.current_health * 35, 5]
        max_bar_pos = [self.rect.x, self.rect.y - 20, self.max_health * 35, 5]

        pygame.draw.rect(screen, (60, 63, 60), max_bar_pos)
        pygame.draw.rect(screen, 'green', bar_pos)

    def jump(self):
        # change valeur de jumping pour pouvoir jump
        self.jumping = True

    def update_y(self):
        # fonction de jump (meme que le joueur)
        if self.jumpcount >= 0 and self.jumping:
            self.rect.y -= (self.jumpcount * abs(self.jumpcount)) * 0.5
            self.jumpcount -= 1
        else:
            self.jumpcount = 10
            self.jumping = False

        # variables collisions
        check_collision = self.game.check_collision_ground(self) or self.game.check_collision_platform(self) or self.game.check_collision_movable_platform(self) or self.game.check_collision_bounce_platform(self)

        # descente 
        self.rect.y += (not check_collision) * 10 - 0
