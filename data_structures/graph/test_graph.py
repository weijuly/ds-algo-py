import unittest

from data_structures.graph.graph import Graph


class TestDirectedAcyclicGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(directed=True, cyclic=False)
        self.graph.addEdge('A', 'C', 1)
        self.graph.addEdge('A', 'D', 2)
        self.graph.addEdge('B', 'D', 3)
        self.graph.addEdge('B', 'E', 2)
        self.graph.addEdge('D', 'F', 3)
        self.graph.addEdge('D', 'G', 4)
        self.graph.addEdge('G', 'I', 2)
        self.graph.addEdge('H', 'I', 3)

    def test_degree(self):
        self.assertEqual(self.graph.degree('Z'), 0)
        self.assertEqual(self.graph.degree('A'), 2)
        self.assertEqual(self.graph.degree('B'), 2)
        self.assertEqual(self.graph.degree('D'), 4)
        self.assertEqual(self.graph.degree('I'), 2)

    def test_adjacents(self):
        self.assertListEqual(self.graph.adjacents('Z'), [])
        self.assertListEqual(self.graph.adjacents('A'), [('C', 1), ('D', 2)])
        self.assertListEqual(self.graph.adjacents('B'), [('D', 3), ('E', 2)])
        self.assertListEqual(self.graph.adjacents('D'), [('A', 2), ('B', 3), ('F', 3), ('G', 4)])

    def test_topologicalSort(self):
        graph = Graph(directed=True, cyclic=False)
        graph.addEdge('5', '11', 1)
        graph.addEdge('7', '11', 1)
        graph.addEdge('7', '8', 1)
        graph.addEdge('3', '8', 1)
        graph.addEdge('3', '10', 1)
        graph.addEdge('11', '2', 1)
        graph.addEdge('11', '9', 1)
        graph.addEdge('11', '10', 1)
        graph.addEdge('8', '9', 1)
        ordered = graph.topologicalSort()
        self.assertTrue(ordered.index('5') < ordered.index('11'))
        self.assertTrue(ordered.index('7') < ordered.index('11'))
        self.assertTrue(ordered.index('3') < ordered.index('11'))
        self.assertTrue(ordered.index('5') < ordered.index('8'))
        self.assertTrue(ordered.index('7') < ordered.index('8'))
        self.assertTrue(ordered.index('3') < ordered.index('8'))
        self.assertTrue(ordered.index('11') < ordered.index('2'))
        self.assertTrue(ordered.index('11') < ordered.index('9'))
        self.assertTrue(ordered.index('11') < ordered.index('10'))
        self.assertTrue(ordered.index('8') < ordered.index('2'))
        self.assertTrue(ordered.index('8') < ordered.index('9'))
        self.assertTrue(ordered.index('8') < ordered.index('10'))


class TestNonDirectedAcyclicGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(directed=False, cyclic=False)
        self.graph.addEdge('A', 'C', 1)
        self.graph.addEdge('A', 'D', 2)
        self.graph.addEdge('B', 'D', 3)
        self.graph.addEdge('B', 'E', 2)
        self.graph.addEdge('D', 'F', 3)
        self.graph.addEdge('D', 'G', 4)
        self.graph.addEdge('G', 'I', 2)
        self.graph.addEdge('H', 'I', 3)

    def test_degree(self):
        self.assertEqual(self.graph.degree('Z'), 0)
        self.assertEqual(self.graph.degree('A'), 2)
        self.assertEqual(self.graph.degree('B'), 2)
        self.assertEqual(self.graph.degree('D'), 4)
        self.assertEqual(self.graph.degree('I'), 2)

    def test_adjacents(self):
        self.assertListEqual(self.graph.adjacents('Z'), [])
        self.assertListEqual(self.graph.adjacents('A'), [('C', 1), ('D', 2)])
        self.assertListEqual(self.graph.adjacents('B'), [('D', 3), ('E', 2)])
        self.assertListEqual(self.graph.adjacents('D'), [('A', 2), ('B', 3), ('F', 3), ('G', 4)])
