import pygame

        

basic_skin = pygame.image.load('assets/skins/basic_skin.jpg')
basic_skin = pygame.transform.scale(basic_skin, (200, 160))
basic_skin_rect = basic_skin.get_rect(center = (640, 360))

batman_skin = pygame.image.load('assets/skins/skin_batman_unlock.jpg')
batman_skin = pygame.transform.scale(batman_skin, (200, 160))
batman_skin_rect = batman_skin.get_rect(center = (640, 360))

launcher_skin = pygame.image.load('assets/skins/launcher_skin_unlock.jpg')
launcher_skin = pygame.transform.scale(launcher_skin, (200, 160))
launcher_skin_rect = batman_skin.get_rect(center = (640, 360))

flash_skin = pygame.transform.scale(pygame.image.load('assets/skins/flash_skin_unlock.jpg'), (200, 160))
flash_skin_rect = flash_skin.get_rect(center = (640, 360))

super_skin = pygame.transform.scale(pygame.image.load('assets/skins/super_skin_unlock.jpg'), (200, 160))
super_skin_rect = super_skin.get_rect(center = (640, 360))

max_skins = 4

basic_skin = {'name' : basic_skin,
              'skin' : 'assets/skins/basic_skin.jpg',
              'character' : 'just a normal capybara.',
              'power' : "But, at least, he can do... nothing but he's funny",
              'price' : '0',
              'unlock' : '1'
             }

batman_skin = {'name' : batman_skin,
               'skin' : 'assets/skins/skin_batman.jpg',
               'character' : 'capybatman is a dark capybara.',
               'power' : 'and with his cape, he can glide down more slowly',
               'price' : '10',
               'unlock' : '0'
              }

launcher_skin = {'name' : launcher_skin,
                 'skin' : 'assets/skins/launcher_skin.jpg',
                 'character' : "he's a sniper capybara",
                 'power' : 'Who can launch projectiles to kill monsters',
                 'price' : '20',
                 'unlock' : '0'
                }

flash_skin = {'name' : flash_skin,
              'skin' : 'assets/skins/flash_skin.jpg',
              'character' : "he's a super-capybara.",
              'power' : 'Who can run very, very, very fast.',
              'price' : '30',
              'unlock' : '0'
             }

super_skin = {'name' : super_skin,
              'skin' : 'assets/skins/super_skin.jpg',
              'character' : "Nobody know what is this capybara.",
              'power' : "But rumors say he's the stronger and better capybara",
              'price' : '???',
              'unlock' : '1'
             }

skins = {
    0 : basic_skin,
    1 : batman_skin,
    2 : launcher_skin,
    3 : flash_skin,
    4 : super_skin,
}
