import os
import glob
from utils import clearScreen, userInput, display
from play import tutorial

difficulty = 0      # 0 or 1
scriptDirPath = os.path.dirname(__file__)
saveFile = None


def newGame() :
    tutorial()

    return 'play'


def loadGame() :
    # TODO - Include an option to delete a save file
    global saveFile
    _invalid = ''
    savefiles = glob.glob(scriptDirPath + '/saves/*')
    saves = [os.path.basename(file) for file in savefiles]
    saves.extend(['-EMPTY-', '-EMPTY-', '-EMPTY-'])
    _1, _2, _3 = saves[:3]

    while True :
        clearScreen()
        print(display['loadgame'].format(_1, _2, _3) + _invalid)

        print('    [ Enter your choice ]\n')
        choice = userInput()
        if choice not in '123b' :
            _invalid = '\n    [ Please choose valid option ]\n'
            continue
        elif choice == 'b' :
            return 'back'
        elif int(choice) > len(savefiles) :
            _invalid = '\n    [ This save file is empty ]\n'
            continue
        else :
            saveFile = savefiles[int(choice)-1]
            return 'play'


def difficultyLevel() :
    global difficulty
    _invalid = ''
    indicator = [['>', ' '],    # easy
                 [' ', '>']]    # hard

    while True :
        clearScreen()
        print(display['difficultylevel'].format(indicator[0][difficulty], indicator[1][difficulty]) + _invalid)

        print('    [ Enter your choice ]\n')
        choice = userInput()
        if choice == 'e' :
            difficulty = 0
        elif choice == 'h' :
            difficulty = 1
        elif choice == 'b' :
            return 'back'
        else :
            _invalid = '\n    [ Please choose valid option ]\n'


def quitGame() :
    clearScreen()
    print(display['quitgame'])

    print('    [ Enter your choice ]\n')
    if userInput() == 'y':
        return 'quit'
    else:
        return 'back'
