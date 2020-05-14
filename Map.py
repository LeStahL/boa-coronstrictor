import pygame, json
from Tile import *

class Map:
    Layout = None
    Name = None
    Tiles = None

    def __init__(self):
        pass

    def __init__(self, dirname):
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
            self.Tiles.append(Tile(TileJSON['name'], TileJSON['symbol'], TileJSON['file'], TileJSON['accessible']))

        LayoutFileName = "maps/" + dirname + "/" + dirname + ".layout"
        with open(LayoutFileName, "rt") as f:
            self.Layout = f.read()
            f.close()

        pass

    # Gives the width of the map
    def width(self):
        if(self.Layout == None):
            return 0
        return len(self.Layout.split('\n')[0])

    # Gives the height of the map
    def height(self):
        if(self.Layout == None):
            return 0
        return len(self.Layout.split('\n'))

    # Returns the specific tile at position (x,y)
    def tileAt(self, x, y):
        tileSymbol = self.Layout.split("\n")[y][x]
        for tile in self.Tiles:
            if tile.Symbol == tileSymbol:
                return tile
        return None

    # Returns a list of adjacent tiles for a given position (x,y)
    def adjacentTiles(self,x,y):
        ret = []
        tile = self.tileAt(x+1,y)
        if tile != None: 
            ret.append(tile)
        tile = self.tileAt(x, y+1)
        if tile != None:
            ret.append(tile)
        tile = self.tileAt(x-1,y)
        if tile != None:
            ret.append(tile)
        tile = self.tileAt(x,y-1)
        if tile != None:
            ret.append(tile)
        return ret
    