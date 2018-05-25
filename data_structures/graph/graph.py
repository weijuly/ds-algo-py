import sys


class Graph:

    def __init__(self, directed=True, cyclic=False):
        self.directed, self.cyclic = directed, cyclic
        self.graph = {}

    def addEdge(self, source, target, weight=1):
        if not source or not target:
            return
        key = (source, target)
        if key in self.graph:
            return
        self.graph[key] = weight
        if not self.directed:
            key = (target, source)
            self.graph[key] = weight

    def degree(self, vertex):
        if self.directed:
            return sum([1 for k in self.graph.keys() if k[0] == vertex or k[1] == vertex])
        return sum([1 for k in self.graph.keys() if k[0] == vertex])

    def adjacents(self, vertex):
        incoming = [(k[1], self.graph[k]) for k in self.graph.keys() if k[0] == vertex]
        outgoing = [(k[0], self.graph[k]) for k in self.graph.keys() if k[1] == vertex] if self.directed else []
        return sorted(incoming + outgoing)

    def shortestPath(self, source, target):
        if self.directed:
            if source not in [k[0] for k in self.graph.keys()]:
                return sys.maxsize
            if target not in [k[1] for k in self.graph.keys()]:
                return sys.maxsize
        else:
            if source not in [k[0] for k in self.graph.keys()] or target not in [k[0] for k in self.graph.keys()]:
                return sys.maxsize
        if self.directed:
            distances = {k[0]: sys.maxsize for k in self.graph.keys()}
            distances[source] = 0
            current = source
            distances.pop(source)

