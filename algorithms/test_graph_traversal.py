import unittest

from algorithms.graph_traversal import Graph, djkstra_shortest_path


def graph_with_cycles():
    graph = Graph()
    graph.add_edge('A', 'B', 6)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('A', 'D', 1)
    graph.add_edge('D', 'B', 2)
    graph.add_edge('D', 'E', 1)
    graph.add_edge('B', 'E', 2)
    graph.add_edge('C', 'E', 5)
    return graph


class Test(unittest.TestCase):
    def test_djkstra_shortest_path(self):
        self.assertEqual(djkstra_shortest_path(graph_with_cycles(), 'A', 'B'), 3)
        pass
