import unittest
from algorithms.kruskal import UF

class TestUF(unittest.TestCase):
    def setUp(self):
        self.unionfind = UF(10)
        self.parent = {(1,1):(1,1),
                       (0,1):(1,1),
                       (1,0):(1,0)}
        self.rank = {(1,1):1,
                     (0,1):0,
                     (1,0):0}

    def test_constructor_creates_correct_amount_of_nodes(self):
        self.assertEqual(len(self.unionfind.nodes),100)

    def test_constructor_creates_correct_amount_of_edges(self):
        self.assertEqual(len(self.unionfind.edges), 360)

    def test_neighbours_creates_correct_output(self):
        nbors = self.unionfind.neighbors((1,1))
        self.assertEqual(nbors[0],(0,1))

    def test_find(self):
        root = self.unionfind.find(self.parent, (0,1))
        self.assertEqual(root,(1,1))

    def test_union_root1_rank_is_bigger(self):
        node1 = (1,1)
        node2 = (1,0)
        self.unionfind.union(self.parent, self.rank, node1, node2)
        self.assertEqual(self.parent[node2], node1)

    def test_union_root2_rank_is_bigger(self):
        node1 = (1,1)
        node2 = (1,0)
        self.rank[node2] = 2
        self.unionfind.union(self.parent, self.rank, node1, node2)
        self.assertEqual(self.parent[node1], node2)

    def test_union_root_ranks_are_equal_correct_parent_set(self):
        node1 = (1,1)
        node2 = (1,0)
        self.rank[node2] = 1
        self.unionfind.union(self.parent, self.rank, node1, node2)
        self.assertEqual(self.parent[node2], node1)

    def test_union_root_ranks_are_equal_correct_rank_increase(self):
        node1 = (1,1)
        node2 = (1,0)
        self.rank[node2] = 1
        self.unionfind.union(self.parent, self.rank, node1, node2)
        self.assertEqual(self.rank[node1], 2)

    def test_kruskal_output_maze_lenght(self):
        maze = self.unionfind.kruskal()
        self.assertEqual(len(maze),99)
