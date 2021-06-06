# Author: Thomas Fenaroli
# Date: 02/15/2021
# Purpose: Create a system class for a group of body objects in the model

#questions: G constant,

from body import Body
from math import *

G = 6.67384e-11

# creates system class
class System:
    # initializes instance variables
    def __init__(self, body_list):
        self.body_list = body_list

    # computes acceleration
    def compute_acceleration(self, n):

        ax_total = 0
        ay_total = 0

        for planet in self.body_list:
            if planet == self.body_list[n]:
                pass

            else:
                dx = planet.x - self.body_list[n].x
                dy = planet.y - self.body_list[n].y
                a = (G * planet.mass) / (dx**2 + dy**2)

                ax = (a * dx) / sqrt(dx**2 + dy**2)
                ay = (a * dy) / sqrt(dx**2 + dy**2)

                ax_total += ax
                ay_total += ay

        return ax_total, ay_total

    # updates the positions and velocities of body objects
    def update(self, timestep):
        for body in self.body_list:
            body.update_position(timestep)

        for index in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(index)
            self.body_list[index].update_velocity(ax, ay, timestep)

    # draws body objects
    def draw(self, cx, cy, pixels_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)
