import math

class Vertex:

    def __init__(self, name):
        self.name = name
        self.distance = math.inf

    def __repr__(self):
        return self.name

def initialize(graph):
    sorted_keys = sorted(graph.keys())
    start = sorted_keys[0]
    graph[start].distance = 0
    return sorted_keys

def bellman_ford(graph, adjacency):
    sorted_keys = initialize(graph)
    for key in sorted_keys:
        vertex = graph[key]
        for weight, neighbor in adjacency[vertex.name]:
            if vertex.distance + weight < neighbor.distance:
                neighbor.distance = vertex.distance + weight
