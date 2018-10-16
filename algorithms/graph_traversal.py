import sys


class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, source, target, weight=1):
        self.graph[(source, target)] = weight
        self.graph[(target, source)] = weight

    def nodes(self):
        sources = [x[0] for x in self.graph]
        targets = [x[1] for x in self.graph]
        return list(set(sources + targets))

    def edges(self):
        return self.graph


def djkstra_shortest_path(graph, source, target):
    distances = {}
    for edge in graph.edges():
        distances[edge[0]] = sys.maxsize
        distances[edge[1]] = sys.maxsize
    visited, pending = [], list(distances.keys())
    runner = source
    distances[runner] = 0
    min_dist = 0
    while pending:
        for edge in [x for x in graph.edges() if x[0] == runner]:
            if min_dist + graph.graph[edge] < distances[edge[1]]:
                distances[edge[1]] = min_dist + graph.graph[edge]
        visited.append(runner)
        pending.remove(runner)
        if pending:
            min_dist = min([distances[x] for x in pending if distances[x] != 0])
            runner = [x for x in distances if distances[x] == min_dist][0]
    return distances[target]
