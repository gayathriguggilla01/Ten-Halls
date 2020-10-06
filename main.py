import os
from menu import newGame, loadGame, difficultyLevel, quitGame, scriptDirPath
from play import playGame
from utils import clearScreen, userInput, display


menuOptions = {
    'n': newGame,
    'l': loadGame,
    'd': difficultyLevel,
    'q': quitGame
}


def mainMenu() :
    print(display['title'])
    while True :
        if userInput() == 's' : break

    while True :
        clearScreen()
        print(display['mainmenu'])

        print('    [ Enter your choice ]\n')
        result = menuOptions[userInput()]()

        if result == 'quit' :
            clearScreen(); return False
        elif result == 'play' :
            return True
        elif result == 'back' :
            continue


# TODO - Open a separate console / window for displaying the output
if __name__ == '__main__' :
    if 'saves' not in os.listdir() :
        os.mkdir(os.path.join(scriptDirPath, 'saves'))

    if mainMenu() :
        from menu import saveFile
        playGame(saveFile)
        pass
