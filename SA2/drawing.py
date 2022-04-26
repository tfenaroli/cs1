#Author: Thomas Fenaroli
#Date: 01/15/2021
#Purpose: Draw Monsters, Inc. picture book cover (Mike Wazowski)

from cs1lib import *

#makes background purple
def set_background_purple():
    set_clear_color(1, 0, 1)
    clear()

def draw_mike():

    set_background_purple()

    #draws Mike's body
    set_stroke_color(0, 0, 0)
    set_stroke_width(1)
    set_fill_color(0, 1, 0)
    draw_circle(200, 200, 100)

    #draws eye
    set_fill_color(1, 1, 1)
    draw_circle(200, 180, 40)
    set_fill_color(0, 0, 0)
    draw_circle(200, 190, 20)

    #draws mouth
    draw_line(175, 250, 225, 250)

    #draws legs
    set_stroke_width(20)
    set_stroke_color(0, 1, 0)
    draw_line(278, 278, 310, 310)
    draw_line(315, 320, 315, 360)
    draw_line(122, 278, 90, 310)
    draw_line(85, 320, 85, 360)

    #draws feet
    draw_line(85, 360, 60, 360)
    draw_line(315, 360, 340, 360)

    #draws arms
    draw_line(100, 225, 50, 250)
    draw_line(280, 225, 350, 150)

    #draws hands
    set_fill_color(0, 1, 0)
    draw_circle(50, 250, 10)
    draw_circle(350, 150, 10)

    #draws name
    set_stroke_color(0, 0, 0)
    draw_text("Thomas Fenaroli", 200, 50)

start_graphics(draw_mike)

