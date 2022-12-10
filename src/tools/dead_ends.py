

def count_dead_ends(maze):
    """
    Laskee sokkelon vieruslistaesityksestä kuinka monta umpikujaa
    sokkelossa on. Mikäli solulla on vain yksi naapuri, sen on oltava
    umpikuja.
    """
    counter = 0
    for neighbours in maze.values():
        if len(neighbours) == 1:
            counter += 1
    return counter
