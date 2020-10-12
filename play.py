import numpy as np
from utils import clearScreen, userInput

#       player, wall, floor, enemy, NPC
MapTiles = ['O', '#', '.', 'X', '@']
LvlUpXP = np.array([10, 30, 60, 100, 150, 210, 270, 340, 420, 500], dtype=int)

class Map :
    def __init__(self, save=None, hall=0, mapsize=20, tut=False) :
        self.hall = None
        self.mapSize = None
        self.mapGrid = None
        self.pXY = None
        self.enemies = None
        if tut :
            self.initTut()
        elif save :
            self.initSave(save)
        else :
            self.initDefault(hall, mapsize)

    def initTut(self) :
        self.mapGrid = np.genfromtxt('tutorial.csv', delimiter=',', dtype=int)
        self.mapSize = len(self.mapGrid)
        self.pXY = np.argwhere(self.mapGrid == 0)[0]
        self.enemies = list(np.argwhere(self.mapGrid == 3))

    def initSave(self, savefile) :
        pass

    def initDefault(self, hall, mapsize) :      # figure out later on
        self.mapSize = mapsize
        self.mapGrid = np.zeros(mapsize, dtype=int)
        self.hall = hall
        self.pXY = np.argwhere(self.mapGrid == 0)[0]
        self.enemies = list(np.argwhere(self.mapGrid == 3))

    def update(self) :
        maptiles = np.vectorize(lambda x : MapTiles[x])
        mapgrid_1d = maptiles(self.mapGrid).flatten()
        N = self.mapSize; num_ = 3*N + 2
        mapDisplay = ' '+'_'*num_+' \n' + \
                     '|'+' '*num_+'|\n' + \
                     ('|' + '  {}'*N + '  |\n')*N + \
                     ' '+'_'*num_+' '
        print(mapDisplay.format(*mapgrid_1d))

# TODO - add items to the player
class Player :
    def __init__(self, name, save=None) :
        self.Name = name
        self.HP = None
        self.stats = None
        self.XP = None
        self.currentMap = None
        if save :
            self.initSave(save)
        else :
            self.initDefault()

    def initSave(self, savefile) :
        pass

    def initDefault(self) :
        self.HP = 100
        self.stats = {
            'attack': 5,
            'defense': 5,
            'speed': 5
        }
        self.XP = 0

    def linkMap(self, currentmap) :
        self.currentMap = currentmap

    def move(self, userinput) :
        mapgrid = self.currentMap.mapGrid
        pxy = self.currentMap.pXY; px, py = pxy
        inputKey_to_arrayChange = dict(w=(-1,0),s=(1,0),a=(0,-1),d=(0,1))
        dx,dy = inputKey_to_arrayChange[userinput]
        if mapgrid[px+dx][py+dy] == 2 :
            mapgrid[px][py], mapgrid[px+dx][py+dy] = 2, 0
            pxy[0] += dx; pxy[1] += dy


def tutorial() :
    tutplayer = Player('Tutorial')
    tutmap = Map(tut=True)
    tutplayer.linkMap(tutmap)
    while True :
        clearScreen()
        tutmap.update()
        choice = userInput()
        if choice == 'q' :
            break
        else :
            tutplayer.move(choice)

    del tutmap, tutplayer

def playGame(savefile) :
    clearScreen()
    print('yet to design LOL')
    print(savefile)