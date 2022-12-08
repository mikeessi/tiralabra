import random

class Wilson:
    """
    Luokka, joka mallintaa Wilsonin algoritmia.
    """

    def __init__(self,size):
        """
        Luo listan jokaisen solun koordinaateista, ja hajautustaulun solujen naapureista.
        """
        self.size = size
        self.nodes = [(i,j) for i in range(size) for j in range(size)]
        self.edges = {node:self.neighbors(node) for node in self.nodes}

    def neighbors(self, node):
        """
        Luo solulle listan naapureista.

        Args:
            node: Solu, jolle naapurilista halutaan tehdä.
        Returns:
            Lista, jossa argumenttisolun naapurit.
        """
        return [(node[0]+dx,node[1]+dy) for dx, dy in ((-1,0),(1,0),(0,1),(0,-1))
               if node[0]+dx >= 0 and node[0]+dx < self.size
               and node[1]+dy >= 0 and node[1]+dy < self.size]

    def create_maze(self):
        """
        Luo sokkelon ensin valitsemalla satunnaisen solun, ja lisäämällä sen osaksi sokkeloa.
        Tämän jälkeen valitaan satunnainen solu, joka ei vielä kuulu sokkeloon, ja etsitään
        sieltä reitti sokkeloon. Jatketaan kunnes kaikki solut ovat osa sokkeloa.

        Returns:
            Sokkelo, jonka ensimmäinen alkio on tuple (x,y), joka merkitsee sokkelon alkua.
            Loput alkiot ovat muotoa [(x,y)], joista kukin kuvaa yhtä reittiä satunnaisesta
            solusta sokkelon osaksi.
        """
        start = self.new_node()
        route = [start]

        while len(self.nodes) > 0:
            node = random.choice(self.nodes)
            path = [node]

            while node in self.nodes:
                neighbor = random.choice(self.edges[node])
                if neighbor in path:
                    path = path[0:path.index(neighbor)+1]
                else:
                    path.append(neighbor)
                node = neighbor
            for node in path:
                if node not in self.nodes:
                    continue
                self.nodes.remove(node)
            route.append(path)

        return route

    def new_node(self):
        """
        Tuottaa uuden satunnaisen solun solujen listalta.
        """
        return self.nodes.pop(random.randint(0,len(self.nodes)-1))
