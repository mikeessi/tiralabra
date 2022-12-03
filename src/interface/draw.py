import pygame
from pygame.constants import K_ESCAPE, K_RETURN, KEYDOWN
from interface.clock import Clock
from interface.eventqueue import EventQueue
from interface.renderer import Renderer

class Draw:
    """
    Luokka, joka mallintaa sokkelon piirtämistä.
    """

    def __init__(self,display,route,size):
        """
        Luo kello- tapahtumajono-, ja renderöintioliot.
        Laskee solulle sopivan koon, jottei sokkelo mene muuta kuin suurilla
        syötteillä ikkunan ulkopuolelle.
        Args:
            display: pygame.display-olio, jolle kuva piirretään
            route: Lista ruudulle piirrettävistä soluista sopivassa järjestyksessä.
            size: Sokkelon reunan mitta soluina.
        """
        self.display = display
        self.clock = Clock()
        self.eventqueue = EventQueue()
        self.cell_size = self.calculate_cell_size(size)
        self.renderer = Renderer(self.cell_size)
        self.route = route
        self.route_so_far = []

    def handle_events(self):
        """
        Käsittelee tapahtumat.

        Returns:
            False, kun halutaan palata takaisin menuun.
        """
        for event in self.eventqueue.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                return False
            if event.type == pygame.QUIT:
                return False
            if event.type == KEYDOWN and event.key == K_RETURN:
                self.skip_to_end()

    def run(self):
        """
        Hoitaa sokkelon vaiheittaisen piirtämisen ruudulle.
        """
        while True:
            if self.handle_events() is False:
                break
            if len(self.route) > 0:
                self.route_so_far.append(self.route.pop(0))
            self.renderer.render(self.display, self.route_so_far)
            self.clock.tick(30)


    def calculate_cell_size(self,size):
        """
        Laskee solulle sopivan koon.
        Returns:
            Solun koko.
        """
        offset_total = size*2
        cell_size = max(1,round((1000-offset_total)/size))
        return cell_size

    def skip_to_end(self):
        self.route_so_far = self.route_so_far + self.route
        self.route = []
