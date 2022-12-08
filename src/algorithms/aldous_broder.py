import random

class AldousBroder:

    def __init__(self, size):
        self.size = size
        self.remaining = self.size**2
        self.route = set()

    def create_maze(self):
        """
        Tuottaa sokkelon hyödyntämällä Aldous-Broderin algoritmia.
        """
        directions = [(1,0,"U"),(-1,0,"D"),(0,1,"L"),(0,-1,"R")]
        x, y = (random.randint(0,self.size-1), random.randint(0,self.size-1))
        self.remaining -= 1
        path = [(x,y,None)]
        self.route.add((x,y))
        curr_node = (x,y)
        while self.remaining > 0:
            random.shuffle(directions)
            for (dx, dy, direction) in directions:
                nx, ny = (curr_node[0]+dx,curr_node[1]+dy)
                if nx >= 0 and ny >= 0 and nx < self.size and ny < self.size:
                    curr_node = (nx, ny)
                    break
            if curr_node in self.route:
                continue
            a, b = curr_node
            path.append((a,b,direction))
            self.route.add((a,b))
            self.remaining -= 1
        return path