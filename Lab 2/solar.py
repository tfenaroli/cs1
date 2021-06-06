# Author: Thomas Fenaroli
# Date: 02/19/2021
# Purpose: Create an accurate model of the solar system

from cs1lib import *
from system import System
from body import Body

# global constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 3.0e6
PIXELS_PER_METER = 7/1e10

FRAMERATE = 30
TIMESTEP = 1.0 / FRAMERATE

# creates solar system model
def model():

    set_clear_color(0, 0, 0)
    clear()

    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)
    solar_system.update(TIMESTEP * TIME_SCALE)

# creates body objects
sun = Body(1.98892e30, 0, 0, 0, 0, 20, 1, 1, 0)
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 4, 0.7, 0.3, 0)
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 7, 0.6, 0.4, 0.6)
earth = Body(5.97e24, -149.6e9, 0, 0, 29790, 8, 0, 0, 1)
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 6, 1, 0, 0)

# creates system object
solar_system = System([sun, mercury, venus, earth, mars])

# starts graphics
start_graphics(model, 2400, framerate=FRAMERATE)