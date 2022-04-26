# Author: Thomas Fenaroli
# Date: 03/09/2021
# Purpose: Create a Vertex class that stores the vertex name, its adjacent vertices, and its text

# defines class as described above
class Vertex:
    # initializes instance variables
    def __init__(self, name, adj_vertices, text):
        self.name = name
        self.adj_vertices = adj_vertices
        self.text = text
