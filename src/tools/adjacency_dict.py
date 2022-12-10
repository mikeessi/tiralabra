
def create_adjacency_dict(route):
    """
    Luo annetusta reitistä sokkelon vieruslistaesityksen

    Args:
        route: Algoritmin muodostama reitti.
    """
    adj_dict = {}
    for x,y,direction in route:
        if (x,y) not in adj_dict:
            adj_dict[(x,y)] = []
        if direction is None:
            continue
        neighbour = get_neighbour(x,y,direction)
        if neighbour not in adj_dict[(x,y)]:
            adj_dict[(x,y)].append(neighbour)
        if neighbour not in adj_dict:
            adj_dict[neighbour] = [(x,y)]
        if neighbour in adj_dict and (x,y) not in adj_dict[neighbour]:
            adj_dict[neighbour].append((x,y))
    return adj_dict

def get_neighbour(x,y,direction):
    """
    Laskee suunnan perusteella naapurisolun koordinaatit

    Args:
        x, y: Solun koordinaatit
        direction: Suunta, jossa naapuri on
    """
    if direction == "U":
        return (x-1,y)
    if direction == "D":
        return (x+1,y)
    if direction == "L":
        return (x,y-1)
    if direction == "R":
        return (x,y+1)
