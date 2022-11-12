import random

class UF:
    """
    Luokka, joka mallintaa union-find tietorakennetta Kruskalin algoritmia varten.
    """
    def __init__(self, size):
        """
        Luo hajautustaulun solmuille, luo jokaisesta ruudukon solusta solmun.

        Args:
            size = Sokkelon reunan koko soluina
        """
        self.size = size
        self.node_map = {}
        self.nodes = [(i,j) for j in range(size) for i in range(size)]
        for i, val in enumerate(self.nodes):
            node = UFNode(val, i)
            self.node_map[val] = node

    def neighbors(self, node):
        """
        Tekee naapurilistan solmulle,

        Args:
            node: Solmu, jonka naapurilista halutaan saada.
        Returns:
            Lista koordinaateista solmun ympäriltä.
        """
        return [(node[0]+dx,node[1]+dy) for dx, dy in ((-1,0),(1,0),(0,1),(0,-1))
               if node[0]+dx >= 0 and node[0]+dx < self.size
               and node[1]+dy >= 0 and node[1]+dy < self.size]

    def find(self, node):
        """
        Kertoo kyseisen komponentin edustajasolmun.

        Args:
            node: Solmu, jonka komponentin edustajasolmu halutaan tietää.
        Returns:
            Komponentin edustajasolmu
        """
        return self.find_node(node).parent

    def find_node(self, node):
        """
        Kertoo komponentin edustajasolun.

        Args:
            node: Solmu, jonka edustaja halutaan tietää.
        Returns
            Edustajasolmu
        """
        if isinstance(self.node_map[node].parent,int):
            return self.node_map[node]
        parent_node = self.find_node(self.node_map[node].parent.val)
        self.node_map[node].parent = parent_node
        return parent_node

    def union(self, node1, node2):
        """
        Tarkistaa, kuuluuko solmut samaan komponenttiin. Jos ei, liitetään ne samaan komponenttiin.

        Args:
            node1, node2: Solmut, jotka halutaan yhdistää.
        """
        parent1 = self.find_node(node1)
        parent2 = self.find_node(node2)
        if parent1.parent != parent2.parent:
            parent1.parent = parent2


    def kruskal(self):
        """
        Määrittää virittävän puun kaikkien ruudukon komponenttien välillä satunnaisesti.
        Ts. luo sokkelon, johon kaikki ruudukon solmut kuuluvat.

        Returns:
            Virittävä puu listana, joka kertoo solmujen yhteydet.
        """
        edges = [(node,nbor) for node in self.nodes for nbor in self.neighbors(node)]
        maze = []

        while len(maze) < len(self.nodes)-1:
            edge = edges.pop(random.randint(0, len(edges)-1))
            if self.find(edge[0]) != self.find(edge[1]):
                self.union(edge[0], edge[1])
                maze.append(edge)
        return maze

class UFNode:
    """
    Luokka, joka mallintaa yhtä solmua/komponenttia union-find-tietorakenteessa.
    """
    def __init__(self,val,parent):
        self.val = val
        self.parent = parent

a = UF(10)
