# Author: Thomas Fenaroli
# Date: 03/08/21
# Purpose: Create a vertex class that stores name, coordinates, and adjacent vertices

# imports files
from cs1lib import *

# assigns to global constants
VERTEX_RADIUS = 8
EDGE_WIDTH = 4

# creates class as described above
class Vertex:
    # initializes instance variables
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adj_list = []
        self.distance = None

    # draws vertex
    def draw_vertex(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, VERTEX_RADIUS)

    # draws edge
    def draw_edge(self, vertex_obj, r, g, b):
        enable_stroke()
        set_stroke_width(EDGE_WIDTH)
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, vertex_obj.x, vertex_obj.y)

    # draws adjacent edges
    def draw_adjacent_edges(self, r, g, b):
        for vertex in self.adj_list:
            self.draw_edge(vertex, r, g, b)

    # determines if mouse is on a vertex
    def is_on_vertex(self, x, y):
        if self.x - VERTEX_RADIUS <= x <= self.x + VERTEX_RADIUS and self.y - \
                VERTEX_RADIUS <= y <= self.y + VERTEX_RADIUS:
            return True
        else:
            return False

    # returns string according to instructions
    def __str__(self):
        adjacent_vertex_names = self.adj_list[0].name
        for vertex in self.adj_list:
            if vertex != self.adj_list[0]:
                adjacent_vertex_names += ", " + vertex.name

        return self.name + "; " + "Location: " + str(self.x) + ", " + str(self.y) \
               + "; Adjacent vertices: " + adjacent_vertex_names
