import pygame 
import math

class Plane():
    def __init__(self,x,y,sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.vel = 5
        self.rect = self.sprite.get_rect()
        self.last = "d"
        self.current_angle = 0


    def draw(self, surface):
        surface.blit(self.sprite,self.x,self.y)



    def move_left_joystick(self, left_joystick, surface):
        left_stick_x = left_joystick.get_axis(0)
        left_stick_y = left_joystick.get_axis(1)

        if abs(left_stick_x) > 0.1:
                self.x += left_stick_x * self.vel
        if abs(left_stick_y) > 0.1:
                self.y += left_stick_y * self.vel

        # Redraw the sprite on the surface
        rotated_sprite = pygame.transform.rotate(self.sprite, -self.current_angle)

        # Get the rect of the rotated sprite to keep its position
        rotated_rect = rotated_sprite.get_rect(center=(self.x, self.y))

        # Redraw the rotated sprite on the surface
        surface.blit(rotated_sprite, rotated_rect)

    def rotate_right_joystick(self,joystick1,value, surface):
        # Calculate the angle change based on joystick input
        angle_change = value * 7  # Adjust this value as needed for sensitivity

        # Update the current angle
        self.current_angle += angle_change

        # Ensure the angle stays within 0 to 360 degrees range
        self.current_angle %= 360

        # Rotate the sprite
        rotated_sprite = pygame.transform.rotate(self.sprite, -self.current_angle)

        # Get the rect of the rotated sprite to keep its position
        rotated_rect = rotated_sprite.get_rect(center=(self.x, self.y))

        # Redraw the rotated sprite on the surface
        surface.blit(rotated_sprite, rotated_rect)

        # Update the last rotation direction
        self.last = "d" if -45 <= self.current_angle <= 45 else "a"
        self.move_left_joystick(joystick1,surface)


    def draw_sprite(self, surface, angle=None):
        if angle is not None:
            rotated_sprite = pygame.transform.rotate(self.sprite, math.degrees(angle))
            surface.blit(rotated_sprite, (self.x, self.y))
        else:
            surface.blit(self.sprite, (self.x, self.y))
        self.rect.center = (self.x, self.y)




    def get_x(self):
        return(self.x)
    def get_y(self):
        return(self.y)
