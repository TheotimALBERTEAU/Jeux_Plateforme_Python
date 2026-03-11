import pygame


class PauseScreen:

    def __init__(self, game):
        self.game = game
        # bouton play
        self.play_button = pygame.image.load('assets/buttons/play_button.jpg')
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_hitbox = pygame.Rect(self.play_button_rect.x, self.play_button_rect.y, 50, 50)
        
        # bouton infos
        self.info_button = pygame.image.load('assets/buttons/info_button.jpg')
        self.info_button_rect = self.info_button.get_rect()
        self.info_button_rect.y = 75
        self.info_button_hitbox = pygame.Rect(self.info_button_rect.x, self.info_button_rect.y, 50, 50)
        self.key_z = pygame.image.load('assets/infos/key_z.jpg')
        self.key_q = pygame.image.load('assets/infos/key_q.jpg')
        self.key_s = pygame.image.load('assets/infos/key_s.jpg')
        self.key_d = pygame.image.load('assets/infos/key_d.jpg')
        self.key_space = pygame.image.load('assets/infos/key_space.jpg')

        # bouton settings
        self.settings_button = pygame.image.load('assets/buttons/settings_button1.jpg')
        self.settings_button = pygame.transform.scale(self.settings_button, (50, 50))
        self.settings_button_rect = self.settings_button.get_rect()
        self.settings_button_rect.x = self.game.data.screen_width - 75
        self.settings_button_hitbox = pygame.Rect(self.settings_button_rect.x, self.settings_button_rect.y, 50, 50)
        self.reso_1 = pygame.image.load('assets/buttons/button_reso_1.jpg')
        self.reso_2 = pygame.image.load('assets/buttons/button_reso_2.jpg')     
        self.fullscreen_button = pygame.transform.scale(pygame.image.load('./assets/buttons/fullscreen_button.jpg'), (175, 56))
        self.reso_1_hitbox = pygame.Rect(0, 0, 0, 0)
        self.reso_2_hitbox = pygame.Rect(0, 0, 0, 0)
        self.fullscreen_hitbox = pygame.Rect(0, 0, 0, 0)

        # bouton restart
        self.restart_button = pygame.image.load('assets/buttons/restart_logo_button.jpg')
        self.restart_button = pygame.transform.scale(self.restart_button, (50, 50))
        self.restart_button_rect = self.restart_button.get_rect()
        self.restart_button_rect.y = 150
        self.restart_button_hitbox = pygame.Rect(self.restart_button_rect.x, self.restart_button_rect.y, 50, 50)

        # bouton home
        self.home_button = pygame.image.load('assets/buttons/home_button.jpg')
        self.home_button = pygame.transform.scale(self.home_button, (50, 50))
        self.home_button_rect = self.home_button.get_rect()
        self.home_button_rect.y = 225
        self.home_button_hitbox = pygame.Rect(self.home_button_rect.x, self.home_button_rect.y, 50, 50)

        # bouton menu
        self.menu_button = pygame.image.load('assets/buttons/levels_menu.jpg')
        self.menu_button = pygame.transform.scale(self.menu_button, (50, 50))
        self.menu_button_rect = self.menu_button.get_rect()
        self.menu_button_rect.y = 300
        self.menu_button_hitbox = pygame.Rect(self.menu_button_rect.x, self.menu_button_rect.y, 50, 50)

        # boutons ✅ et ❎
        self.ok_button = pygame.image.load('assets/buttons/ok_button.jpg')
        self.ok_button_hitbox = pygame.Rect(0, 0, 0, 0)
        self.not_ok_button = pygame.image.load('assets/buttons/not_ok_button.jpg')
        self.not_ok_button_hitbox = pygame.Rect(0, 0, 0, 0)

        self.easter_egg_hitbox = pygame.Rect(0, 0, 0, 0)

    def pause_screen(self, screen):
        # met en ordre et affiche elements de l'ecran de pause
        bg_pause = pygame.image.load('assets/backgrounds/background_pause.jpg')
        bg_pause = pygame.transform.scale(bg_pause, (self.game.data.screen_width, self.game.data.screen_height))
        self.play_button = pygame.transform.scale(self.play_button, (50, 50))
        self.info_button = pygame.transform.scale(self.info_button, (50, 50))
        logo = pygame.transform.scale(pygame.image.load('./assets/objects/logo2.jpg'), (600, 400))
        logo_rect = logo.get_rect()
        logo_rect.x = self.game.data.screen_width / 2 - 280
        logo_rect.y = 70
        self.easter_egg_hitbox = pygame.Rect(logo_rect.x + 370, logo_rect.y + 111, 10, 5)

        screen.blit(bg_pause, (0, 0))
        screen.blit(logo, (logo_rect))
        screen.blit(self.play_button, self.play_button_rect)
        screen.blit(self.info_button, self.info_button_rect)
        screen.blit(self.restart_button, self.restart_button_rect)
        screen.blit(self.home_button, self.home_button_rect)
        screen.blit(self.menu_button, self.menu_button_rect)
        screen.blit(self.settings_button, self.settings_button_rect)

    def infos(self, screen):
        # mini ecran d'infos de touches
        self.key_z = pygame.transform.scale(self.key_z, (50, 50))
        screen.blit(self.key_z, (125, 50))
        self.key_q = pygame.transform.scale(self.key_q, (50, 50))
        screen.blit(self.key_q, (75, 100))
        self.key_s = pygame.transform.scale(self.key_s, (50, 50))
        screen.blit(self.key_s, (125, 100))
        self.key_d = pygame.transform.scale(self.key_d, (50, 50))
        screen.blit(self.key_d, (175, 100))
        self.key_space = pygame.transform.scale(self.key_space, (100, 50))
        screen.blit(self.key_space, (100, 150))
    
    def settings(self, screen):
        # menu settings
        self.reso_1 = pygame.transform.scale(self.reso_1, (175, 56))
        self.reso_1_rect = self.reso_1.get_rect()
        self.reso_1_rect.x = self.game.data.screen_width - 250
        self.reso_1_hitbox = pygame.Rect(self.reso_1_rect.x, self.reso_1_rect.y, 175, 56)
        screen.blit(self.reso_1, self.reso_1_rect)
        
        self.reso_2 = pygame.transform.scale(self.reso_2, (175, 56))
        self.reso_2_rect = self.reso_2.get_rect()
        self.reso_2_rect.x = self.game.data.screen_width - 250
        self.reso_2_rect.y = 70
        self.reso_2_hitbox = pygame.Rect(self.reso_2_rect.x, self.reso_2_rect.y, 175, 56)
        screen.blit(self.reso_2, self.reso_2_rect)

        self.fullscreen_rect = self.fullscreen_button.get_rect()
        self.fullscreen_rect.x = self.game.data.screen_width - 250
        self.fullscreen_rect.y = 140
        self.fullscreen_hitbox = pygame.Rect(self.fullscreen_rect.x, self.fullscreen_rect.y, 175, 56)
        screen.blit(self.fullscreen_button, self.fullscreen_rect)

    def reload(self):
        self.settings_button_rect.x = self.game.data.screen_width - 75
        self.settings_button_hitbox = pygame.Rect(self.settings_button_rect.x, self.settings_button_rect.y, 50, 50)
        self.game.data.warning_rect = self.game.data.warning_surface.get_rect(center = (self.game.data.screen_width / 2, self.game.data.screen_height / 2 - 25))
        self.game.data.choice_rect = self.game.data.choice_surface.get_rect(center = (self.game.data.screen_width / 2, self.game.data.screen_height / 2 + 25))

    def warning(self, screen):
        self.ok_button = pygame.transform.scale(self.ok_button, (100, 100))
        self.ok_button_rect = self.ok_button.get_rect()
        self.ok_button_rect.x = self.game.data.screen_width / 4
        self.ok_button_rect.y = self.game.data.screen_width / 3
        self.ok_button_hitbox = pygame.Rect(self.ok_button_rect.x, self.ok_button_rect.y, 100, 100)

        self.not_ok_button = pygame.transform.scale(self.not_ok_button, (100, 100))
        self.not_ok_button_rect = self.not_ok_button.get_rect()
        self.not_ok_button_rect.x = self.game.data.screen_width / 2 + 200
        self.not_ok_button_rect.y = self.game.data.screen_width / 3
        self.not_ok_button_hitbox = pygame.Rect(self.not_ok_button_rect.x, self.not_ok_button_rect.y, 100, 100)

        # creation menu warning
        screen.fill('Black')
        screen.blit(self.game.data.warning_surface, self.game.data.warning_rect)
        screen.blit(self.game.data.choice_surface, self.game.data.choice_rect)
        screen.blit(self.ok_button, self.ok_button_rect)
        screen.blit(self.not_ok_button, self.not_ok_button_rect)
