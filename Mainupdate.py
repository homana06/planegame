import pygame
from Sprite import *
import sys
from Map import *
from enemy import *

pygame.init()
pygame.joystick.init()
try:
    pygame.mixer.init()
except pygame.error:
    print("error line 8")



run = True
frame = 0
Blue = (0, 0, 255)
Black = (0, 0, 0)
backx = 0
backy = 0
running = True
screen = pygame.display.set_mode([900, 900])
pygame.display.set_caption("Zoomies")
try:
    pygame.mixer.music.load("Music/Brinstar.mp3")
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play(-1)
except pygame.error:
    print("Error loading or playing the music file.")
clock = pygame.time.Clock()

image = pygame.image.load("images/Jet.png")
player = Plane(450, 450, image)

background = TilingBackground(900, 900, 10, 10, 0.01)
EDGE_THRESHOLD = 5
SCROLL_SPEED = 2
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 900
gun = Bullet()
# ---------------movement--------------------------------------|||||||||||||||||||||||||||||||
keys = pygame.key.get_pressed()
num_joysticks = pygame.joystick.get_count()

if num_joysticks > 0:
    joysticks = []
    for i in range(num_joysticks):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        print(f"Initialized joystick {i + 1}: {joystick.get_name()}")
        joysticks.append(joystick)
else:
    joysticks = None
    print("No joystick available")

# Now you can access the initialized joysticks if they exist
if joysticks:
    joystick1 = joysticks[0]
    joystick2 = joysticks[1] if num_joysticks > 1 else None

# -----------------------------------------------------Run Loop----------------------------------------------------------------------------------------------------------------------------------

while running:  # main running loop
    keys = pygame.key.get_pressed()
    screen.fill(Black)
    player.rect.x = player.get_x()
    player.rect.y = player.get_y()
    player.angle = player.get_angle()
    background.draw(screen)
    player.draw_sprite(screen)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.JOYBUTTONDOWN:
            # Check if the right trigger is pressed
            if event.button == 7:
                player.shoot()
    if event.type == pygame.JOYAXISMOTION:
        # Check if joystick objects are initialized
        axis = event.axis
        value = event.value
        #print(axis, "---", value)
        if axis == 2 or axis == 3:
            player.rotate_right_joystick(joystick1, value, screen)
        elif axis == 0 or axis == 1:
            player.move_left_joystick(joystick1,value ,screen)
        elif axis == 5:
            #print("pew pew")
            print(player.angle)
            gun.move(player.angle,player.rect.x,player.rect.y,screen)

    if player.rect.x < EDGE_THRESHOLD:
        background.scroll(SCROLL_SPEED, 0)
    elif player.rect.x > SCREEN_WIDTH - EDGE_THRESHOLD:
        background.scroll(-SCROLL_SPEED, 0)
    if player.rect.y < EDGE_THRESHOLD:
        background.scroll(0, SCROLL_SPEED)
    elif player.rect.y > SCREEN_HEIGHT - EDGE_THRESHOLD:
        background.scroll(0, -SCROLL_SPEED)


    clock.tick(60)

    pygame.display.flip()
pygame.mixer.music.stop()
pygame.quit()
