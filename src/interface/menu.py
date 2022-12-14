import pygame_menu
from interface.draw import Draw
from algorithms.random_dfs import DFS
from algorithms.wilson import Wilson
from algorithms.kruskal import UF
from algorithms.aldous_broder import AldousBroder
from algorithms.parse_output import parse_kruskal_output, parse_wilson_output

class Menu:
    """
    Mallintaa ohjelman menua hyödyntämällä pygame_menu-kirjastoa
    """
    def __init__(self,display):
        """
        Luo menuun nappulat ja valitsimet.

        Args:
            display: Pygame-ikkuna,johon menu halutaan
        """
        self.display = display

        self.menu = pygame_menu.Menu("Sokkelosovellus",1000,1000,
                                     theme=pygame_menu.themes.THEME_DARK)
        self.alg_input = self.menu.add.selector("Algoritmi: ", [("Satunnaistettu Kruskal",1),
                         ("Satunnaistettu syvyyshaku",2),("Wilsonin algoritmi",3),
                         ("Aldous-Broder",4)])
        self.size_input = self.menu.add.text_input("Sokkelon koko: ", default="20",
                           valid_chars=["1","2","3","4","5","6","7","8","9","0"])
        self.menu.add.button("Luo sokkelo", self.create_maze)
        self.menu.add.button("Poistu", pygame_menu.events.EXIT)

    def create_maze(self):
        """
        Hakee valitut parametrit menun valitsimista, ja kutsuu
        haluttua algoritmia sokkelon luomiseen. Kutsuu algoritmista
        riippuen parserin ja sen jälkeen kutsuu sokkelon piirtäjää.
        """
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
        if alg == 3:
            aldous_broder = AldousBroder(size)
            route = aldous_broder.create_maze()
        self.draw_maze(route,size)

    def get_size(self):
        """
        Varmistaa, että sokkelon koko on validi, ja antaa sille
        oletusarvon, mikäli näin ei ole.
        """
        if self.size_input.get_value() == "":
            size = 20
        elif int(self.size_input.get_value()) == 0:
            size = 20
        else:
            size = int(self.size_input.get_value())
        return size

    def draw_maze(self,route,size):
        """
        Luo Draw-luokan olion, ja kutsuu sitä piirtämään sokkelon
        pygame-ikkunaan

        Args:
            route: Lista algoritmin muodostamasta
            size: Sokkelon reunan pituus
        """
        app = Draw(self.display,route, size)
        app.run()
