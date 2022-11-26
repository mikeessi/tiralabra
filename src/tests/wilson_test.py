import unittest
from algorithms.wilson import Wilson

class TestWilson(unittest.TestCase):
    def setUp(self):
        self.wilson = Wilson(10)

    def test_constructor_creates_correct_amount_of_nodes(self):
        self.assertEqual(len(self.wilson.nodes),100)

    def test_constructor_creates_correct_amount_of_edges(self):
        amount = 0
        for node, edges in self.wilson.edges.items():
            amount += len(edges)
        self.assertEqual(amount, 360)

    def test_neighbors_corner_node(self):
        amount = len(self.wilson.neighbors((0,0)))
        self.assertEqual(amount,2)

    def test_neighbors_side_node(self):
        amount = len(self.wilson.neighbors((0,1)))
        self.assertEqual(amount,3)

    def test_neighbors_inside_node(self):
        amount = len(self.wilson.neighbors((1,1)))
        self.assertEqual(amount,4)

    def test_route_visits_every_node(self):
        visited = set()
        maze = self.wilson.create_maze()
        for path in maze[1:]:
            for node in path:
                visited.add(node)
        self.assertEqual(len(visited),100)
