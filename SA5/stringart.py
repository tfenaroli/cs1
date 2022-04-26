# Author: Thomas Fenaroli
# Date: 02/07/2021
# Purpose: Create a function that takes 9 parameters and
# draws string art based on the parameters, which describe the coordinates of each end point of the two
# sticks and the number of strings

from cs1lib import *


# draws string art in separate window once called in the main() function
def draw_string_art(x1a, y1a, x2a, y2a, x1b, y1b, x2b, y2b, n):

    set_stroke_width(3)
    set_stroke_color(1, 0, 0)

    draw_line(x1a, y1a, x2a, y2a)
    draw_line(x1b, y1b, x2b, y2b)

    set_stroke_width(1)

    lines_drawn = 0
    f = 0

    while lines_drawn < n:
        set_stroke_color(0, f, 1)
        draw_line(x1a + f * (x2a - x1a), y1a + f * (y2a - y1a), x2b + f * (x1b - x2b), y2b + f * (y1b - y2b))

        f += 1 / (n - 1)
        lines_drawn += 1


# calls draw_string_art() to draw the string art
def main():
    set_clear_color(0, 0, 0)
    clear()

    draw_string_art(80, 180, 120, 280, 320, 130, 370, 390, 18)


# calls start_graphics to draw the string art
start_graphics(main)
