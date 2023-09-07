import sys


class DirectedGraph:
    def __init__(self):
        self._edges = {}
        self._nodes = set()

    def add(self, source=None, target=None, weight=1):
        if source is None or target is None:
            return
        self._edges[(source, target)] = weight
        self._nodes.add(source)
        self._nodes.add(target)
        return self

    def nodes(self):
        return list(self._nodes)

    def edges(self):
        return self._edges


def bellman_ford_only_for_non_cyclic(graph, source):
    distances = {source: 0}
    for i in range(1, len(graph.edges())):
        stack = [[x[1], graph.edges()[x]] for x in graph.edges() if x[0] == source]
        visited = []
        while stack:
            node, weight = stack.pop(0)
            if node in visited and weight > distances[node]:
                continue
            visited.append(node)
            if node not in distances:
                distances[node] = sys.maxsize
            if weight < distances[node]:
                distances[node] = weight
            stack.extend([[x[1], graph.edges()[x] + weight] for x in graph.edges() if x[0] == node])
        print(distances)


def relax(graph, distances):
    for edge, w in graph.edges().items():
        x, y = edge
        if distances[x] != sys.maxsize and distances[x] + w < distances[y]:
            distances[y] = distances[x] + w
    return distances


def bellman_ford(graph, source):
    distances = {x: sys.maxsize for x in graph.nodes()}
    distances[source] = 0
    for _ in range(1, len(graph.edges())):
        distances = relax(graph, distances)
    negative_cycle = distances != relax(graph, distances.copy())
    return distances, negative_cycle


graph = DirectedGraph()
graph.add('1', '2', 6)
graph.add('1', '3', 5)
graph.add('3', '2', -2)
graph.add('2', '4', -1)
graph.add('3', '4', 4)
graph.add('4', '5', 3)
graph.add('3', '5', 3)
print(bellman_ford(graph, '1'))

graph = DirectedGraph()
graph.add('A', 'B', 5)
graph.add('B', 'C', 1)
graph.add('B', 'D', 2)
graph.add('D', 'F', 2)
graph.add('F', 'E', -3)
graph.add('E', 'D', -1)
graph.add('C', 'E', 1)
print(bellman_ford(graph, 'A'))
