import unittest
from algorithms.aldous_broder import AldousBroder

class TestAldousBroder(unittest.TestCase):
    def setUp(self):
        self.aldous_broder = AldousBroder(10)

    def test_constructor_creates_size_correctly(self):
        self.assertEqual(self.aldous_broder.size, 10)

    def test_constructor_correct_remaining(self):
        self.assertEqual(self.aldous_broder.remaining, 100)

    def test_all_cells_are_visited(self):
        maze = self.aldous_broder.create_maze()
        self.assertEqual(len(self.aldous_broder.route), 100)
