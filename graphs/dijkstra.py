import heapq
import math

class Vertex:

    def __init__(self, name):
        self.name = name
        self.distance = math.inf
        self.visited = False

def dijkstra(graph, start):
    start.distance = 0
    heapq.heapify([(start.distance, start)])
    while queue:
        vertex = heapq.heappop(queue)[1]
        vertex.visited = True
        for weight, neighbor in graph[vertex.name]:
            if not neighbor.visited:
                if vertex.distance + weight < neighbor.distance:
                    neighbor.distance = vertex.distance + weight
                heapq.heappush(queue, (neighbor.distance, neighbor))
