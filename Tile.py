import pygame

class Tile:
    Name = None
    PygameImage = None
    Symbol = None

    def __init__(self, name, symbol, file):
        self.PygameImage = pygame.image.load(file)
        self.Symbol = symbol
        self.Name = name

        pass
