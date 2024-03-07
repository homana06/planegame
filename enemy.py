import pygame
import math
import random
from bullet import *


class Enemy:
    def __init__(self, x, y, player_x, player_y):
        self.x = x
        self.y = y
        self.player_x = player_x
        self.player_y = player_y
        self.speed = 2
        self.width = 20
        self.height = 20
        self.color = (255, 0, 0)
        self.shoot_interval = 60  # Interval in frames between shots
        self.shoot_timer = random.randint(0, self.shoot_interval)  # Random initial timer value

    def move(self):
        # Move towards the player's position
        angle = math.atan2(self.player_y - self.y, self.player_x - self.x)
        self.x += self.speed * math.cos(angle)
        self.y += self.speed * math.sin(angle)

    def shoot(self):
        # Shoot at the player
        # In a real game, you would create a bullet object here
        print("Enemy shoots at player")

    def update(self, player_x, player_y):
        # Update player's position
        self.player_x = player_x
        self.player_y = player_y

        # Move towards the player
        self.move()

        # Decrease shoot timer
        self.shoot_timer -= 1

        # Shoot if the shoot timer reaches zero
        if self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = self.shoot_interval

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

