
def parse_wilson_output(maze):
    """
    Muodostaa Wilsonin algoritmin tuotoksesta sopivan reittilistan pygamelle.

    Args:
        Wilsonin algoritmin tuottama lista, jossa ensimmäinen alkio on
        tuple (x,y), joka on lähtösolu, ja loput alkiot ovat [(x,y)]
        muotoisia listoja, jotka kuvaavat algoritmin etsimää reittiä.
    Returns:
        Lista muotoa (x,y,dir), jossa x,y ovat reitin solun koordinaatit
        ja dir on suunta, missä naapurisolu on, tai None, jos polku alkaa
        tästä solusta.
    """
    dirs = {(1,0):"U",
        (-1,0):"D",
        (0,1):"L",
        (0,-1):"R"
       }
    output = []
    (x,y) = maze.pop(0)
    output.append((x,y,None))
    previous = None
    for path in maze:
        for (x,y) in path:
            if previous is None:
                output.append((x,y,None))
                previous = (x,y)
            else:
                (a,b) = previous
                direction = (x-a,y-b)
                output.append((x,y,dirs[direction]))
                previous = (x,y)
        previous = None
    return output

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
