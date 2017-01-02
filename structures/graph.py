class Vertex:

    def __init__(self, name):
        self.name = name
        self.distance = 0
        self.visited = False

    def __repr__(self):
        return self.name

class Edge:

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.weight = 0.0

class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        self.graph[v.name] = []

    def add_edge(self, v1, v2):
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.graph[v1.name].append(v2)
        self.graph[v2.name].append(v1)

    def get_neighbors(self, v):
        return self.graph[v.name]
