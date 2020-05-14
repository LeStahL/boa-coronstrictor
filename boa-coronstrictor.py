import pygame
from Map import *
from Tile import *

class GameWindow:
    DisplaySurface = None
    Width = 640
    Height = 400
    Map = None

    def __init__(self):
        pygame.init()
        self.DisplaySurface = pygame.display.set_mode((self.Width, self.Height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.Map = Map("example-map")
        self.Width = self.Map.width() * 32
        self.Height = self.Map.height() * 32
        self.DisplaySurface = pygame.display.set_mode((self.Width, self.Height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        while True:
            for event in pygame.event.get():
                self.eventHandler(event)
            self.render()
            pygame.display.update()

        pass

    def eventHandler(self, event):
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.USEREVENT:
            print("Tick")
        pass

    def render(self):
        for i in range(self.Map.width()):
            for j in range(self.Map.height()):
                tile = self.Map.tileAt(i,j)
                if tile != None:
                    self.DisplaySurface.blit(tile.PygameImage, (32*i,32*j))
        pass

if __name__ == "__main__" :
    mainWindow = GameWindow()