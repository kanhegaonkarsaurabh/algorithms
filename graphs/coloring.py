def greedy_coloring(graph):
    colors = [1]
    chromatic = {vertex: None for vertex in graph.keys()}
    for vertex in graph.keys():
        for color in colors:
            used = False
            for neighbor in graph[vertex]:
                if chromatic[neighbor] == color:
                    used = True
            if not used:
                chromatic[vertex] = color
                break
        if chromatic[vertex] is None:
            colors.append(colors[-1] + 1)
            chromatic[vertex] = colors[-1]
    return chromatic
