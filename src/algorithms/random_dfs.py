import random

class DFS:
    """
    Luokka, joka mallintaa syvyyshakua.
    """
    def __init__(self, size):
        """
        Args:
            size: Sokkelon reunan pituus
        """
        self.size = size
        self.maze = []
        self.visited = set()

    def create_maze(self,x,y):
        """
        Luo sokkelon satunnaistetulla syvyyshaulla.
        Sen sijaan, että valitaan aina tietty kulkusuunta,
        lista suunnista sekoitetaan jokaisella iteraatiolla ja
        suunnanvalinta on näin sattumanvarainen.

        Args:
            x,y: Sokkelon luonnin alkukoordinaatit
        Returns:
            Lista algoritmin luomasta reitistä muodossa (x,y,dir),
            missä x,y ovat solun koordinaatit ja dir on suunta,
            mistä soluun saavutaan.
        """
        directions = [(1,0,"U"),(-1,0,"D"),(0,1,"L"),(0,-1,"R")]
        nodes = []
        nodes.append((x,y,None))
        while nodes:
            (nx,ny,direction) = nodes.pop()
            if (nx,ny) in self.visited:
                continue
            self.visited.add((nx,ny))
            self.maze.append((nx,ny,direction))
            random.shuffle(directions)
            for (dx,dy,direction) in directions:
                if (nx+dx >= 0 and nx+dx < self.size and ny+dy >= 0 and ny+dy < self.size
                   and (nx+dx,ny+dy) not in self.visited):
                    nodes.append((nx+dx,ny+dy,direction))
        return self.maze
