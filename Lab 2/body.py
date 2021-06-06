# Author: Thomas Fenaroli
# Date: 02/15/2021
# Purpose: Create a body class for bodies in the model

from cs1lib import *

# creates body class
class Body:
    # initializes instance variables
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

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
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x * pixels_per_meter + cx, self.y * pixels_per_meter + cy, self.pixel_radius)
