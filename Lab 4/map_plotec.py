# imports files
from cs1lib import *
from load_graph import *
from bfs import *

# assigns to global variables
map = load_image("dartmouth_map.png")
vertex_dict = load_graph("dartmouth_graph.txt")
x = 0
y = 0
start_vertex = None
goal_vertex = None
is_pressed = False


# updates global x and y values according to mouse location
def move(mx, my):
    global x, y
    x = mx
    y = my


# changes is_pressed to True
def press(mx, my):
    global is_pressed
    is_pressed = True


# changes is_pressed to False
def release(mx, my):
    global is_pressed
    is_pressed = False


# draws map, vertices, and edges
def draw_map():
    global start_vertex, goal_vertex, is_pressed

    # draws image
    draw_image(map, 0, 0)

    # sets font size
    set_font_size(15)

    # for every vertex, draws vertex and edges accordingly (in different color if start or goal vertex)
    for vertex in vertex_dict:

        # draws adjacent edges
        vertex_dict[vertex].draw_adjacent_edges(0, 0, 1)

        # draws and assigns to start_vertex
        if vertex_dict[vertex].is_on_vertex(x, y) and is_pressed or start_vertex == vertex_dict[vertex]:
            start_vertex = vertex_dict[vertex]
            vertex_dict[vertex].draw_vertex(1, 0, 0)
            enable_stroke()
            draw_text(vertex_dict[vertex].name, vertex_dict[vertex].x, vertex_dict[vertex].y - 20)

        # draws and assigns to goal_vertex
        elif start_vertex != None and not is_pressed and vertex_dict[vertex].is_on_vertex(x, y):
            goal_vertex = vertex_dict[vertex]
            vertex_dict[vertex].draw_vertex(1, 0, 0)
            enable_stroke()
            draw_text(vertex_dict[vertex].name, vertex_dict[vertex].x, vertex_dict[vertex].y - 20)

        # draws normal vertices
        else:
            vertex_dict[vertex].draw_vertex(0, 0, 1)

    # determines and draws path
    if start_vertex != None and goal_vertex != None:

        final_path = breadth_first_search(start_vertex, goal_vertex)

        # draws vertices in final_path
        for vertex in final_path:
            vertex.draw_vertex(1, 0, 0)

        # draws edges in final_path
        for index in range(len(final_path) - 1):
            final_path[index].draw_edge(final_path[index + 1], 1, 0, 0)


# starts graphics
start_graphics(draw_map, width=1012, height=811, mouse_move=move, mouse_press=press, mouse_release=release)