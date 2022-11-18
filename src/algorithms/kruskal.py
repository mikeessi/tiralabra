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
        self.nodes = [(i,j) for j in range(size) for i in range(size)]
        self.edges = [(node,nbor) for node in self.nodes for nbor in self.neighbors(node)]

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

    def find(self, parent, node):
        """
        Kertoo kyseisen komponentin edustajasolmun.

        Args:
            parent: Hajautustaulu, jossa kunkin solmun komponentin edustaja.
            node: Solmu, jonka komponentin edustajasolmu halutaan tietää.
        Returns:
            Komponentin edustajasolmu
        """
        if parent[node] == node:
            return node
        return self.find(parent, parent[node])

    def union(self, parent, rank, node1, node2):
        """
        Tarkistaa, kuuluuko solmut samaan komponenttiin. Jos ei, liitetään ne samaan komponenttiin.

        Args:
            parent: Hajautustaulu, joka kertoo kunkin solmun komponentin edustajan.
            rank: Hajautustaulu, joka kertoo kunkin komponentin "syvyyden".
            node1, node2: Solmut, jotka halutaan yhdistää.
        """
        root1 = self.find(parent,node1)
        root2 = self.find(parent,node2)
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root2] = root1
            rank[root1] += 1


    def kruskal(self):
        """
        Määrittää virittävän puun kaikkien ruudukon komponenttien välillä satunnaisesti.
        Ts. luo sokkelon, johon kaikki ruudukon solmut kuuluvat.

        Returns:
            Virittävä puu listana, joka kertoo solmujen yhteydet.
        """
        maze = []
        rank = {}
        parent = {}
        for node in self.nodes:
            rank[node] = 0
            parent[node] = node

        while len(maze) < len(self.nodes)-1:
            node1, node2 = self.edges.pop(random.randint(0, len(self.edges)-1))
            root1 = self.find(parent, node1)
            root2 = self.find(parent, node2)
            if root1 != root2:
                maze.append((node1,node2))
                self.union(parent,rank,node1,node2)
        return maze

