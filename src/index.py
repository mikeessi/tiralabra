import pygame
from interface.menu import Menu

def main():
    display = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption("Sokkelosovellus")
    pygame.init()

    menu = Menu(display)
    menu.menu.mainloop(display)


if __name__ == "__main__":
    main()
