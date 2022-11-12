import pygame, sys
from pygame.constants import K_ESCAPE, KEYDOWN
from clock import Clock
from eventqueue import EventQueue
from renderer import Renderer

class App:

    def __init__(self,route,size,cell_size):
        self.clock = Clock()
        self.eventqueue = EventQueue()
        self.renderer = Renderer(cell_size)
        self.screen_size = self.calculate_screen_size(size, cell_size)
        self.route = route
        self.route_so_far = []

    def handle_events(self):
        for event in self.eventqueue.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                return False
            if event.type == pygame.QUIT:
                return False

    def run(self):
        self.display = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Sokkelo")
        pygame.init()
        while True:
            if self.handle_events() is False:
                break
            if len(self.route) > 0:
                self.route_so_far.append(self.route.pop(0))
            self.renderer.render(self.display, self.route_so_far)
            self.clock.tick(200)

        pygame.quit()
        sys.exit()

    def calculate_screen_size(self,size, cell_size):
        height = size*cell_size + size*2
        return (height, height)
