import unittest
from algorithms.random_dfs import DFS

class TestDFS(unittest.TestCase):
    def setUp(self):
        self.dfs = DFS(10)

    def test_constructor_creates_size_correctly(self):
        self.assertEqual(self.dfs.size, 10)

    def test_all_cells_visited_are_unique(self):
        maze = self.dfs.create_maze(0,0)
        self.assertEqual(len(self.dfs.visited),100)

    def test_correct_maze_length(self):
        maze = self.dfs.create_maze(0,0)
        self.assertEqual(len(maze), 100)
