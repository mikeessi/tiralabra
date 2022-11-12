import pygame

WHITE = (255,255,255)

class Renderer:

    def __init__(self,cell_size):
        self.bg_color = (0,0,0)
        self.cell_size = cell_size
        self.offset = 2

    def render(self, display, route):
        display.fill(self.bg_color)

        for (y,x,dir) in route:
            y_coord = y*self.cell_size + y*self.offset
            x_coord = x*self.cell_size + x*self.offset
            if dir is None:
                rect = pygame.Rect(x_coord,y_coord,self.cell_size, self.cell_size)
            elif dir == "L":
                rect = pygame.Rect(x_coord-self.offset,y_coord,self.cell_size+self.offset,self.cell_size)
            elif dir == "R":
                rect = pygame.Rect(x_coord,y_coord,self.cell_size+self.offset,self.cell_size)
            elif dir == "D":
                rect = pygame.Rect(x_coord,y_coord,self.cell_size,self.cell_size+self.offset)
            elif dir == "U":
                rect = pygame.Rect(x_coord,y_coord-self.offset,self.cell_size,self.cell_size+self.offset)
            pygame.draw.rect(display, WHITE, rect)
#        for y in grid:
#            for x in y:
#                color = BLACK
#                rect = pygame.Rect(x_offset,y_offset,50,50)
#                x_offset += 52
#                if x == True:
#                    color = WHITE
#                pygame.draw.rect(display, color, rect)
#            y_offset += 52
#            x_offset = 10
        pygame.display.flip()
