from pygame import *
init()  # This is needed to initialise pygame

# Set up the screen 
screen = display.set_mode((800,600)) 

img_path = "/Users/mirjam/learning/python/flappy_bird/images/"
background_image = image.load(f"{img_path}bg.png")
screen.blit(background_image, (0,0))
display.update()

# Classes
# Bird Class
# Pipes Class
class Pipe():
    def __init__(self, x, y, direction) -> None:
        self.x = x
        self.y = y
        self.direction = direction
        self.rect = None

        up_img = image.load(f"{img_path}pipe.png")
        if self.direction == "up":
            self.img = up_img
        else:
            self.img = transform.flip(up_img, 0, 1)

    def move(self):
        left_speed = 5
        self.x = self.x - left_speed

    def blit(self):
        self.rect = screen.blit(self.img, (self.x, self.y))

# SETUP
# Pygame Setup
# Set up the bird
# Set up the pipes

# GAME TIME
# Waiting to play
# Moving Objects
# Game over
# Show the pics!