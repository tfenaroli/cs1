# Author: Thomas Fenaroli
# Date: 03/08/21
# Purpose: Create a function load_graph that creates a dictionary containing the references to each vertex object
# and appends to the adjacency list of each vertex object the references of adjacent vertices

# imports Vertex class
from vertex import *

# defines function as described above
def load_graph(file_name):
    # assigns to list and dictionary
    dart_list = []
    dict = {}

    # reads file_name and appends to dart_list each line of the file
    dart_graph = open(file_name, "r")
    for line in dart_graph:
        dart_list.append(line)
    dart_graph.close()

    # creates a dictionary for each line that contains reference to vertex object as value
    for line in dart_list:
        stripped_line = line.strip()
        split_line = stripped_line.split(";")
        split_coordinates = split_line[-1].split(",")
        x = split_coordinates[0].strip()
        y = split_coordinates[1].strip()
        dict[split_line[0]] = Vertex(split_line[0], x, y)

    # appends to each vertex' adjacency list references to adjacent vertices
    for line in dart_list:
        stripped_line = line.strip()
        split_line = stripped_line.split(";")
        split_adjacents = split_line[1].split(",")
        for location in split_adjacents:
            adjacent = location.strip()
            dict[split_line[0]].adj_list.append(dict[adjacent])

    # returns the dictionary
    return dict
