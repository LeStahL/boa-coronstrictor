import pygame

class Tile:
    def __init__(self, name, symbol, file, allowed):
        self.PygameImage = pygame.image.load(file)
        self.Symbol = symbol
        self.Name = name
        self.Allowed = allowed
        pass
