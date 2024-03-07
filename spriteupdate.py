import pygame
import math
from bullet import *



class Plane():
    def __init__(self,x,y,sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.vel = 5
        self.rect = self.sprite.get_rect()
        self.last = "d"
        self.current_angle = 0




    def move_left_joystick(self, left_joystick,value, surface):
        left_stick_x = left_joystick.get_axis(0)
        left_stick_y = left_joystick.get_axis(1)
        if abs(left_stick_x) > 0.1:
            self.x += left_stick_x * self.vel
        if abs(left_stick_y) > 0.1:
            self.y += left_stick_y * self.vel
        self.draw_sprite(surface)
        


    def rotate_right_joystick(self, joystick1, value, surface):
        # Adjust angle change based on the value of the joystick
        angle_change = value * -0.1  # Inverted and slowed down rotation
        self.current_angle += angle_change
        self.current_angle %= 360
        self.draw_sprite(surface)
        self.last = "d" if -45 <= self.current_angle <= 45 else "a"
        self.move_left_joystick(joystick1,value ,surface)


    def draw_sprite(self, surface):
        if self.current_angle is not None:
            rotated_sprite = pygame.transform.rotate(self.sprite, math.degrees(self.current_angle))
            rotated_rect = rotated_sprite.get_rect(center=self.rect.center)  # Get the rect of rotated sprite
            surface.blit(rotated_sprite, rotated_rect.topleft)  # Blit using the top-left corner of the rotated rect
        else:
            surface.blit(self.sprite, self.rect)  # Blit using the rect of the sprite

    def shoot(self):
        bullet = Bullet(self.x, self.y, self.current_angle)
        self.bullets.append(bullet)


    def get_x(self):
        return(self.x)
    def get_y(self):
        return(self.y)
    def get_angle(self):
        return(self.current_angle)
