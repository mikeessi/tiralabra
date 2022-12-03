import pygame_menu
from interface.draw import Draw
from algorithms.random_dfs import DFS
from algorithms.wilson import Wilson
from algorithms.kruskal import UF
from algorithms.parse_output import parse_kruskal_output, parse_wilson_output

class Menu:

    def __init__(self,display):
        self.display = display

        self.menu = pygame_menu.Menu("Sokkelosovellus",1000,1000,
                                     theme=pygame_menu.themes.THEME_DARK)
        self.alg_input = self.menu.add.selector("Algoritmi :", [("Satunnaistettu Kruskal",1),
                         ("Satunnaistettu syvyyshaku",2),("Wilsonin algoritmi",3)])
        self.size_input = self.menu.add.text_input("Sokkelon koko :", default="20",
                           valid_chars=["1","2","3","4","5","6","7","8","9","0"])
        self.menu.add.button("Luo sokkelo", self.create_maze)
        self.menu.add.button("Poistu", pygame_menu.events.EXIT)

    def create_maze(self):
        size = self.get_size()
        alg = self.alg_input.get_index()
        if alg == 0:
            uf = UF(size)
            route = parse_kruskal_output(uf.kruskal())
        if alg == 1:
            dfs = DFS(size)
            route = dfs.create_maze(0,0)
        if alg == 2:
            wilson = Wilson(size)
            route = parse_wilson_output(wilson.create_maze())
        self.draw_maze(route,size)

    def get_size(self):
        if self.size_input.get_value() == "":
            size = 20
        elif int(self.size_input.get_value()) == 0:
            size = 20
        else:
            size = int(self.size_input.get_value())
        return size

    def draw_maze(self,route,size):
        app = Draw(self.display,route, size)
        app.run()
