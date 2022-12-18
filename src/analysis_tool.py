import time
from algorithms.parse_output import parse_wilson_output, parse_kruskal_output
from algorithms.kruskal import UF
from algorithms.wilson import Wilson
from algorithms.random_dfs import DFS
from algorithms.aldous_broder import AldousBroder
from tools.adjacency_dict import create_adjacency_dict
from tools.dead_ends import count_dead_ends
from tools.bfs import bfs

GREETINGS = {1:"SATUNNAISTETTU KRUSKALIN ALGORITMI",
             2:"SATUNNAISTETTU SYVYYSHAKU",
             3:"WILSONIN ALGORITMI",
             4:"ALDOUS-BRODERIN ALGORITMI"
            }

def test_algorithm(iterations, size, algorithm):
    """
    Luo halutun määrän tietyn algoritmin tuottamia sokkeloita,
    ja laskee sokkeloiden luomiseen kuluneen ajan, umpikujien määrän,
    sekä kaikkien sokkeloiden em. ominaisuuksien keskiarvon.

    Args:
        iterations: Iteraatioiden määrä
        size: Haluttu sokkelokoko
        algorithm: Testattava algoritmi
    """
    times = []
    dead_end_counts = []

    print(f"{GREETINGS[algorithm]:>40}")

    for iteration in range(iterations):
        start = time.time()
        if algorithm == 1:
            maze = test_kruskal(size)
        if algorithm == 2:
            maze = test_dfs(size)
        if algorithm == 3:
            maze = test_wilson(size)
        if algorithm == 4:
            maze = test_aldous_broder(size)
        end = time.time()

        times.append(end-start)

        if algorithm == 1:
            maze = parse_kruskal_output(maze)
        if algorithm == 3:
            maze = parse_wilson_output(maze)

        adj_dict = create_adjacency_dict(maze)

        dead_ends = count_dead_ends(adj_dict)
        dead_end_counts.append(dead_ends)

        is_uniform = bfs(size, adj_dict)
        print_single_maze_results(iteration,end-start,dead_ends,is_uniform)

    print_total_results(iterations, times, dead_end_counts)

def test_kruskal(size):
    """
    Luo testisokkelon Kruskalin algoritmilla

    Args:
        size: Sokkelon koko
    """
    union_find = UF(size)
    maze = union_find.kruskal()
    return maze

def test_dfs(size):
    """
    Luo testisokkelon syvyyshaulla

    Args:
        size: Sokkelon koko
    """
    dfs = DFS(size)
    maze = dfs.create_maze(0,0)
    return maze

def test_wilson(size):
    """
    Luo testisokkelon Wilsonin algoritmilla

    Args:
        size: Sokkelon koko
    """
    wilson = Wilson(size)
    maze = wilson.create_maze()
    return maze

def test_aldous_broder(size):
    """
    Luo testisokkelon Aldous-Broderin algoritmilla

    Args:
        size: Sokkelon koko
    """
    aldous_broder = AldousBroder(size)
    maze = aldous_broder.create_maze()
    return maze

def print_single_maze_results(number, elapsed_time, dead_ends, is_uniform):
    """
    Tulostaa ruudulle yksittäisen sokkelon ominaisuudet

    Args:
        number: Iteraation numero
        time: Luontiin kulunut aika
        dead_ends: Umpikujien määrä sokkelossa
        is_uniform: Totuusarvo sokkelon yhtenäisyydestä
    """
    print(f"Sokkelo nro {number+1}:")
    print(f"-- Luotu ajassa: {elapsed_time} sekuntia")
    print(f"-- Umpikujien määrä: {dead_ends}")
    print(f"-- Sokkelo on yhtenäinen: {'Kyllä' if is_uniform is True else 'Ei'}")


def print_total_results(iterations, times, dead_ends):
    """
    Laskee keskiarvot sokkeloiden luontiajoille ja umpikujien määrille.
    Määrittää lyhimmän ja pisimmän luomisajan. Määrittää suurimman ja
    pienimmän umpikujien määrän.
    Tulostaa ruudulle koko testaussilmukan tulokset.

    Args:
        iterations: Kierrosten määrä
        times: Lista jokaisen sokkelon luontiajoista
        dead_ends: Lista jokaisen sokkelon umpikujien määristä
    """
    print("----------------------------------------------------")
    print(f"Aikojen keskiarvo: {sum(times)/iterations} sekuntia")
    print(f"Nopein luonti: {min(times)} sekuntia")
    print(f"Hitain luonti: {max(times)} sekuntia")
    print(f"Umpikujien keskiarvo: {sum(dead_ends)/iterations}")
    print(f"Vähiten umpikujia: {min(dead_ends)}")
    print(f"Eniten umpikujia: {max(dead_ends)}")
