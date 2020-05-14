import pygame, random, datetime
from Map import *
from Tile import *

class Snake:
    def __init__(self, map):
        random.seed(datetime.now())
        self.Map = map
        self.ExtendVertically = random.choice([True,False])
        self.TailImage = pygame.image.load('tiles/snake-tail.png')
        self.BodyImage = pygame.image.load('tiles/snake-body.png')
        self.CornerImage = pygame.image.load('tiles/snake-body.png')
        self.HeadImage = pygame.image.load('tiles/snake-head.png')
        self.Segments = []

        # Spawn a random snake that is allowed
        

        pass

    def randomSnake(self):
        pos = [-1,-1]
        while not self.Map.tileAt(pos[0], pos[1]).Allowed:
            pos = []
        pass