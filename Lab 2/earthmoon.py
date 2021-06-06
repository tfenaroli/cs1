# Author: *TEST CODE FOR EARTH-MOON SYSTEM*
# Date: 02/15/2021
# Purpose: To create graphics window with Earth and moon. Since it is the checkpoint, Earth will be stationary and
# moon will accelerate non-centripetally

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 100000         # real seconds per simulation second
PIXELS_PER_METER = 3 / 1e7  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    earth_moon.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    earth_moon.update(TIMESTEP * TIME_SCALE)

# gave moon slight negative vx to emulate elliptical orbit
earth = Body(5.9736e24, 0, 0, 0, 0, 24, 0, 0, 1)            # blue earth
moon = Body(7.3477e22, 3.84403e8, 0, -500, 1022, 4, 1, 1, 1)   # white moon
earth_moon = System([earth, moon])

start_graphics(main, 2400, framerate=FRAMERATE)