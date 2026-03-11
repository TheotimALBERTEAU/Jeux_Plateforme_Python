import pygame
from data import Data
from game import Game
from screens.home_screen import HomeScreen
from screens.play_screen import PlayScreen
from screens.pause_screen import PauseScreen
from screens.win_screen import WinScreen
from screens.skin_screen import SkinScreen
from objects.skins_data import *


# initialisation de pygame et de la fenetre de jeu
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Super Capy Bros")
data = Data()
screen = pygame.display.set_mode((data.screen_width, data.screen_height))

running = True

# instances de plusieurs classes
game = Game(screen)
play_screen = PlayScreen(game)
home_screen = HomeScreen(game)
pause_screen = PauseScreen(game)
win_screen = WinScreen(screen, game)
skin_screen = SkinScreen(game)

cursor = pygame.cursors.Cursor((0, 0), game.cursor)
pygame.mouse.set_cursor(cursor)

game_icon = pygame.image.load('assets/objects/logo.jpg')
pygame.display.set_icon(game_icon)

# boucle de verif si la fenetre est lancé
while running:
        
    # actualise fenetre
    pygame.display.flip()
    clock.tick(240)

    # verif de la variable nb_screen pour afficher le bon screen
    # ecran d'accueil | 1
    if game.nb_screen == 1:
        home_screen.home_screen(screen)

    # ecran d'accueil | 1.2
    if game.nb_screen == 1.2:
        skin_screen.skin_screen(screen)

    # ecran de pause | 2
    elif game.nb_screen == 2:
        pause_screen.pause_screen(screen)

    # ajoute infos de touches a pause | 2.1
    elif game.nb_screen == 2.1:
        pause_screen.pause_screen(screen)
        pause_screen.infos(screen)

    elif game.nb_screen == 2.2:
        pause_screen.pause_screen(screen)
        pause_screen.settings(screen)

    # ecran de reso vers 1920x1080 | 2.3
    elif game.nb_screen == 2.3:
        pause_screen.warning(screen)

    # ecran de reso vers 1280x720  | 2.4
    elif game.nb_screen == 2.4:
        pause_screen.warning(screen)

    # ecran de reso vers fullscreen  | 2.5
    elif game.nb_screen == 2.5:
        pause_screen.warning(screen)

    # ecran de victoire (a finir) | 3
    elif game.nb_screen == 3:
        win_screen.win_screen(screen)

    # ecran de selection de niveau | 4
    elif game.nb_screen == 4:
        game.overworld_screen.overworld_screen(screen)
    
    # ecran de jeu | 5
    elif game.nb_screen == 5:
        play_screen.play_screen(screen)
        game.play(screen)
        game.level.input()

    # verif des differents evenements
    for event in pygame.event.get():
        
        # fermeture de la fenetre | ❌
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # touche pressé = ajouter la touche en True
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        
            if game.pressed.get(pygame.K_RCTRL):
                running = False
                pygame.quit()

            if game.pressed.get(pygame.K_i):
                skins[game.current_skin]['unlock'] = '1'
                skin_screen.actualize_skins()
                skin_screen.reload()

        # touche relaché = passer touche en False
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # verif clique de souris
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # clique sur bouton start
            if home_screen.start_button_hitbox.collidepoint(event.pos) and game.nb_screen == 1:
                game.nb_screen = 4

            elif home_screen.skins_button_hitbox.collidepoint(event.pos) and game.nb_screen == 1:
                game.nb_screen = 1.2

            elif game.overworld_screen.skins_button_hitbox.collidepoint(event.pos) and game.nb_screen == 4:
                game.nb_screen = 1.2

            elif skin_screen.menu_button_hitbox.collidepoint(event.pos) and game.nb_screen == 1.2:
                game.nb_screen = 4

            elif skin_screen.home_button_hitbox.collidepoint(event.pos) and game.nb_screen == 1.2:
                game.nb_screen = 1

            # clique bouton pause
            elif play_screen.pause_button_hitbox.collidepoint(event.pos) and game.nb_screen == 5:
                game.nb_screen = 2

            # clique bouton play
            elif pause_screen.play_button_hitbox.collidepoint(event.pos) and (game.nb_screen == 2 or game.nb_screen == 2.1 or game.nb_screen == 2.2):
                game.nb_screen = 5

            # clique bouton infos touches
            elif pause_screen.info_button_hitbox.collidepoint(event.pos) and (game.nb_screen == 2 or game.nb_screen == 2.1 or game.nb_screen ==  2.2):
                # si fermé => ouvrir
                if game.nb_screen == 2:
                    game.nb_screen = 2.1
                # si ouvert => fermer
                else:
                    game.nb_screen = 2
            
            elif pause_screen.easter_egg_hitbox.collidepoint(event.pos) and (game.nb_screen == 2 or game.nb_screen == 2.1 or game.nb_screen ==  2.2):
                skins[5]['unlock'] = '1'
                game.current_skin = 5
                game.nb_screen = 1.2
                skin_screen.reload()

            # clique bouton rejouer quand gagner
            elif win_screen.restart_button_hitbox.collidepoint(event.pos) and game.nb_screen == 3:
                game.restart()
                game.nb_screen = 5

            # clique bouton rejouer dans ecran pause
            elif pause_screen.restart_button_hitbox.collidepoint(event.pos) and (game.nb_screen == 2 or game.nb_screen == 2.1 or game.nb_screen == 2.2):
                game.restart()
                game.nb_screen = 5

            elif win_screen.menu_button_hitbox.collidepoint(event.pos) and game.nb_screen == 3:
                game.create_overworld(game.level.current_level, game.level.level_data['unlock'], screen)
                game.nb_screen = 4
            
            elif pause_screen.home_button_hitbox.collidepoint(event.pos) and (game.nb_screen == 2 or game.nb_screen == 2.1 or game.nb_screen == 2.2):
                game.nb_screen = 1
                home_screen.reload()

            elif pause_screen.menu_button_hitbox.collidepoint(event.pos) and (game.nb_screen == 2 or game.nb_screen == 2.1 or game.nb_screen == 2.2):
                game.create_overworld(game.level.current_level, game.max_level, screen)
                game.nb_screen = 4

            elif pause_screen.settings_button_hitbox.collidepoint(event.pos) and (game.nb_screen == 2 or game.nb_screen == 2.1 or game.nb_screen == 2.2):
                if (game.nb_screen == 2 or game.nb_screen == 2.1):
                    game.nb_screen = 2.2
                else:
                    game.nb_screen = 2

            elif pause_screen.reso_1_hitbox.collidepoint(event.pos) and game.nb_screen == 2.2:
                game.nb_screen = 2.3
                
            elif pause_screen.ok_button_hitbox.collidepoint(event.pos) and game.nb_screen == 2.3:
                game.data.screen_width = 1920
                game.data.screen_height = 1080
                screen = pygame.display.set_mode((game.data.screen_width, game.data.screen_height))
                game.restart()
                pause_screen.reload()
                win_screen.reload()
                game.nb_screen = 2

            elif pause_screen.not_ok_button_hitbox.collidepoint(event.pos) and game.nb_screen == 2.3:
                game.nb_screen = 2
            
            elif pause_screen.reso_2_hitbox.collidepoint(event.pos) and game.nb_screen == 2.2:
                game.nb_screen = 2.4

            elif pause_screen.ok_button_hitbox.collidepoint(event.pos) and game.nb_screen == 2.4:
                game.data.screen_width = 1280
                game.data.screen_height = 720
                screen = pygame.display.set_mode((game.data.screen_width, game.data.screen_height))
                game.restart()
                pause_screen.reload()
                win_screen.reload()
                game.nb_screen = 2

            elif pause_screen.not_ok_button_hitbox.collidepoint(event.pos) and game.nb_screen == 2.4:
                game.nb_screen = 2

            elif pause_screen.fullscreen_hitbox.collidepoint(event.pos) and game.nb_screen == 2.2:
                game.nb_screen = 2.5

            elif pause_screen.ok_button_hitbox.collidepoint(event.pos) and game.nb_screen == 2.5:
                game.data.screen_width = 1920
                game.data.screen_height = 1080
                screen = pygame.display.set_mode((game.data.screen_width, game.data.screen_height), pygame.FULLSCREEN)
                game.restart()
                pause_screen.reload()
                win_screen.reload()
                game.nb_screen = 2

            elif pause_screen.not_ok_button_hitbox.collidepoint(event.pos) and game.nb_screen == 2.5:
                game.nb_screen = 2

            elif skin_screen.left_arrow_hitbox.collidepoint(event.pos) and game.nb_screen == 1.2:
                if game.current_skin > 0:
                    game.current_skin -= 1
                else:
                    game.current_skin = max_skins
                skin_screen.reload()
            
            elif skin_screen.right_arrow_hitbox.collidepoint(event.pos) and game.nb_screen == 1.2:
                if game.current_skin < max_skins:
                    game.current_skin += 1
                else:
                    game.current_skin = 0
                skin_screen.reload()

            
            elif skin_screen.buy_button_hitbox.collidepoint(event.pos) and game.nb_screen == 1.2:
                if skins[game.current_skin]['unlock'] == '0':
                    if not game.current_skin == 5:
                        if game.money >= int(skins[game.current_skin]['price']):
                            game.money -= int(skins[game.current_skin]['price'])
                            skins[game.current_skin]['unlock'] = '1'
                            skin_screen.actualize_skins()
                            skin_screen.reload()
                        else:
                            print("Ooooooh, you don't have enough money to buy this 😢")
                    else:
                        print("Why you wan't to buy this capybara if you don't know how many he coast")
                elif skins[game.current_skin]['unlock'] == '1':
                    game.character = game.current_skin
                    game.create_overworld(game.level.current_level, game.max_level, screen)
                    game.nb_screen = 4
