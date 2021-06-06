# Author: Thomas Fenaroli
# Date: 01/20/2021
# Purpose: Create the pong game

from cs1lib import *
from random import *

# assigns to global variable vy_sign, which determines positive or negative vy at start
vy_sign = 0


# determines vy_sign randomly
def determine_vy_sign():
    global vy_sign

    x = randint(1, 2)
    if x == 1:
        vy_sign = 1
    else:
        vy_sign = -1


# calls determine_vy_sign
determine_vy_sign()


# assign to global variables
W = 20
H = 80
x1 = 0
y1 = 0
x2 = 400 - W
y2 = 400 - H
cx = 200
cy = 200
vx = 4
vy = vy_sign * uniform(2, 5)
RADIUS = 10
PADDLE_MOVEMENT = 10
left_up = False
left_down = False
right_up = False
right_down = False


# sets background
def set_background():

    # background color
    set_clear_color(0, 0, 0)
    clear()
    set_fill_color(1, 1, 1)

    # draws middle circle
    draw_circle(200, 200, 50)
    set_fill_color(0, 0, 0)
    draw_circle(200, 200, 48)
    enable_stroke()
    set_stroke_color(1, 1, 1)

    # draws line
    draw_line(200, 0, 200, 400)
    disable_stroke()


# creates rectangles
def make_rectangle(x, y):
    global W, H

    set_fill_color(1, 0, 0)
    draw_rectangle(x, y, W, H)


# makes ball
def make_ball(x, y, r):

    set_fill_color(1, 1, 0)
    draw_circle(x, y, r)


# determines if there is paddle contact
def paddle_contact():
    global RADIUS, W, H, y1, y2, cx, cy, vx

    if cx + RADIUS > 400 - W and y2 < cy < y2 + H or cx - RADIUS < W and y1 < cy < y1 + H:
        return True


# determines if there is contact on ceiling or floor
def horizontal_contact():
    global RADIUS, cy

    if cy - RADIUS <= 0 or cy + RADIUS >= 400:
        return True


# determines key press
def press(key):
    global left_down, left_up, right_up, right_down, x1, y1, x2, y2, cx, cy, vy, vy_sign

    # moves left paddle
    if key.lower() == "a":
        left_up = True
    if key.lower() == "z":
        left_down = True

    # moves right paddle
    if key.lower() == "l":
        right_up = True
    if key.lower() == "m":
        right_down = True

    # resets game
    if key == " ":
        x1 = 0
        y1 = 0
        x2 = 400 - W
        y2 = 400 - H
        cx = 200
        cy = 200
        determine_vy_sign()
        vy = vy_sign * uniform(2, 5)

    # quits game
    if key.lower == "q":
        cs1_quit()


# determine key release
def release(key):
    global left_down, left_up, \
        right_up, right_down

    # stops left paddle
    if key.lower() == "a":
        left_up = False
    if key.lower() == "z":
        left_down = False

    # stops right paddle
    if key.lower() == "l":
        right_up = False
    if key.lower() == "m":
        right_down = False


# determines if there is wall contact
def game_over():
    global cx, RADIUS

    if cx - RADIUS <= 0 or cx + RADIUS >= 400:
        return True


# main draw function
def pong():
    global x1, y1, x2, y2, cx, cy, RADIUS, W, H, vx, vy, PADDLE_MOVEMENT, left_down, left_up, right_down, right_up

    set_background()

    make_rectangle(x1, y1)
    make_rectangle(x2, y2)

    make_ball(cx, cy, RADIUS)

    # moves ball
    cy += vy
    cx += vx

    # flips velocities for paddle and ceiling/floor contact
    if paddle_contact():
        vx = -vx
    if horizontal_contact():
        vy = -vy

    # controls left paddle
    if left_up and y1 > 0:
        y1 -= PADDLE_MOVEMENT
    if left_down and y1 < 400 - H:
        y1 += PADDLE_MOVEMENT

    # controls right paddle
    if right_up and y2 > 0:
        y2 -= PADDLE_MOVEMENT
    if right_down and y2 < 400 - H:
        y2 += PADDLE_MOVEMENT

    # quits game
    if game_over():
        cs1_quit()


start_graphics(pong, key_press=press, key_release=release)
