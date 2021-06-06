#Author: Thomas Fenaroli
#Date: 01/20/2021
#Purpose: Create the pong game (checkpoint)

from cs1lib import *

# assigns to global variables
W = 20
H = 80
X1 = 0
Y1 = 0
X2 = 400 - W
Y2 = 400 - H
PADDLE_MOVEMENT = 10
left_up = False
left_down = False
right_up = False
right_down = False


# sets background color
def set_background():

    # background color
    set_clear_color(0, 0, 0)
    clear()

    # center circle
    set_fill_color(1, 1, 1)
    draw_circle(200, 200, 50)
    set_fill_color(0, 0, 0)
    draw_circle(200, 200, 48)

    # center line
    enable_stroke()
    set_stroke_color(1, 1, 1)
    draw_line(200, 0, 200, 400)
    disable_stroke()


# creates rectangles
def make_rectangle(x, y):
    global W, H

    set_fill_color(1, 0, 0)
    draw_rectangle(x, y, W, H)


# takes key press
def press(key):
    global left_down, left_up, right_up, right_down, X1, Y1, X2, Y2

    # left paddle
    if key == "a":
        left_up = True
    if key == "z":
        left_down = True

    # right paddle
    if key == "l":
        right_up = True
    if key == "m":
        right_down = True


# takes key release
def release(key):
    global left_down, left_up, right_up, right_down

    # left paddle
    if key == "a":
        left_up = False
    if key == "z":
        left_down = False

    # right paddle
    if key == "l":
        right_up = False
    if key == "m":
        right_down = False


# main draw function
def pong():
    global X1, Y1, X2, Y2, W, H, PADDLE_MOVEMENT, left_down, left_up, right_down, right_up

    # calls set_background()
    set_background()

    # calls make_rectangle() for left and right paddles
    make_rectangle(X1, Y1)
    make_rectangle(X2, Y2)

    # controls left paddle
    if left_up and Y1 > 0:
        Y1 -= PADDLE_MOVEMENT
    if left_down and Y1 < 400 - H:
        Y1 += PADDLE_MOVEMENT

    # controls right paddle
    if right_up and Y2 > 0:
        Y2 -= PADDLE_MOVEMENT
    if right_down and Y2 < 400 - H:
        Y2 += PADDLE_MOVEMENT


# calls pong()
start_graphics(pong, key_press = press, key_release = release)