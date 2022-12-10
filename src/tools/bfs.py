from collections import deque

def bfs(size, maze):
    """
    Määrittää syvyyshaulla, että sokkelo on varmasti yhtenäinen.
    Aluksi lasketaan solujen yhteismäärä, ja sitten siitä vähennetään
    yksi aina, kun kohdataan uusi solu. Jos lopussa yhteismäärä on 0,
    on kaikissa soluissa käyty, ja näin ollen sokkelo on yhtenäinen.
    """
    start = (0,0)
    remaining = size*size
    visited = set()
    stack = deque()
    stack.append(start)
    while stack:
        curr_node = stack.popleft()
        remaining -= 1
        visited.add(curr_node)
        for neighbor in maze[curr_node]:
            if neighbor not in visited:
                stack.append(neighbor)
    if remaining == 0:
        return True
    return False
