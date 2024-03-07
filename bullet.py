import pygame
import math




class Bullet:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 10
        self.width = 5
        self.height = 10
        self.color = (255, 0, 0)

    def move(self, angle, x, y, surface):
        # Move the bullet in the direction defined by its angle
        while 0 <= x <= surface.get_width() and 0 <= y <= surface.get_height():
            x = x + self.speed * math.cos(math.radians(angle))
            y = y - self.speed * math.sin(math.radians(angle))  # Negative since y-coordinates increase downward
            self.draw(surface, x, y)
            pygame.display.update()  # Update the display to show the bullet's movement

    def draw(self, surface, x, y):
        pygame.draw.rect(surface, self.color, (x, y, self.width, self.height))

    def move_until_off_screen(self, surface, angle, x, y):
        # Continuously move and draw the bullet until it goes off-screen
        while 0 <= self.x <= surface.get_width() and 0 <= self.y <= surface.get_height():
            self.move(angle, self.x, self.y)
            self.draw(surface)
            pygame.display.update()  # Update the display to show the bullet's movement


while True:
    dy/dx - 4 
