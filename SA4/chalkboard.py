#Author: Thomas Fenaroli
#Date: 01/19/2021
#Purpose: Create a chalkboard that allows you to change the color of your marker

from cs1lib import *

#global variables
i = 0
old_x = 0
old_y = 0
x = 0
y = 0
draw = False

#starts drawing upon press
def press(mx, my):
    global draw
    draw = True

#continues drawing/not drawing upon move
def move(mx, my):
    global x, y
    x = mx
    y = my

#stops drawing upon release
def release(mx, my):
    global draw
    draw = False

#changes brush color
def key_press(value):
    # changes marker color
    if value == "r":
        set_stroke_color(1, 0, 0)
    elif value == "g":
        set_stroke_color(0, 1, 0)
    elif value == "b":
        set_stroke_color(0, 0, 1)
    elif value == "y":
        set_stroke_color(1, 1,0)

#sets background and stroke colors
def background():
    set_clear_color(0, 0, 0)
    clear()
    set_stroke_color(1, 1, 1)
    set_stroke_width(2)

def chalkboard():
    global old_x, old_y, x, y, i, draw

    #calls background function only once
    if i == 0:
        background()
        i += 1

    #draws
    if draw:
        draw_line(old_x, old_y, x, y)

    #updates old coordinates to new ones
    old_x = x
    old_y = y

#opens window and starts graphic
start_graphics(chalkboard, mouse_move=move, mouse_press=press, mouse_release=release, key_press=key_press)