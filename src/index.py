import sys
from app import App
from parse_output import parse_wilson_output, parse_kruskal_output
from algorithms.kruskal import UF
from algorithms.random_dfs import DFS
from algorithms.wilson import Wilson

algs = {"1":1,
        "2":2,
        "3":3
       }

def main():
    """
    Käyttöliittymän pääsilmukka
    """
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
    """
    Kutsuu pygamea piirtämään sokkelon ruudulle.
    Args:
        route: Järjestys, jossa reitti piirretään ruudulle
        size: Ruudukon koko (size*size)
        cell_size: Yksittäisen solun koko
    """
    screen = App(route,size,cell_size)
    screen.run()

def choose_params():
    """
    Silmukka, jossa valitaan halutut luotavan sokkelon parametrit.
    """
    while True:
        size = choose_size()
        if size is None:
            return
        alg = choose_alg()
        if alg is None:
            return
        maze = create_maze(size, alg)
        draw_query = choose_to_draw()
        if draw_query is True:
            cell_size = define_cell_size(size)
            if alg == 1:
                route = parse_kruskal_output(maze)
            elif alg == 3:
                route = parse_wilson_output(maze)
            else:
                route = maze
            draw_pic(route,size,cell_size)

def choose_size():
    """
    Silmukka, jossa valitaan sokkelon koko.

    Returns:
        size: Ruudukon reunan pituus soluina
    """
    while True:
        print("Valitse sokkelon koko (>=2)")
        print("e. Takaisin")
        ans = input()
        if ans == "e":
            return None
        try:
            size = int(ans)
            if size >= 2:
                return size
        except ValueError:
            pass

def choose_alg():
    """
    Silmukka, jossa valitaan käytettävä algoritmi

    Returns:
        alg: Haluttu algoritmi
    """
    while True:
        print("Valitse käytettävä algoritmi")
        print("1. Satunnaistettu Kruskalin algoritmi")
        print("2. Satunnaistettu syvyyshaku")
        print("3. Wilsonin algoritmi")
        print("4. Alkuun")
        ans = input()
        if ans == "4":
            return None
        try:
            alg = algs[ans]
            return alg
        except KeyError:
            pass

def choose_to_draw():
    """
    Silmukka, jossa päätetään, piirretäänkö sokkelo vai ei.
    Isojen sokkeloiden piirtäminen ei mahdu ruudulle ja niiden piirtämisessä kestäisi
    kovin kauan, joten niitä ei välttämättä haluta piirtää.

    Returns:
        Totuusarvon, joka kertaa piirretäänkö vai ei.
    """
    while True:
        print("Piirretäänkö sokkelo? k/e")
        ans = input()
        if ans == "k":
            return True
        if ans == "e":
            return False

def define_cell_size(size):
    """
    Laskee sopivan solukoon solujen määrän perusteella.

    Returns:
        Sopivan solukoon.
    """
    return round(800/size)

def create_maze(size, algo):
    """
    Kutsuu algoritmi/tietorakenneluokat ja luo sokkelot.

    Args:
        size: Sokkelon koko
        algo: Käytettävä algoritmi
    Returns:
        Sokkelo "raakamuodossa", joka vaatii ehkä vielä uudelleenmuokkausta pygamea varten
    """
    if algo == 1:
        uf = UF(size)
        maze = uf.kruskal()
        return maze
    if algo == 2:
        dfs = DFS(size)
        maze = dfs.create_maze(0,0)
        return maze
    if algo == 3:
        wilson = Wilson(size)
        maze = wilson.create_maze()
        return maze

if __name__ == "__main__":
    main()
