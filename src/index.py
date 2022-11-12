import sys
from app import App
from kruskal import UF
import random

options = {"1":(800,800),
           "2":(600,600)
          }

algs = {"1":1
       }

def main():
    while True:
        print("Valitse toiminto")
        print("1. Luo uusi sokkelo")
        print("2. Poistu")
        ans = input()
        if ans == "1":
            choose_params()
        if ans == "2":
            sys.exit()

def draw_pic(route,size,cell_size):
    screen = App(route,size,cell_size)
    screen.run()

def choose_params():
    while True:
        size = choose_size()
        if size is None:
            return
        alg = choose_alg()
        if alg is None:
            return
        maze = create_maze(size, alg)
        draw_query = choose_to_draw()
        if draw_query == True:
            cell_size = define_cell_size(size)
            route = parse_kruskal_output(maze)
            draw_pic(route,size,cell_size)

def choose_size():
    while True:
        print("Valitse sokkelon koko (>=2)")
        print("e. Takaisin")
        ans = input()
        if ans == "e":
            return None
        else:
            try:
                size = int(ans)
                if size >= 2:
                    return size
            except:
                pass

def choose_alg():
    while True:
        print("Valitse käytettävä algoritmi")
        print("1. Satunnaistettu Kruskalin algoritmi")
        print("2. Alkuun")
        ans = input()
        if ans == "2":
            return None
        try:
            alg = algs[ans]
            return alg
        except:
            pass

def parse_kruskal_output(maze):
    dirs = {(1,0):"D",
            (-1,0):"U",
            (0,1):"R",
            (0,-1):"L"
           }
    output = []
    seen = set([])
    for ((x,y),(a,b)) in maze:
        if (x,y) in seen:
            dir = (x-a,y-b)
            output.append((a,b,dirs[dir]))
            seen.add((a,b))
        else:
            seen.add((x,y))
            seen.add((a,b))
            dir = (x-a,y-b)
            output.append((x,y,None))
            output.append((a,b,dirs[dir]))
    return output

def choose_to_draw():
    while True:
        print("Piirretäänkö sokkelo? k/e")
        ans = input()
        if ans == "k":
            return True
        if ans == "e":
            return False

def define_cell_size(size):
    return round(800/size)

def create_maze(size, algo):
    if algo == 1:
        union_find = UF(size)
        maze = union_find.kruskal()
        return maze

if __name__ == "__main__":
    main()
