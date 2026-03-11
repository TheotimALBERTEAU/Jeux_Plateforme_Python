from objects.finish_flag import FinishFlag
from screens.overworld_screen import OverworldScreen
from overworld.level import Levels
from levels.level1 import Level1
from levels.level2 import Level2
from levels.level3 import Level3
from levels.level4 import Level4
from levels.level5 import Level5
from levels.level6 import Level6
from levels.level7 import Level7
from data import Data
from objects.skins_data import *
from objects.animation import Animation
import random
import pygame


class Game:

    def __init__(self, screen):
        self.data = Data()
        self.screen = screen
        self.finish_flag = FinishFlag(self)
        self.animation = Animation(self)
        self.is_choice_make = False
        self.pressed = {}
        self.walkcount = 5
        self.nb_screen = 1
        self.is_bg_moving = False
        self.cursor = pygame.image.load('assets/interface/cursor.jpg')
        self.cursor = pygame.transform.scale(self.cursor, (30, 30))
        self.current_skin = 0
        self.character = 0
        self.velocity_move = 7

        # setup overworld
        self.max_level = 0
        self.start_level = 0
        
        # setup levels
        self.level1 = Level1(self)
        self.level2 = Level2(self)
        self.level3 = Level3(self)
        self.level4 = Level4(self)
        self.level5 = Level5(self)
        self.level6 = Level6(self)
        self.level7 = Level7(self)
        self.actual_level = self.level1

        self.lost_life = 0
        self.money = 98

        self.create_level(self.start_level)
        self.create_overworld(self.level.current_level, self.max_level, screen)


    def play(self, screen):
        
        if self.character == 4 or self.character == 5:
            self.velocity_move = 14
        else:
            self.velocity_move = 7
        
        animations = [self.animation.animation_basic_skin, self.animation.animation_rainbow_skin, self.animation.animation_batman_skin, self.animation.animation_launcher_skin, self.animation.animation_flash_skin, self.animation.animation_super_skin]
        
        animations[self.character]()

        # quand joue -> toujours update les hitboxs
        self.update_hitboxes()

        # boucle pour acceder a tous les monstres1
        for cat in self.spawncat.all_cats:
            # update la hauteur du monstre1
            cat.update_y(self)
            
            # si collisions avec le sol ou plateforme : avancer
            if self.check_collision_ground(cat) or self.check_collision_platform(cat) or self.check_collision_movable_platform(cat) or self.check_collision_bounce_platform(cat):
                cat.forward(self)

                # jump a un moment aleatoire
                i = random.randint(1, 100)
                if i == 5:
                    cat.jump()
            if cat.rect.x > self.finish_flag.rect.x:
                self.removecat(cat)

        # boucle pour acceder a tous les monstres2
        for bob in self.spawnbob.all_bob:

            # update hauteur monstre2
            bob.update_y(self)

            # si trop bas alors fly
            if bob.rect.y >= (int(self.data.screen_height / 100) - 2) * 100:
                bob.flying = True
            bob.fly()

            # si collisions avec sol ou plateforme -> avancer
            if self.check_collision_bounce_platform(bob) or self.check_collision_movable_platform(bob) or self.check_collision_platform(bob):
                bob.forward(self)
                
            if bob.rect.x > self.finish_flag.rect.x:
                self.removebob(bob)

        # boucle pour acceder a toutes les movable_platform et les faire bouger
        for movable_platform in self.spawnmovableplatform.all_movable_platforms:
            movable_platform.move()

        # verif si c'est le player ou bg qui doit move
        if self.spawnplayer.player.rect.x <= 50 and not self.pressed.get(pygame.K_d):
            self.is_bg_moving = True
        elif self.spawnplayer.player.rect.x >= 750 and not self.pressed.get(pygame.K_q):
            self.is_bg_moving = True
        else:
            self.is_bg_moving = False
        
        # verif si touche pressé et possibilité de move
        if self.pressed.get(pygame.K_d) and self.finish_flag.rect.x > self.spawnplayer.player.rect.x < 1180:
            self.spawnplayer.player.orientation = 'right'
            if not self.check_collision_right():
                if not self.is_bg_moving:
                    self.spawnplayer.player.move_right()
                else:
                    self.move_right()
        
        # verif si collision avec monstre -> une vie perdue
        if self.check_collision_right():
            self.life_lost()

        # verif si touche pressé et possiblité de move
        if self.pressed.get(pygame.K_q) and self.spawnplayer.player.rect.x > 0:
            self.spawnplayer.player.orientation = 'left'
            if not self.check_collision_left():
                if not self.is_bg_moving:
                    self.spawnplayer.player.move_left()
                else:
                    self.move_left()

        # collisions avec monstre = 1 vie en -
        if self.check_collision_left():
            self.life_lost()

        # si collisions avec sol ou plateforme et touche pressée -> jump
        if self.pressed.get(pygame.K_z) and (self.check_collision_ground(self.spawnplayer.player) or self.check_collision_platform(self.spawnplayer.player) or self.check_collision_movable_platform(self.spawnplayer.player)) or self.check_collision_bounce_platform(self.spawnplayer.player):
            self.spawnplayer.player.jump()

        # verif si win
        if self.check_collision_finish_flag(self.spawnplayer.player):
            self.remove_all()
            self.nb_screen = 3

        if self.pressed.get(pygame.K_SPACE) and self.nb_screen == 5 and self.spawnplayer.player.orientation == 'right' and self.character == 3:
            if not self.spawnplayer.player.is_launching:
                self.spawnplayer.player.launch_projectile()
                self.spawnplayer.player.is_launching = True
        
        for projectile in self.spawnplayer.player.all_projectiles:
            projectile.move()
            if projectile.rect.x == projectile.startx + 350:
                self.spawnplayer.player.all_projectiles.remove(projectile)
                self.spawnplayer.player.is_launching = False
            if projectile.rect.x > self.finish_flag.rect.x + 1000:
                self.spawnplayer.player.all_projectiles.remove(projectile)
                self.spawnplayer.player.is_launching = False

            for cat in self.spawncat.all_cats:
                if self.check_collision_projectile(projectile, self.spawncat.all_cats):
                    self.spawnplayer.player.all_projectiles.remove(projectile)
                    self.spawnplayer.player.is_launching = False
                    self.spawncat.all_cats.remove(cat)
                    self.spawnplayer.player.score.add_score_cat()
            
            for bob in self.spawnbob.all_bob:
                if self.check_collision_projectile(projectile, self.spawnbob.all_bob):
                    self.spawnplayer.player.all_projectiles.remove(projectile)
                    self.spawnplayer.player.is_launching = False
                    self.spawnbob.all_bob.remove(bob)
                    self.spawnplayer.player.score.add_score_bob()
        
        for boss in self.actual_level.removeboss.spawnboss.all_boss:
            check_collision = self.check_collision_ground(boss) or self.check_collision_platform(boss) or self.check_collision_movable_platform(boss) or self.check_collision_bounce_platform(boss)
            boss.update_y()
            boss.move()
            boss.update_health_bar(screen)
            if check_collision:
                if (random.randint(1, 100)) == 54:
                    boss.jump()

        if self.pressed.get(pygame.K_j):
            self.start_boss()

        # update le joueur
        self.spawnplayer.player.update()
        self.draw(screen)

    def check_collision_right(self):
        
        # verif si collisions droite(joueur) et gauche(monstre) pour tous les monstres
        for cat in self.spawncat.all_cats:
            if pygame.Rect.colliderect(self.spawnplayer.player.hitbox_right, cat.hitbox_left):
                return True
        for bob in self.spawnbob.all_bob:
            if pygame.Rect.colliderect(self.spawnplayer.player.hitbox_right, bob.hitbox_left):
                return True
        for boss in self.actual_level.removeboss.spawnboss.all_boss:
            if pygame.Rect.colliderect(self.spawnplayer.player.hitbox_right, boss.hitbox_left):
                return True
        return False

    def check_collision_left(self):

        # verif si collisions gauche(joueur) et droite(monstre) pour tous les monstres
        for cat in self.spawncat.all_cats:
            if pygame.Rect.colliderect(self.spawnplayer.player.hitbox_left, cat.hitbox_right):
                return True
        for bob in self.spawnbob.all_bob:
            if pygame.Rect.colliderect(self.spawnplayer.player.hitbox_left, bob.hitbox_right):
                return True
        for boss in self.actual_level.removeboss.spawnboss.all_boss:
            if pygame.Rect.colliderect(self.spawnplayer.player.hitbox_left, boss.hitbox_right):
                return True
        return False

    def check_collision_top(self, monster):
        # verif si collisions top(joueur) et below(monstre)
        if pygame.Rect.colliderect(self.spawnplayer.player.hitbox_top, monster.hitbox_below):
            return True
        return False

    def check_collision_jump(self, monster):

        # verif si collisions below(joueur) et top(monstre)
        return pygame.Rect.colliderect(self.spawnplayer.player.hitbox_below, monster.hitbox_top)

    def check_collision_ground(self, sprite):

        # verif si collisions below(joueur) et sol
        for ground in self.spawnground.all_ground:
            return pygame.Rect.colliderect(sprite.hitbox_below, ground.hitbox)

    def check_collision_platform(self, sprite):

        # verif si collisions below(joueur ou monstre) et plateforme pour toutes les plateformes
        for platform in self.spawnplatform.all_platforms:
            if pygame.Rect.colliderect(sprite.hitbox_below, platform.hitbox):
                return True
        return False

    def check_collision_bounce_platform(self, sprite):

        # verif si collisions below(joueur ou monstre) et bounce_plateforme pour toutes les bounce_plateformes
        for bounce_platform in self.spawnbounceplatform.all_bounce_platforms:
            if pygame.Rect.colliderect(sprite.hitbox_below, bounce_platform.hitbox):
                return True
        return False

    def check_collision_movable_platform(self, sprite):

        # verif si collisions below(joueur ou monstre) et movable_plateforme pour toutes les movable_plateformes
        for movable_platform in self.spawnmovableplatform.all_movable_platforms:
            if pygame.Rect.colliderect(sprite.hitbox_below, movable_platform.hitbox):
                return True
        return False

    def check_collision_finish_flag(self, sprite):
        # verif si collisions left/right(joueur) et finish flag
        if pygame.Rect.colliderect(sprite.hitbox_right, self.finish_flag.hitbox):
            return True
        elif pygame.Rect.colliderect(sprite.hitbox_left, self.finish_flag.hitbox):
            return True
        return False

    def check_collision_spawnpoint(self, sprite):
        if pygame.Rect.colliderect(sprite.hitbox_right, self.actual_level.levelsource.spawnpoint1):
            self.actual_level.levelsource.spawnpoint1x -= 500
            self.actual_level.levelsource.first_checkpoint_spawn()
        elif pygame.Rect.colliderect(sprite.hitbox_right, self.actual_level.levelsource.spawnpoint2):
            self.actual_level.levelsource.spawnpoint1x += 500
            self.actual_level.levelsource.spawnpoint2x += 500
            self.actual_level.spawn_checkpoint2()
        elif pygame.Rect.colliderect(sprite.hitbox_left, self.actual_level.levelsource.spawnpoint1):
            self.actual_level.levelsource.spawnpoint1x -= 500
            if self.actual_level.levelsource.spawnpoint1x < self.actual_level.levelsource.spawnpoint2x - 1500:
                self.actual_level.spawn_checkpoint1()

    def check_collision_projectile(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def check_monster_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def check_collision_money(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def life_lost(self):
        # fait perdre une vie au joueur et lui redonne les bonnes coordonnées
        self.spawnplayer.all_players.remove(self.spawnplayer.player)
        self.spawnplayer.player.current_life -= 1
        self.lost_life += 1
        self.spawnplayer.player.rect.y = 640
        self.spawnplayer.player.rect.x = 30
        self.create_overworld(self.level.current_level, self.max_level, self.screen)
        self.nb_screen = 4
        if self.spawnplayer.player.current_life == 0:
            self.lost_life = 0
            self.max_level = 0
            self.create_overworld(0, 0, self.screen)

    def remove_all(self):
        # supprime tous les monstres et plateformes et joueurs et redonne coordonnées au joueur
        for cat in self.spawncat.all_cats:
            self.removecat(cat)
        for bob in self.spawnbob.all_bob:
            self.removebob(bob)
        for platform in self.spawnplatform.all_platforms:
            self.removeplatform(platform)
        for bounce_platform in self.spawnbounceplatform.all_bounce_platforms:
            self.removebounceplatform(bounce_platform)
        for movable_platform in self.spawnmovableplatform.all_movable_platforms:
            self.removemovableplatform(movable_platform)
        for player in self.spawnplayer.all_players:
            self.removeplayer(player)
            player.rect.x = 30
            player.rect.y = 0
        for ground in self.spawnground.all_ground:
            self.removeground(ground)
        for money in self.spawnplayer.player.moneyimage.all_money:
            self.spawnplayer.player.moneyimage.all_money.remove(money)
        for boss in self.actual_level.removeboss.spawnboss.all_boss:
            self.actual_level.removeboss.remove_boss(boss)
        self.finish_flag.rect.x = 5000
        self.finish_flag.rect.y = self.data.screen_height - 353
        self.spawnplayer.player.rect.x = 30
        self.actual_level.levelsource.spawnpoint1x = 500
        self.actual_level.levelsource.spawnpoint2x = 1000

    def move_right(self):
        # fais bouger tous les elements vers la gauche a la place du joueur        
        for cat in self.spawncat.all_cats:
            cat.rect.x -= self.velocity_move
        for bob in self.spawnbob.all_bob:
            bob.rect.x -= self.velocity_move
        for platforms in self.spawnplatform.all_platforms:
            platforms.rect.x -= self.velocity_move
        for bounce_platforms in self.spawnbounceplatform.all_bounce_platforms:
            bounce_platforms.rect.x -= self.velocity_move
        for movable_platforms in self.spawnmovableplatform.all_movable_platforms:
            movable_platforms.rect.x -= self.velocity_move
        for ground in self.spawnground.all_ground:
            ground.rect.x -= self.velocity_move
        for money in self.spawnplayer.player.moneyimage.all_money:
            money.rect.x -= self.velocity_move
        for boss in self.actual_level.removeboss.spawnboss.all_boss:
            boss.rect.x -= self.velocity_move
        self.finish_flag.rect.x -= self.velocity_move
        self.actual_level.levelsource.spawnpoint1x -= self.velocity_move
        self.actual_level.levelsource.spawnpoint2x -= self.velocity_move

    def move_left(self):
        # fais bouger tous les elements vers la droite a la place du joueur
            if self.actual_level == self.level6:
                max = 1500
            else:
                max = 1500
            if self.finish_flag.rect.x < max:
                for cat in self.spawncat.all_cats:
                    cat.rect.x += self.velocity_move
                for bob in self.spawnbob.all_bob:
                    bob.rect.x += self.velocity_move
                for platforms in self.spawnplatform.all_platforms:
                    platforms.rect.x += self.velocity_move
                for bounce_platforms in self.spawnbounceplatform.all_bounce_platforms:
                    bounce_platforms.rect.x += self.velocity_move
                for movable_platforms in self.spawnmovableplatform.all_movable_platforms:
                    movable_platforms.rect.x += self.velocity_move
                for ground in self.spawnground.all_ground:
                    ground.rect.x += self.velocity_move
                for money in self.spawnplayer.player.moneyimage.all_money:
                    money.rect.x += self.velocity_move
                for boss in self.actual_level.removeboss.spawnboss.all_boss:
                    boss.rect.x += self.velocity_move
                self.finish_flag.rect.x += self.velocity_move
                self.actual_level.levelsource.spawnpoint1x += self.velocity_move
                self.actual_level.levelsource.spawnpoint2x += self.velocity_move
   
    def restart(self):
        # supprime puis refais spawn tous les elements pour recommencer
        self.remove_all()
        self.actual_level.start_spawn()

    def create_level(self, current_level):
        levels = [self.level1, self.level2, self.level3, self.level4, self.level5, self.level6, self.level7]

        self.actual_level = levels[current_level]
        
        self.actual_level.levelsource.spawnpoint1 = pygame.Rect(500, -100, 5, 1000)
        self.actual_level.levelsource.spawnpoint2 = pygame.Rect(1000, -100, 5, 1000)

        self.level = Levels(self, self.level1.levelsource, current_level, self.screen, self.create_overworld)
        
        # initialise spawns et removes
        self.spawnbob = self.actual_level.removebob.spawnbob
        self.removebob = self.actual_level.removebob.remove_bob
        self.spawncat = self.actual_level.removecat.spawncat
        self.removecat = self.actual_level.removecat.remove_cat
        self.spawnplayer = self.actual_level.removeplayer.spawnplayer
        self.removeplayer = self.actual_level.removeplayer.remove_player
        self.spawnplatform = self.actual_level.removeplatform.spawnplatform
        self.removeplatform = self.actual_level.removeplatform.remove_platform
        self.spawnbounceplatform = self.actual_level.removebounceplatform.spawnbounceplatform
        self.removebounceplatform = self.actual_level.removebounceplatform.remove_bounce_platform
        self.spawnmovableplatform = self.actual_level.removemovableplatform.spawnmovableplatform
        self.removemovableplatform = self.actual_level.removemovableplatform.remove_movable_platform
        self.spawnground = self.actual_level.removeground.spawnground
        self.removeground = self.actual_level.removeground.remove_ground

        self.actual_level.start_spawn()

    def create_overworld(self, current_level, new_max_level, screen):
        self.remove_all()
        if new_max_level >= self.max_level:
            self.max_level = new_max_level
        self.overworld_screen = OverworldScreen(self, self.level, current_level, self.max_level, screen, self.create_level)

    def update_hitboxes(self):
        # actualise les hitboxes de tous les elements de jeu
        # hitboxes player
        if self.spawnplayer.player.current_life > 0:
            self.spawnplayer.player.hitbox_right = pygame.Rect(self.spawnplayer.player.rect.x + 80, self.spawnplayer.player.rect.y + 5, 10, 33)
            self.spawnplayer.player.hitbox_left = pygame.Rect(self.spawnplayer.player.rect.x + 3, self.spawnplayer.player.rect.y + 5, 10, 33)
            self.spawnplayer.player.hitbox_top = pygame.Rect(self.spawnplayer.player.rect.x + 5, self.spawnplayer.player.rect.y, 85, 10)
            self.spawnplayer.player.hitbox_below = pygame.Rect(self.spawnplayer.player.rect.x + 5, self.spawnplayer.player.rect.y + 34, 85, 10)

        # hitboxes monstres1
        for cat in self.spawncat.all_cats:
            cat.hitbox_right = pygame.Rect(cat.rect.x + 100, cat.rect.y + 5, 10, 55)
            cat.hitbox_left = pygame.Rect(cat.rect.x, cat.rect.y + 5, 10, 55)
            cat.hitbox_top = pygame.Rect(cat.rect.x + 5, cat.rect.y, 95, 10)
            cat.hitbox_below = pygame.Rect(cat.rect.x + 5, cat.rect.y + 60, 95, 10)
        
        # hitboxes monstres2
        for bob in self.spawnbob.all_bob:
            bob.hitbox_right = pygame.Rect(bob.rect.x + 60, bob.rect.y + 5, 10, 55)
            bob.hitbox_left = pygame.Rect(bob.rect.x, bob.rect.y + 5, 10, 55)
            bob.hitbox_top = pygame.Rect(bob.rect.x + 5, bob.rect.y, 55, 10)
            bob.hitbox_below = pygame.Rect(bob.rect.x + 5, bob.rect.y + 60, 55, 10)

        for boss in self.actual_level.removeboss.spawnboss.all_boss:
            if boss.current_health > 0:
                boss.hitbox_right = pygame.Rect(boss.rect.x + 350, boss.rect.y + 5, 10, 395)
                boss.hitbox_left = pygame.Rect(boss.rect.x, boss.rect.y + 5, 10, 395)
                boss.hitbox_top = pygame.Rect(boss.rect.x + 5, boss.rect.y, 345, 10)
                boss.hitbox_below = pygame.Rect(boss.rect.x + 5, boss.rect.y + 400, 345, 10)
            else:
                self.actual_level.removeboss.spawnboss.all_boss.remove(boss)
                self.spawnplayer.player.score.add_score_boss()
                self.finish_flag.rect.x = 1500

        # hitboxes plateformes
        for platform in self.spawnplatform.all_platforms:
            platform.hitbox = pygame.Rect(platform.rect.x + 10, platform.rect.y + 20, 105, 10)

        # hitboxes bounce plateformes
        for bounce_platform in self.spawnbounceplatform.all_bounce_platforms:
            bounce_platform.hitbox = pygame.Rect(bounce_platform.rect.x + 10, bounce_platform.rect.y + 20, 105, 10)

        # hitboxes movable plateformes
        for movable_platform in self.spawnmovableplatform.all_movable_platforms:
            movable_platform.hitbox = pygame.Rect(movable_platform.rect.x + 10, movable_platform.rect.y + 20, 105, 10)

        # hitbox flag
        self.finish_flag.hitbox = pygame.Rect(self.finish_flag.rect.x + 60, self.finish_flag.rect.y, 10, 334)
        
        self.check_collision_spawnpoint(self.spawnplayer.player)
        self.actual_level.levelsource.spawnpoint1 = pygame.Rect(self.actual_level.levelsource.spawnpoint1x, -500, 5, 2000)
        self.actual_level.levelsource.spawnpoint2 = pygame.Rect(self.actual_level.levelsource.spawnpoint2x, -500, 5, 2000)

    def draw(self, screen):
        self.actual_level.run(screen)
