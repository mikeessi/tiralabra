import sys
from app import App
from kruskal import UF

algs = {"1":1
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
            route = parse_kruskal_output(maze)
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
        print("2. Alkuun")
        ans = input()
        if ans == "2":
            return None
        try:
            alg = algs[ans]
            return alg
        except KeyError:
            pass

def parse_kruskal_output(maze):
    """
    Muodostaa Kruskalin algoritmin tuotoksesta sopivan reittilistan pygamelle.

    Args:
        Kruskalin algoritmin antama lista, alkiot muotoa ((x,y),(a,b)),
        missä (x,y) on käytävän lähtösolu ja (a,b) kohdesolu.
    Returns:
        Lista muotoa (x,y,dir), jossa x,y on käytävän solun koordinaatit
        ja dir on suunta, missä naapurisolu on.
    """
    dirs = {(1,0):"D",
            (-1,0):"U",
            (0,1):"R",
            (0,-1):"L"
           }
    output = []
    seen = set([])
    for ((x,y),(a,b)) in maze:
        if (x,y) in seen:
            direction = (x-a,y-b)
            output.append((a,b,dirs[direction]))
            seen.add((a,b))
        else:
            seen.add((x,y))
            seen.add((a,b))
            direction = (x-a,y-b)
            output.append((x,y,None))
            output.append((a,b,dirs[direction]))
    return output

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
        union_find = UF(size)
        maze = union_find.kruskal()
        return maze

if __name__ == "__main__":
    main()
