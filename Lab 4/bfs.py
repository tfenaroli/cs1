# Author: Thomas Fenaroli
# Date: 03/09/2021
# Purpose: Create a file with function breadth_first_search that takes start and end vertex as
# parameters and returns the shortest path

# imports files
from collections import *
from vertex import *

# defines function as described above
def breadth_first_search(start, goal):

    # assigns to local variables
    path = []
    backpointers = {start: None}
    queue = deque()
    queue.append(start)

    # while loop for executing search
    while len(queue) > 0:
        # assigns to current_vertex
        current_vertex = queue.popleft()

        # appends to queue and adds to backpointers dictionary
        for vertex in current_vertex.adj_list:
            if vertex not in backpointers:
                backpointers[vertex] = current_vertex
                queue.append(vertex)

        # if goal is reached, creates path through backchaining
        if current_vertex == goal:
            value = goal
            path.append(value)
            while value != start:
                value = backpointers[value]
                path.append(value)

            # returns path
            return path




