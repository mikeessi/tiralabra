import random

class UF:
    def __init__(self, size):
        self.size = size
        self.node_map = {}
        self.nodes = [(i,j) for j in range(size) for i in range(size)]
        for i, val in enumerate(self.nodes):
            n = UFNode(val, i)
            self.node_map[val] = n

    def neighbors(self, node):
        return [(node[0]+dx,node[1]+dy) for dx, dy in ((-1,0),(1,0),(0,1),(0,-1))
               if node[0]+dx >= 0 and node[0]+dx < self.size and node[1]+dy >= 0 and node[1]+dy < self.size] 

    def find(self, node):
        return self.find_node(node).parent

    def find_node(self, node):
        if type(self.node_map[node].parent) is int:
            return self.node_map[node]
        else:
            parent_node = self.find_node(self.node_map[node].parent.val)
            self.node_map[node].parent = parent_node
            return parent_node

    def union(self, node1, node2):
        parent1 = self.find_node(node1)
        parent2 = self.find_node(node2)
        if parent1.parent != parent2.parent:
            parent1.parent = parent2


    def kruskal(self):
        edges = [(node,nbor) for node in self.nodes for nbor in self.neighbors(node)]
        self.maze = []

        while len(self.maze) < len(self.nodes)-1:
            edge = edges.pop(random.randint(0, len(edges)-1))
            if self.find(edge[0]) != self.find(edge[1]):
                self.union(edge[0], edge[1])
                self.maze.append(edge)
        return self.maze

class UFNode:
    def __init__(self,val,parent):
       self.val = val
       self.parent = parent

a = UF(10)
