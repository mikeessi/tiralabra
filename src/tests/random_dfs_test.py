import unittest
from algorithms.random_dfs import DFS

class TestDFS(unittest.TestCase):
    def setUp(self):
        self.dfs = DFS(10)

    def test_constructor_creates_size_correctly(self):
        self.assertEqual(self.dfs.size, 10)
