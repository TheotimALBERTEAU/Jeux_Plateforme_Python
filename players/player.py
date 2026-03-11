import pygame
from objects.projectile import Projectile
from objects.life import Life
from objects.score import Score
from objects.money import Money
from objects.skins_data import *


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.score = Score(game)
        self.life = Life(game)
        self.moneyimage = Money(game)
        self.current_life = self.life.current_life
        self.image = pygame.image.load(skins[self.game.character]['skin'])
        self.image = pygame.transform.scale(self.image, (80, 48))
        self.attack = 1
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = self.game.data.screen_height - 200
        self.velocity = 7
        self.jumping = False
        self.jumpcount = 12
        # initialise les differentes hitbox
        self.hitbox_right = pygame.Rect(0, 0, 0, 0)
        self.hitbox_left = pygame.Rect(0, 0, 0, 0)
        self.hitbox_top = pygame.Rect(0, 0, 0, 0)
        self.hitbox_below = pygame.Rect(0, 0, 0, 0)
        self.v_decent = 14
        self.orientation = 'right'

        self.all_projectiles = pygame.sprite.Group()
        self.is_launching = False
        
        self.font = pygame.font.Font(None, 40)
        self.money_surface = self.font.render(f'money : {self.game.money}', True, (255, 107, 0))
        self.money_rect = self.money_surface.get_rect(center = (self.game.data.screen_width / 2, 20))

        for i in range(self.current_life):
            self.life.draw()

    def move_right(self):
        # deplacement de joueur vers la droite
        if self.game.character == 4 or self.game.character == 5:
            self.rect.x += self.velocity * 2
        elif self.game.character == 1:
            self.rect.x += self.velocity / 3
        else:
            self.rect.x += self.velocity

    def move_left(self):
        # deplacement du joueur vers la gauche
        if self.game.character == 4 or self.game.character == 5:
            self.rect.x -= self.velocity * 2
        elif self.game.character == 1:
            self.rect.x -= self.velocity / 7
        else:
            self.rect.x -= self.velocity

    def launch_projectile(self):
        self.projectile = Projectile(self)
        self.all_projectiles.add(self.projectile)

    def jump(self):
        # affecte valeur True pour pouvoir jump
        if not self.game.character == 1:
            self.jumping = True

    def reload_money(self):
        self.money_surface = self.font.render(f'money : {self.money}', True, (255, 107, 0))
        self.money_rect = self.money_surface.get_rect(center = (self.game.data.screen_width / 2, 25))

    def update(self):
        if self.game.money == 100:
            self.game.money = 0
            self.current_life += 1
            self.game.lost_life -= 1
            self.life.draw()
        
        # variable de toutes les collisions
        check_collision = self.game.check_collision_ground(self) or self.game.check_collision_platform(
            self) or self.game.check_collision_movable_platform(self)

        # boucle pour acceder a tous les monstres1
        for cat in self.game.spawncat.all_cats:
            
            # verif collisions: si oui alors tuer le monstre et jump
            if self.game.check_collision_jump(cat):
                self.game.removecat(cat)
                self.score.add_score_cat()
                self.jump()
        
            # si haut du joueur touche bas du monstre alors 1 vie en moins
            elif self.game.check_collision_top(cat):
                self.game.life_lost()
        
        # boucle pour acceder à tous les monstres2
        for bob in self.game.spawnbob.all_bob:
        
            # verif collisions: si oui alors tuer le monstre et jump
            if self.game.check_collision_jump(bob):
                self.game.removebob(bob)
                self.score.add_score_bob()
                self.jump()
            
            # si haut du joueur touche bas du monstre alors 1 vie en moins
            elif self.game.check_collision_top(bob):
                self.game.life_lost()

        for boss in self.game.actual_level.removeboss.spawnboss.all_boss:

            if self.game.check_collision_jump(boss):
                self.game.actual_level.removeboss.spawnboss.boss.current_health -= 1
                self.jump()

            elif self.game.check_collision_top(boss):
                self.game.life_lost()

        
        # fonction pour le saut (reduit la vitesse de 72 jusqu'a 0 puis ne fais plus rien)
        if self.jumpcount >= 0 and self.jumping:
            self.rect.y -= self.jumpcount ** 2 / 2
            self.jumpcount -= 1
        # remet les valeurs de bases
        else:
            self.jumpcount = 12
            self.jumping = False

        # modification de la vitesse de descente en fonction d'une touche appuyé ou non
        if self.game.pressed.get(pygame.K_z) and (self.game.character == 2 or self.game.character == 5):
            self.v_decent = 2
        elif self.game.pressed.get(pygame.K_s):
            self.v_decent = 34
        else:
            self.v_decent = 17
        
        # variation du y du joueur jusqu'a une collision
        self.rect.y += (not check_collision) * self.v_decent

        # deplacement du joueur lorsqu'il est sur une movable platform
        if self.game.check_collision_movable_platform(self):
            if self.game.spawnmovableplatform.movable_platform.iterations < 100:
                self.rect.x += self.game.spawnmovableplatform.movable_platform.velocity
            else:
                self.rect.x -= self.game.spawnmovableplatform.movable_platform.velocity

        for money in self.moneyimage.all_money:
            if self.game.check_collision_money(money, self.game.spawnplayer.all_players):
                self.game.money += 1
                self.moneyimage.all_money.remove(money)
