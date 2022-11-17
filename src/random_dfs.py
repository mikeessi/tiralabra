import random

class DFS:
    def __init__(self, size):
        self.size = size
        self.maze = []
        self.visited = set()

    def create_maze(self,x,y):
        directions = [(1,0,"U"),(-1,0,"D"),(0,1,"L"),(0,-1,"R")]
        nodes = []
        nodes.append((x,y,None))
        while nodes:
            (nx,ny,dir) = nodes.pop()
            if (nx,ny) in self.visited:
                continue
            self.visited.add((nx,ny))
            self.maze.append((nx,ny,dir))
            random.shuffle(directions)
            for (dx,dy,dir) in directions:
                if (nx+dx >= 0 and nx+dx < self.size and ny+dy >= 0 and ny+dy < self.size
                   and (nx+dx,ny+dy) not in self.visited):
                    nodes.append((nx+dx,ny+dy,dir))
        return self.maze

