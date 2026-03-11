import pygame
from removes.remove_bob import RemoveBob
from removes.remove_cat import RemoveCat
from removes.remove_player import RemovePlayer
from removes.remove_platform import RemovePlatform
from removes.remove_bounce_platform import RemoveBouncePlatform
from removes.remove_movable_platform import RemoveMovablePlatform
from removes.remove_ground import RemoveGround
from removes.remove_boss import RemoveBoss
from objects.money import Money
from data import *


class LevelSource:
    def __init__(self, game):
        self.game = game
        self.removebob = RemoveBob(game)
        self.removecat = RemoveCat(game)
        self.removeplayer = RemovePlayer(game)
        self.removeplatform = RemovePlatform(game)
        self.removebounceplatform = RemoveBouncePlatform(game)
        self.removemovableplatform = RemoveMovablePlatform(game)
        self.removeground = RemoveGround(game)
        self.removeboss = RemoveBoss(game)
        self.levelsource = self
        self.spawnpoint1x = 500
        self.spawnpoint2x = 1000
        self.spawnpoint1 = pygame.Rect(self.spawnpoint1x, -500, 5, 2000)
        self.spawnpoint2 = pygame.Rect(self.spawnpoint2x, -500, 5, 2000)
        self.is_collision_spawnpoint = 0

    def run(self, screen):
        # affiche tous les elements
        self.removeground.spawnground.all_ground.draw(screen)
        
        self.removeplatform.spawnplatform.all_platforms.draw(screen)
        self.removebounceplatform.spawnbounceplatform.all_bounce_platforms.draw(screen)
        self.removemovableplatform.spawnmovableplatform.all_movable_platforms.draw(screen)
        self.removeplayer.spawnplayer.all_players.draw(screen)
        self.removecat.spawncat.all_cats.draw(screen)
        self.removebob.spawnbob.all_bob.draw(screen)
        self.removeboss.spawnboss.all_boss.draw(screen)
        
        screen.blit(self.game.finish_flag.image, self.game.finish_flag.rect)
        self.removeplayer.spawnplayer.player.all_projectiles.draw(screen)
        screen.blit(self.removeplayer.spawnplayer.player.money_surface, self.removeplayer.spawnplayer.player.money_rect)
        self.removeplayer.spawnplayer.player.money_surface = self.removeplayer.spawnplayer.player.font.render(f'money : {self.game.money}', True, (255, 107, 0))
        screen.blit(self.removeplayer.spawnplayer.player.score.surface, self.removeplayer.spawnplayer.player.score.rect)
        self.removeplayer.spawnplayer.player.score.surface = self.removeplayer.spawnplayer.player.score.font.render(f'score : {self.removeplayer.spawnplayer.player.score.current_score}', True, (255, 107, 0))
        self.removeplayer.spawnplayer.player.life.all_lifes.draw(screen)
        self.removeplayer.spawnplayer.player.moneyimage.all_money.draw(screen)

    def spawn_checkpoint1(self):
        # fais spawn le bon nombre de plateformes/monstres/joueurs et le finish flag
        for i in self.game.actual_level.cat_x_spawnpoint1:
            self.game.actual_level.removecat.spawncat.spawn_cat()
            if self.game.data.screen_width <= 1280:
                self.game.spawncat.cat.rect.x = i
            else:
                self.game.spawncat.cat.rect.x = i - 450
        if self.game.level.current_level >= 1:
            for i in self.game.actual_level.bob_x_spawnpoint1:
                self.game.actual_level.removebob.spawnbob.spawn_bob()
                self.game.spawnbob.bob.rect.x = i
            
    def spawn_checkpoint2(self):
        for i in self.cat_x_spawnpoint2:
            self.game.actual_level.removecat.spawncat.spawn_cat()
            if self.game.data.screen_width <= 1280:
                self.game.spawncat.cat.rect.x = i
            else:
                self.game.spawncat.cat.rect.x = i + 450
        if self.game.level.current_level >= 1:
            for i in self.game.actual_level.bob_x_spawnpoint2:
                self.game.actual_level.removebob.spawnbob.spawn_bob()
                self.game.spawnbob.bob.rect.x = i

    def start_spawn(self):
        self.removeplayer.spawnplayer.spawn_player()
        self.removeground.spawnground.spawn_ground()
        for i in range(len(self.money_x)):
            self.money = Money(self.game)
            self.removeplayer.spawnplayer.player.moneyimage.all_money.add(self.money)
            self.money.rect.x = self.money_x[i]
            if self.game.data.screen_width <= 1280:
                self.money.rect.y = self.money_y[i]
            else:
                self.money.rect.y = self.money_y[i] + 360
        for i in self.cat_x_startspawn:
            self.game.actual_level.removecat.spawncat.spawn_cat()
            if self.game.data.screen_width <= 1280:
                self.game.spawncat.cat.rect.x = i
            else:
                self.game.spawncat.cat.rect.x = i + 450
        for i in range(len(self.platform_x_startspawn)):
            self.game.actual_level.removeplatform.spawnplatform.spawn_platform()
            self.game.spawnplatform.platform.rect.x = self.platform_x_startspawn[i]
            if self.game.data.screen_height <= 720:
                self.game.spawnplatform.platform.rect.y = self.platform_y_startspawn[i]
            else:
                self.game.spawnplatform.platform.rect.y = self.platform_y_startspawn[i] + 360
        for i in range(len(self.bounce_x_startspawn)):
            self.game.actual_level.removebounceplatform.spawnbounceplatform.spawn_bounce_platform()
            self.game.spawnbounceplatform.bounce_platform.rect.x = self.bounce_x_startspawn[i]
            if self.game.data.screen_height <= 720:
                self.game.spawnbounceplatform.bounce_platform.rect.y = self.bounce_y_startspawn[i]
            else:
                self.game.spawnbounceplatform.bounce_platform.rect.y = self.bounce_y_startspawn[i] + 360
        if self.game.level.current_level >= 1:
            for i in self.game.actual_level.bob_x_startspawn:
                self.game.actual_level.removebob.spawnbob.spawn_bob()
                self.game.spawnbob.bob.rect.x = i
        if self.game.level.current_level >= 2:
            for i in range(len(self.movable_x_startspawn)):
                self.game.actual_level.removemovableplatform.spawnmovableplatform.spawn_movable_platform()
                self.game.spawnmovableplatform.movable_platform.rect.x = self.game.actual_level.movable_x_startspawn[i]
                if self.game.data.screen_height <= 720:
                    self.game.spawnmovableplatform.movable_platform.rect.y = self.game.actual_level.movable_y_startspawn[i]
                else:
                    self.game.spawnmovableplatform.movable_platform.rect.y = self.game.actual_level.movable_y_startspawn[i] + 360
        if self.game.level.current_level == 6:
            self.removeboss.spawnboss.spawn_boss()

    def first_checkpoint_spawn(self):
        for i in self.cat_x_firstspawn:
            self.game.actual_level.removecat.spawncat.spawn_cat()
            if self.game.data.screen_width <= 1280:
                self.game.spawncat.cat.rect.x = i
            else:
                self.game.spawncat.cat.rect.x = i + 450
        if self.game.level.current_level >= 1:  
            for i in self.bob_x_firstspawn:
                self.game.actual_level.removebob.spawnbob.spawn_bob()
                self.game.spawnbob.bob.rect.x = i
