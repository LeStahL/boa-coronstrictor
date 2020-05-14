import pygame, json
from Tile import *

class Map:
    Layout = None
    Name = None
    Tiles = None

    def __init__(self):
        pass

    def __init__self(self, dirname):
        self.loadFromFilesystem(dirname)
        pass

    # load map from filesystem
    # @param dirname name of the directory inside maps/ containing the map. No slashes required.
    def loadFromFilesystem(self, dirname):
        JSONFileName = "maps/" + dirname + "/" + dirname + ".json"
        JSONFile = None
        with open(JSONFileName, "rt") as f:
            JSONFile = json.load(f)
            f.close()

        self.Name = JSONFile['name']
        self.Tiles = []
        for TileJSON in JSONFile['tiles']:
            self.tiles.append(Tile(TileJSON['name'], TileJSON['symbol'], TileJSON['file']))

        LayoutFileName = "maps/" + dirname + "/" + dirname + ".layout"
        with open(LayoutFileName, "rt") as f:
            self.Layout = f.read()
            f.close()
        
        pass
