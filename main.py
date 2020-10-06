import os
from msvcrt import getch
# import pickle
import glob

clearScreen = lambda : os.system('cls')
userInput = lambda : getch().decode()
difficulty = 0      # 0 or 1
saveFile = None
scriptDirPath = os.path.dirname(__file__)

def newGame() :
    pass


def loadGame() :
    # TODO - Include an option to delete a save file
    display = '\n     __________________________\n    |\n' + \
              '    |    CHOOSE SAVE FILE\n    |\n' + \
              '    |    (1)  {}\n' + \
              '    |    (2)  {}\n' + \
              '    |    (3)  {}\n    |\n' + \
              '    |    (b)  Back\n' + \
              '    |\n    |\n'

    global saveFile
    _invalid = ''
    savefiles = glob.glob(scriptDirPath + '/saves/*')
    saves = [os.path.basename(file) for file in savefiles]
    saves.extend(['-EMPTY-', '-EMPTY-', '-EMPTY-'])
    _1, _2, _3 = saves[:3]

    while True :
        clearScreen()
        print(display.format(_1, _2, _3) + _invalid)

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
    display = '\n     __________________________\n    |\n' + \
              '    |    CHOOSE DIFFICULTY\n    |\n' + \
              '    |  {} (e)  Easy\n' + \
              '    |  {} (h)  Hard\n    |\n' + \
              '    |    (b)  Back\n' + \
              '    |\n    |\n'

    global difficulty
    _invalid = ''
    indicator = [['>', ' '],    # easy
                 [' ', '>']]    # hard

    while True :
        clearScreen()
        print(display.format(indicator[0][difficulty], indicator[1][difficulty]) + _invalid)

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
    display = '\n     __________________________\n    |\n' + \
              '    |    Are you sure?\n    |\n' + \
              '    |      Y      N\n' + \
              '    |\n    |\n'

    clearScreen()
    print(display)

    print('    [ Enter your choice ]\n')
    if userInput() == 'y':
        return 'quit'
    else:
        return 'back'


menuOptions = {
    'n': newGame,
    'l': loadGame,
    'd': difficultyLevel,
    'q': quitGame
}

def mainMenu() :
    # TODO - Separate the title and Main Menu screens
    display = '\n     __________________________\n    |\n'+ \
              '    |        10 HALLS\n    |\n'+ \
              '    |    (n)  NEW GAME\n'+ \
              '    |    (l)  LOAD GAME\n'+ \
              '    |    (d)  DIFFICULTY\n'+ \
              '    |    (q)  QUIT\n'+ \
              '    |\n    |\n'

    while True :
        clearScreen()
        print(display)

        print('    [ Enter your choice ]\n')
        result = menuOptions[userInput()]()

        if result == 'quit' :
            clearScreen(); return 0
        elif result == 'play' :
            return 1
        elif result == 'back' :
            continue


if __name__ == '__main__' :
    if 'saves' not in os.listdir() :
        os.mkdir(os.path.join(scriptDirPath, 'saves'))

    if mainMenu() :
        print(saveFile)
        # playGame(saveFile)
        pass
