# Author: Thomas Fenaroli
# Date: 02/25/2021
# Purpose: Create graphic that depicts locations of cities with largest populations in decreasing
# order

# imports files
from cs1lib import *

# loads image
world_map = load_image("worldec.png")

# opens cities_population.txt
cities_population = open("cities_population.txt", "r")

# assigns to global variables
N = 50
cities = []
for line in cities_population:
    line.strip()
    split_city = line.split(",")
    cities.append([split_city[0], int(split_city[1]), float(split_city[2]), float(split_city[3])])
CX = 720
CY = 360
FRAME_RATE = 5
frame_count = 0

# draws graphic
def draw():
    global frame_count

    set_fill_color(1, 0, 0)
    draw_image(world_map, 0, 0)
    set_stroke_color(1, 0, 0)
    set_font_size(8)

    # draws circles accordingly
    for city_number in range(frame_count):
        x = 4 * cities[city_number][3]
        y = 4 * cities[city_number][2]
        draw_text(cities[city_number][0], CX + x, CY - y)

    # increments frame count if under the number
    if frame_count < N:
        frame_count += 1

# closes cities_population.txt
cities_population.close()

# starts graphic
start_graphics(draw, width=2*CX, height=2*CY, framerate=FRAME_RATE)