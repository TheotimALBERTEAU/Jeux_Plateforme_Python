import pygame
from objects.skins_data import *


class SkinScreen:
    def __init__(self, game):
        self.game = game

        self.left_arrow = pygame.image.load('./assets/buttons/left_arrow.jpg')
        self.left_arrow = pygame.transform.scale(self.left_arrow, (75, 75))
        self.left_arrow_rect = self.left_arrow.get_rect()
        self.left_arrow_rect.x = self.game.data.screen_width / 2 - 400
        self.left_arrow_rect.y = self.game.data.screen_height / 2 - 75
        self.left_arrow_hitbox = pygame.Rect(self.left_arrow_rect.x, self.left_arrow_rect.y, 75, 75)

        self.right_arrow = pygame.image.load('./assets/buttons/right_arrow.jpg')
        self.right_arrow = pygame.transform.scale(self.right_arrow, (75, 75))
        self.right_arrow_rect = self.right_arrow.get_rect()
        self.right_arrow_rect.x = self.game.data.screen_width / 2 + 325
        self.right_arrow_rect.y = self.game.data.screen_height / 2 - 75
        self.right_arrow_hitbox = pygame.Rect(self.right_arrow_rect.x, self.right_arrow_rect.y, 75, 75)

        self.equip_button = pygame.image.load('./assets/buttons/equip_button.jpg')
        self.equip_button = pygame.transform.scale(self.equip_button, (400, 150))
        self.equip_button_rect = self.equip_button.get_rect(center = (self.game.data.screen_width / 2, self.game.data.screen_height - 100))
        self.equip_button_hitbox = pygame.Rect(self.equip_button_rect.x, self.equip_button_rect.y, 400, 150)

        self.buy_button = pygame.transform.scale(pygame.image.load('assets/buttons/buy_button.jpg'), (400, 150))
        self.buy_button_rect = self.buy_button.get_rect(center = (self.game.data.screen_width / 2, self.game.data.screen_height - 100))
        self.buy_button_hitbox = pygame.Rect(self.buy_button_rect.x, self.buy_button_rect.y, 400, 150)
        
        self.other_button = pygame.transform.scale(pygame.image.load('assets/buttons/other_button.jpg'), (400, 150))
        self.other_button_rect = self.other_button.get_rect(center = (self.game.data.screen_width / 2, self.game.data.screen_height - 100))

        # bouton menu
        self.menu_button = pygame.transform.scale(pygame.image.load('assets/buttons/levels_menu.jpg'), (50, 50))
        self.menu_button_rect = self.menu_button.get_rect(center = (30, 30))
        self.menu_button_hitbox = pygame.Rect(self.menu_button_rect.x, self.menu_button_rect.y, 50, 50)

        # bouton home
        self.home_button = pygame.transform.scale(pygame.image.load('assets/buttons/home_button.jpg'), (50, 50))
        self.home_button_rect = self.home_button.get_rect(center = (30, 90))
        self.home_button_hitbox = pygame.Rect(self.home_button_rect.x, self.home_button_rect.y, 50, 50)

        if skins[self.game.current_skin]['unlock'] == '1':
            self.actual_skin = pygame.transform.scale(pygame.image.load(skins[self.game.current_skin]['skin']), (200, 160))
        else:
            self.actual_skin = skins[self.game.current_skin]['name']

        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render(skins[self.game.current_skin]['character'], True, (255, 107, 0))
        self.text_rect = self.text.get_rect(center = (self.game.data.screen_width / 2, self.game.data.screen_height / 2))
        self.text_rect.y = self.game.data.screen_height / 2 + 100

        self.power = self.font.render(skins[self.game.current_skin]['power'], True, (255, 107, 0))
        self.power_rect = self.power.get_rect(center = (self.game.data.screen_width / 2, self.game.data.screen_height / 2))
        self.power_rect.y = self.text_rect.y + 50

        self.price = self.font.render('price : ' + skins[self.game.current_skin]['price'], True, (255, 107, 0))
        self.price_rect = self.price.get_rect(center = (self.game.data.screen_width / 2, self.game.data.screen_height / 2 - 300))

    def reload(self):
        if skins[self.game.current_skin]['unlock'] == '1':
            self.actual_skin = pygame.transform.scale(pygame.image.load(skins[self.game.current_skin]['skin']), (200, 160))
        else:
            self.actual_skin = skins[self.game.current_skin]['name']
        
        self.text = self.font.render(skins[self.game.current_skin]['character'], True, (255, 107, 0))
        self.text_rect = self.text.get_rect(center = (self.game.data.screen_width / 2, self.game.data.screen_height / 2))
        self.text_rect.y = self.game.data.screen_height / 2 + 100
        
        self.power = self.font.render(skins[self.game.current_skin]['power'], True, (255, 107, 0))
        self.power_rect = self.power.get_rect(center = (self.game.data.screen_width / 2, self.game.data.screen_height / 2))
        self.power_rect.y = self.text_rect.y + 50
    
    def actualize_skins(self):
        if skins[self.game.current_skin]['unlock'] == '1':
            skins[self.game.current_skin]['name'] = pygame.image.load(skins[self.game.current_skin]['skin'])
            skins[self.game.current_skin]['name'] = pygame.transform.scale(skins[self.game.current_skin]['name'], (200, 160))

    def skin_screen(self, screen):
        screen.fill('grey')
        screen.blit(self.left_arrow, self.left_arrow_rect)
        screen.blit(self.right_arrow, self.right_arrow_rect)
        screen.blit(self.actual_skin, (self.game.data.screen_width / 2 - 100, self.game.data.screen_height / 2 - 80))
        screen.blit(self.menu_button, self.menu_button_rect)
        screen.blit(self.home_button, self.home_button_rect)
        
        if skins[self.game.current_skin]['unlock'] == '1':
            screen.blit(self.equip_button, self.equip_button_rect)
        elif skins[self.game.current_skin]['unlock'] == '0':
            if not skins[self.game.current_skin]['price'] == '???':
                screen.blit(self.buy_button, self.buy_button_rect)
            else:
                screen.blit(self.other_button, self.other_button_rect)
        
        screen.blit(self.text, self.text_rect)
        screen.blit(self.power, self.power_rect)
        screen.blit(self.game.spawnplayer.player.money_surface, self.game.spawnplayer.player.money_rect)
        self.game.spawnplayer.player.money_surface = self.game.spawnplayer.player.font.render(f'money : {self.game.money}', True, (255, 107, 0))
        screen.blit(self.price, self.price_rect)
        self.price = self.font.render('price : ' + skins[self.game.current_skin]['price'], True, (255, 107, 0))
