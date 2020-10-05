import os
from msvcrt import getch

clearScreen = lambda : os.system('cls')
userInput = lambda : getch().decode()
difficulty = 0      # 0 or 1
saveFile = None

def newGame() :
    pass


def loadGame() :
    pass


def difficultyLevel() :
    global difficulty
    _error = ''
    while True :
        clearScreen()
        print('\n     __________________________\n    |\n' +
              '    |    CHOOSE DIFFICULTY \n    |\n' +
              '    |    Easy    (e)\n' +
              '    |    Hard    (h)\n    |\n' +
              '    |    Back    (b)\n' +
              '    |\n    |\n' +
              _error,
              end='')

        print('\n    [ Enter your choice ]\n')
        choice = userInput()
        if choice == 'e' :
            difficulty = 0; return 'diff0'
        elif choice == 'h' :
            difficulty = 1; return 'diff1'
        elif choice == 'h':
            return 'back'
        else :
            _error = '\n    [ Please choose valid option ]\n'


def quitGame() :
    clearScreen()
    print('\n     __________________________\n    |\n' +
          '    |    Are you sure?\n    |\n' +
          '    |      Y      N\n' +
          '    |\n    |\n',
          end='')

    print('\n    [ Enter your choice ]\n')
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
    while True :
        clearScreen()
        print('\n     __________________________\n    |\n'+
              '    |        10 HALLS\n    |\n'+
              '    |    (n)  NEW GAME\n'+
              '    |    (l)  LOAD GAME\n'+
              '    |    (d)  DIFFICULTY\n'+
              '    |    (q)  QUIT\n'+
              '    |\n    |\n',
              end='')

        print('\n    [ Enter your choice ]\n')
        result = menuOptions[userInput()]()

        if result == 'quit' :
            clearScreen(); return 0
        elif result == 'play' :
            return 1
        elif result == 'back' :
            continue


if __name__ == '__main__' :
    if mainMenu() :
        # playGame(saveFile)
        pass