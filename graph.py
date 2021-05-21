# This is our Markov Chain representation
import random

# define the graph in terms of vertices

class Vertex:
    def __init__(self, value): # value will be the word
        self.value = value
        self.adjacent = {} # nodes that have an edge from this vertex
        self.neighbors = []
        self.neighbors_weights = []

    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        # this is incrementing the weight of the edge
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        # randomly select next word ***Based on weights!
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]

# have our vertex representation, put this together in a graph

class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        # return all possible words
        return set(self.vertices.keys())
    
    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        # what if the value isn't in the graph?
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value] # get the Vertex object

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()



