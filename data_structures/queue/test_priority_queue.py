import unittest

from data_structures.queue.priority_queue import PriorityQueue


class Test(unittest.TestCase):

    def test_priority_queue(self):
        pq = PriorityQueue()
        pq.enqueue(10, 'Tony Stark')
        pq.enqueue(8, 'Peter Parker')
        pq.enqueue(9, 'Natasha Romanoff')
        pq.enqueue(10, 'Maria Hill')
        pq.enqueue(10, 'Nick Fury')
        pq.enqueue(8, 'Bruce Banner')
        pq.enqueue(8, 'Peter Quill')
        pq.enqueue(9, 'Thor Odinson')
        pq.enqueue(9, 'Pepper Potts')
        pq.enqueue(11, 'Wanda Maximoff')

        self.assertEqual('Wanda Maximoff', pq.dequeue())
        self.assertEqual('Tony Stark', pq.dequeue())
        self.assertEqual('Maria Hill', pq.dequeue())
        self.assertEqual('Nick Fury', pq.dequeue())
        self.assertEqual('Natasha Romanoff', pq.dequeue())
        self.assertEqual('Thor Odinson', pq.dequeue())
        self.assertEqual('Pepper Potts', pq.dequeue())
        self.assertEqual('Peter Parker', pq.dequeue())
        self.assertEqual('Bruce Banner', pq.dequeue())
        self.assertEqual('Peter Quill', pq.dequeue())
