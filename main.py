def newGame() :
    pass

def loadGame() :
    pass

def difficultyLevel() :
    pass

def quitGame() :
    pass

menuOptions = {
    'n': newGame, 'N': newGame,
    'l': loadGame, 'L': loadGame,
    'd': difficultyLevel, 'D': difficultyLevel,
    'q': quitGame, 'Q': quitGame
}


def mainMenu() :

    print('\n     __________________________\n    |\n'+
          '    |        10 HALLS\n    |\n'+
          '    |    (n)  NEW GAME\n'+
          '    |    (l)  LOAD GAME\n'+
          '    |    (d)  DIFFICULTY\n'+
          '    |    (q)  QUIT\n'+
          '    |\n    |\n',
          end='')

    choice = input("\n    [ Enter your choice ]\n    ")
    menuOptions[choice]()

if __name__ == '__main__' :
    mainMenu()
