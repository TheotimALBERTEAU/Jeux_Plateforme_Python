import pygame
from data import *
from overworld.level_data import LevelData
from overworld.nodes import Node
from overworld.icon import Icon


class OverworldScreen:
    def __init__(self, game, level, start_level, max_level, screen, create_level):
        super().__init__()
        self.game = game
        self.level = level
        self.leveldata = LevelData(game, screen)
        # setup
        self.screen = screen
        self.max_level = max_level
        self.current_level = start_level
        self.move_direction = pygame.math.Vector2(0, 0)
        self.moving = False
        self.speed = self.game.data.screen_width / 160
        self.create_level = create_level

        self.setup_nodes()
        self.setup_icon()
        
        self.skins_button = pygame.transform.scale(pygame.image.load('./assets/buttons/skins_button.jpg'), (50, 50))
        self.skins_button_rect = self.skins_button.get_rect(center = (30, 30))
        self.skins_button_hitbox = pygame.Rect(self.skins_button_rect.x, self.skins_button_rect.y, 50, 50)

    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()

        for index, node_data in enumerate(self.leveldata.levels.values()):
            if index <= self.max_level:
                node_sprite = Node(node_data['node_pos'], 'available', self.speed, self.game)
            else:
                node_sprite = Node(node_data['node_pos'], 'disable', self.speed, self.game)
            self.nodes.add(node_sprite)

    def draw_paths(self, screen):
        if self.game.max_level > 0:
            points = [node['node_pos'] for index, node in enumerate(self.leveldata.levels.values()) if index <= self.max_level]
            pygame.draw.lines(screen, (255, 107, 0), False, points, 8)

    def setup_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        self.icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center)
        self.icon.add(self.icon_sprite)

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.moving:
            if keys[pygame.K_RIGHT] and self.current_level < self.max_level:
                self.move_direction = self.get_movement('next')
                self.current_level += 1
                self.moving = True
            elif keys[pygame.K_LEFT] and self.current_level > 0:
                self.move_direction = self.get_movement('previous')
                self.current_level -= 1
                self.moving = True
            elif keys[pygame.K_SPACE]:
                self.game.remove_all()
                self.game.create_level(self.current_level)
                self.game.nb_screen = 5
                pygame.time.delay(1000)

    def get_movement(self, target):
        start = pygame.math.Vector2(self.nodes.sprites()[self.current_level].rect.center)
        
        if target == 'next':
            end = pygame.math.Vector2(self.nodes.sprites()[self.current_level + 1].rect.center)
        else:
            end = pygame.math.Vector2(self.nodes.sprites()[self.current_level - 1].rect.center)

        return (end - start).normalize()
        
    def update_icon(self):
        if self.moving and self.move_direction:
            self.icon.sprite.pos += self.move_direction * self.speed
            target_node = self.nodes.sprites()[self.current_level]
            if target_node.detection_zone.collidepoint(self.icon.sprite.pos):
                self.moving = False
                self.move_direction = pygame.math.Vector2(0, 0)

    def overworld_screen(self, screen):
        screen.fill('black')
        self.input()
        self.update_icon()
        self.icon.update()
        self.draw_paths(screen)
        self.nodes.draw(screen)
        self.icon.draw(screen)
        screen.blit(self.skins_button, self.skins_button_rect)
