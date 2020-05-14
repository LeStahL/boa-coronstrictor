import pygame
from Map import *
from Tile import *

class GameWindow:
    DisplaySurface = None
    Width = 640
    Height = 400

    def __init__(self):
        pygame.init()
        self.DisplaySurface = pygame.display.set_mode((self.Width, self.Height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.testTile = Tile("Grass", " ", "tiles/grass.png")

        while True:
            for event in pygame.event.get():
                self.eventHandler(event)
            self.render()
            pygame.display.update()

        pass

    def eventHandler(self, event):
        print(event)
        if event.type == pygame.QUIT:
            quit()
        pass

    def render(self):
        self.DisplaySurface.blit(self.testTile.PygameImage, (0,0))
        pass

if __name__ == "__main__" :
    mainWindow = GameWindow()