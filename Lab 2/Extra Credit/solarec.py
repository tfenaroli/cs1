# Author: Thomas Fenaroli
# Date: 02/20/2021
# Purpose: Create an extra credit model of the solar system

from cs1lib import *
from random import *
from systemec import System
from bodyec import Body

# loads image
space = load_image("spacefinal.jpg")

# global constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 3.0e6
PIXELS_PER_METER = 7/1e10

FRAMERATE = 30
TIMESTEP = 1.0 / FRAMERATE

# adds planet randomly
def key_press(value):
    global solar_system
    if value == "a":
        solar_system.body_list.append(Body(2.0e24, randint(-225e9, -100e9), 0, 0, randint(2e4, 4e4), "moonfinal.png", 5))

# creates solar system model
def model():
    draw_image(space, 0, 0)

    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)
    solar_system.update(TIMESTEP * TIME_SCALE)

# creates body objects
sun = Body(1.98892e30, 0, 0, 0, 0, "sunfinal.png", 20)
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, "mercuryfinal.png", 3)
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, "venusfinal.png", 7)
earth = Body(5.97e24, -149.6e9, 0, 0, 29790, "earthfinal.png", 8)
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, "marsfinal.png", 6)

# creates system object
solar_system = System([sun, mercury, venus, earth, mars])

# starts graphics
start_graphics(model, 2400, framerate=FRAMERATE, key_press=key_press)