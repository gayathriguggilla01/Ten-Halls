from utils import clearScreen, userInput
from classes import Map, Player

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
        elif choice in 'wasd' :
            tutplayer.move(choice)

    del tutmap, tutplayer


def playGame(savefile) :
    clearScreen()
    print('yet to design LOL')
    print(savefile)