# Author: Thomas Fenaroli
# Date: 02/20/2021
# Purpose: Create an extra credit body class for bodies in the model

from cs1lib import *


# creates body class
class Body:
    # initializes instance variables
    def __init__(self, mass, x, y, vx, vy, file_name, image_radius):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image = load_image(file_name)
        self.image_radius = image_radius


    # updates position of body
    def update_position(self, timestep):
        self.x += self.vx * timestep
        self.y += self.vy * timestep

    # updates velocity of body
    def update_velocity(self, ax, ay, timestep):
        self.vx += ax * timestep
        self.vy += ay * timestep

    # draws body
    def draw(self, cx, cy, pixels_per_meter):
        draw_image(self.image, self.x * pixels_per_meter + cx - self.image_radius, self.y * pixels_per_meter + cy - self.image_radius)
