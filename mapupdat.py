import pygame
import random

# Constants for colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class BackgroundTile(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class InteractiveTile(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class TilingBackground:
    def __init__(self, width, height, tile_width, tile_height, interactive_chance):
        self.width = width
        self.height = height
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.interactive_chance = interactive_chance
        self.tiles = pygame.sprite.Group()
        self.viewport_x = 0
        self.viewport_y = 0
        self.generate_tiles()

    def generate_tiles(self):
        for x in range(0, self.width, self.tile_width):
            for y in range(0, self.height, self.tile_height):
                if random.random() < self.interactive_chance:
                    tile = InteractiveTile(GREEN, self.tile_width, self.tile_height)
                else:
                    tile = BackgroundTile(BLUE, self.tile_width, self.tile_height)
                tile.rect.x = x
                tile.rect.y = y
                self.tiles.add(tile)

    def draw(self, screen):
        self.tiles.draw(screen)

    def scroll(self, dx, dy):
        # Scroll the background tiles by dx and dy
        for tile in self.tiles:
            tile.rect.x += dx
            tile.rect.y += dy

        # Update viewport position
        self.viewport_x += dx
        self.viewport_y += dy

        # Check if we need to load more tiles
        if dx > 0:  # Scrolling right
            if self.viewport_x + self.width > len(self.tiles) * self.tile_width:
                self.generate_right_tiles()
        elif dx < 0:  # Scrolling left
            if self.viewport_x < 0:
                self.generate_left_tiles()
        elif dy > 0:  # Scrolling down
            if self.viewport_y + self.height > len(self.tiles) * self.tile_height:
                self.generate_bottom_tiles()
        elif dy < 0:  # Scrolling up
            if self.viewport_y < 0:
                self.generate_top_tiles()
    def generate_right_tiles(self):
        for y in range(0, self.height, self.tile_height):
            tile = self.generate_tile(self.width - self.tile_width, y)
            self.tiles.add(tile)

    def generate_left_tiles(self):
        for y in range(0, self.height, self.tile_height):
            tile = self.generate_tile(0, y)
            self.tiles.add(tile)

    def generate_bottom_tiles(self):
        for x in range(0, self.width, self.tile_width):
            tile = self.generate_tile(x, self.height - self.tile_height)
            self.tiles.add(tile)

    def generate_top_tiles(self):
        for x in range(0, self.width, self.tile_width):
            tile = self.generate_tile(x, 0)
            self.tiles.add(tile)

    def generate_tile(self, x, y):
        if random.random() < self.interactive_chance:
            return InteractiveTile(GREEN, self.tile_width, self.tile_height)
        else:
            return BackgroundTile(BLUE, self.tile_width, self.tile_height)
