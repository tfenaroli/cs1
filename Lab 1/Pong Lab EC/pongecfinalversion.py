# Author: Thomas Fenaroli
# Date: 01/20/2021
# Purpose: Create the pong game with extra credit features

from cs1lib import *
from random import *


# assigns to global variable vx_sign, which determines positive or negative vx at start
vx_sign = 0


# determines vx_sign randomly
def determine_vx_sign():
    global vx_sign

    x = randint(1, 2)
    if x == 1:
        vx_sign = 1
    else:
        vx_sign = -1


# calls determine_vx_sign
determine_vx_sign()


# assign to global variables
W = 20
H = 80
x1 = 0
y1 = 0
x2 = 400 - W
y2 = 400 - H
cx = 200
cy = 200
vx = vx_sign * uniform(2, 5)
vy = uniform(-5, 5)
RADIUS = 10
PADDLE_MOVEMENT = 10
left_up = False
left_down = False
right_up = False
right_down = False
ball_color_r = uniform(0, 1)
ball_color_g = uniform(0, 1)
ball_color_b = uniform(0, 1)


# loads images
atari = load_image("atarilogo.png")
atariball = load_image("atariballlogo.png")
backgroundimg = load_image("pongbackground.png")


# sets background color
def set_background():

    set_clear_color(0.1, 0.3, 0.1)
    clear()
    set_fill_color(1, 1, 1)


# creates rectangles
def make_rectangle(x, y):
    global W, H

    set_fill_color(1, 0, 0)
    draw_rectangle(x, y, W, H)


# makes ball
def make_ball(x, y, r):
    global ball_color_r, ball_color_g, ball_color_b

    # creates random color for ball if paddle_contact
    if paddle_contact():
        ball_color_r = uniform(0, 1)
        ball_color_g = uniform(0, 1)
        ball_color_b = uniform(0, 1)

    set_fill_color(ball_color_r, ball_color_g, ball_color_b)

    # draws circle
    draw_circle(x, y, r)


# determines if there is paddle_contact
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
    global left_down, left_up, right_up, right_down, x1, y1, x2, y2, cx, cy, vx, vy, vx_sign

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
        determine_vx_sign()
        vx = vx_sign * uniform(2, 5)
        vy = uniform(-5, 5)

    # quits game
    if key.lower() == "q":
        cs1_quit()


# determines key release
def release(key):
    global left_down, left_up, right_up, right_down

    # stops moving left paddle
    if key.lower() == "a":
        left_up = False
    if key.lower() == "z":
        left_down = False

    # stops moving right paddle
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
    global x1, y1, x2, y2, cx, cy, RADIUS, W, H, vx, vy, PADDLE_MOVEMENT, left_down, left_up, right_down, right_up, \
        atari, atariball, backgroundimg

    set_background()

    draw_image(backgroundimg, 0, 0)

    make_rectangle(x1, y1)
    make_rectangle(x2, y2)

    draw_image(atari, x1, y1)
    draw_image(atari, x2, y2)

    make_ball(cx, cy, RADIUS)
    draw_image(atariball, cx - RADIUS / 1.5, cy - RADIUS / 1.5)

    # moves ball
    cy += vy
    cx += vx

    # flips velocities for paddle and ceiling/floor contact
    if paddle_contact():
        vx = -vx
        vy = uniform(-5, 5)
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
