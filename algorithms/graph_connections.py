import random
import time

'''
Given a list of sets in the format:
[
    (a, b),
    (c, d),
    (e, f)
]
where (a, b) represents the connection from node[a] <=> node[b], check if there's a connection between any two nodes
'''


class Graph01:
    """
    Using the approach of storing data element like this:
    {
        a: 1
        b: 1
        c: 2
        d: 2
        e: 1
        f: 1
    }
    description:
        a and b are connected because they have same index
        b and c are not connected because they don't have a different index
    pros:
        fast lookup
    cons:
        slow insertion due to re-evaluation of existing connections
    timings:
        ~ 2.4 secs for adding 10k edges ( timeout for 100k )
        ~ 0 secs for checking 10k edges
    """

    def __init__(self):
        self.graph = {}
        self.index = 0
        pass

    def reorganize(self, x, y):
        index = self.graph[x]
        other = self.graph.get(y, -1)
        if other == -1:
            self.graph[y] = index
        else:
            for z in self.graph:
                if self.graph[z] == other:
                    self.graph[z] = index

    def connect(self, x, y):
        if x in self.graph:
            self.reorganize(x, y)
        elif y in self.graph:
            self.reorganize(y, x)
        else:
            self.graph[x], self.graph[y] = self.index, self.index
            self.index += 1

    def connected(self, x, y):
        return self.graph.get(x, -1) == self.graph.get(y, -2)


class Graph02:
    """
    Using the approach of storing data element like this:
    {
        1: [a, b, c, d, e, f]
        2: [g, h, i, j]
    }
    description:
        a and b are connected because they are in same set
        b and g are not connected because they are in different set
    pros:
        single lookup map
    cons:
        slower lookup
    timings:
        ~ 1.1 secs for adding 10k edges ( timeout for 100k )
        ~ 0.5 for checking 10k edges
    """

    def __init__(self):
        self.index = 0
        self.graph = {}

    def connect(self, x, y):
        for index in self.graph:
            if x in self.graph[index]:
                self.graph[index].add(y)
                break
            if y in self.graph[index]:
                self.graph[index].add(x)
                break
        else:
            self.graph[self.index] = {x, y}
            self.index += 1

    def connected(self, x, y):
        for index in self.graph:
            if x in self.graph[index] and y in self.graph[index]:
                return True
        else:
            return False


class Graph03:
    """
        Store a lookup of both elements and indexes
        elements_to_index : { a: 1, b: 1, c: 2, d: 2 }
        index_to_elements : { 1: [a, b], 2: [c, d] }

        pros:
            fast
        cons:
            two lookup maps
        performance:
            ~6 secs for adding 1M edges
            ~0.6 secs for checking 1M edges
    """

    def __init__(self):
        self.index_to_elements = {}
        self.elements_to_index = {}
        self.index = 0

    def add(self, index, y):
        other = self.elements_to_index.get(y, -1)
        if other == -1:
            self.elements_to_index[y] = index
            self.index_to_elements[index].add(y)
        else:
            for k in self.index_to_elements[other]:
                self.elements_to_index[k] = index
            self.index_to_elements[index].update(self.index_to_elements[other])
            self.index_to_elements[other] = set()

    def connect(self, x, y):
        if x in self.elements_to_index:
            self.add(self.elements_to_index[x], y)
        elif y in self.elements_to_index:
            self.add(self.elements_to_index[y], x)
        else:
            self.elements_to_index[x] = self.elements_to_index[y] = self.index
            self.index_to_elements[self.index] = {x, y}
            self.index += 1

    def connected(self, x, y):
        return self.elements_to_index.get(x, -1) == self.elements_to_index.get(y, -2)


class Graph04:
    '''
    Store the elements in a map including reverse lookup:
    {
        x: [a, b, c]
        a: [x, b, c]
        c: [x, a, b]
    }
    performance:
        ~1.5 secs for adding 1M edges
        ~11.5 secs for checking 1M edges
    '''
    def __init__(self):
        self.graph = {}

    def connect(self, x, y):
        if x not in self.graph:
            self.graph[x] = []
        self.graph[x].append(y)
        if y not in self.graph:
            self.graph[y] = []
        self.graph[y].append(x)

    def _connected(self, x, y, exclusions):
        if x not in self.graph:
            return False
        if y in self.graph[x]:
            return True
        for c in [e for e in self.graph[x] if e not in exclusions]:
            return self._connected(c, y, exclusions + [x])
        return False

    def connected(self, x, y):
        return self._connected(x, y, [])


DATA_SIZE = 1000000

graph = Graph03()
edges = [[random.randint(1, DATA_SIZE), random.randint(1, DATA_SIZE)] for x in range(DATA_SIZE)]
start = time.perf_counter()
for edge in edges:
    graph.connect(edge[0], edge[1])
end = time.perf_counter()
print('Time for connect is %f secs' % (end - start))

edges = [[random.randint(1, DATA_SIZE), random.randint(1, DATA_SIZE)] for x in range(DATA_SIZE)]
start = time.perf_counter()
for edge in edges:
    graph.connected(edge[0], edge[1])
end = time.perf_counter()
print('Time for check is %f secs' % (end - start))
