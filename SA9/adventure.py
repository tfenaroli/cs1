# Author: Thomas Fenaroli (partly instruction code)
# Date: 03/09/2021
# Purpose: Finish a file that parses lines in an external story.txt file, loads a story, and
# plays the story

from vertex import *

def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


def load_story(filename):

    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

            #print("vertex " + vertex_name)
            #print(" adjacent:  " + str(adjacent_vertices))
            #print(" text:  " + text)

            # YOU WRITE THIS PART
            # create a graph vertex here and add it to the dictionary
            vertex_dict[vertex_name] = Vertex(vertex_name, adjacent_vertices, text)

    file.close()

    return vertex_dict

# plays the game while playing is True
def play(vertex_dict):
    # assigns True to playing
    playing = True

    # assigns "START" vertex to current_vertex
    current_vertex = vertex_dict["START"]

    # plays the game
    while playing:
        print(current_vertex.text)
        # determines if there are remaining items in adj_vertices and acts accordingly
        if len(current_vertex.adj_vertices) > 0:
            choice = ord(input("Your choice: ").lower()) - ord("a")
            while not 0 <= choice <= len(current_vertex.adj_vertices) - 1:
                print("Invalid input")
                choice = ord(input("Your choice: ").lower()) - ord("a")
            current_vertex = vertex_dict[current_vertex.adj_vertices[choice]]
        else:
            playing = False

# calls play and load_story for the file "story.txt"
play(load_story("story.txt"))

