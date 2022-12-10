import pygame

WHITE = (255,255,255)

class Renderer:
    """
    Mallintaa renderöijää, joka piirtää sokkelon pygame-ikkunaan.
    """

    def __init__(self,cell_size):
        """
        Asettaa taustaväriksi mustan, asettaa sopivan solun koon,
        sekä seinän paksuuden

        Args:
            cell_size: Yhden solun reunan pituus
        """
        self.bg_color = (0,0,0)
        self.cell_size = cell_size
        self.offset = 2

    def render(self, display, route):
        """
        Piirtää sokkelon solut ruudulle, sekä niiden väliset käytävät.
        Piirtää käytävän sen perustella, mikä suunta solun koordinaatit
        sisältävässä tuplessa on.

        Args:
            display: Pygame-ikkuna, johon piirretään
            route: Lista koordinaateista ja suunnista muotoa (x,y,dir)
        """
        display.fill(self.bg_color)

        for (y,x,direction) in route:
            y_coord = y*self.cell_size + y*self.offset
            x_coord = x*self.cell_size + x*self.offset
            if direction is None:
                rect = pygame.Rect(x_coord,y_coord,self.cell_size, self.cell_size)
            elif direction == "L":
                rect = pygame.Rect(x_coord-self.offset,y_coord,
                                  self.cell_size+self.offset,self.cell_size)
            elif direction == "R":
                rect = pygame.Rect(x_coord,y_coord,
                                  self.cell_size+self.offset,self.cell_size)
            elif direction == "D":
                rect = pygame.Rect(x_coord,y_coord,self.cell_size,
                                  self.cell_size+self.offset)
            elif direction == "U":
                rect = pygame.Rect(x_coord,y_coord-self.offset,self.cell_size,
                                  self.cell_size+self.offset)
            pygame.draw.rect(display, WHITE, rect)
        pygame.display.flip()
