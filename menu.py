import os
import glob
from utils import clearScreen, userInput, display, deleteFile
from play import tutorial

difficulty = 0      # 0 or 1
scriptDirPath = os.path.dirname(__file__)
saveFile = None

def newGame() :
    global saveFile
    savefiles = glob.glob(os.path.join(scriptDirPath, 'saves', '*'))
    saves = [os.path.basename(file) for file in savefiles]
    saves.extend(['-EMPTY-', '-EMPTY-', '-EMPTY-'])

    clearScreen()
    print(display['newgame']['name'], end='')
    name = input()

    if len(savefiles) == 3 :
        clearScreen()
        print(display['newgame']['saveerror'])
        while True :
            choice = userInput()
            if choice == 'y' :
                deleteSave(saves, True)
                break
            elif choice == 'n' :
                return 'back'

    clearScreen()
    print(display['newgame']['tutorial'].format(name))
    while True :
        choice = userInput()
        if choice == 'y' :
            tutorial()
            break
        elif choice == 'n' :
            break

    saveFile = os.path.join(scriptDirPath, 'saves', name)
    open(saveFile, 'x').close()
    return 'play'


def deleteSave(savelist, fromSaveError = False) :
    _invalid = ''
    while True :
        _1, _2, _3 = savelist[:3]
        clearScreen()
        print(display['deletesave'].format(_1, _2, _3) + _invalid)
        _invalid = ''

        choice = userInput()
        if choice not in '123b' :
            _invalid = '\n    [ Please choose valid option ]\n'
        elif choice == 'b' :
            break
        elif int(choice) > len(savelist)-3 :
            _invalid = '\n    [ This save file is empty ]\n'
        else :
            clearScreen()
            print(display['confirm'].format('DELETE'))
            while True :
                confirm = userInput()
                if confirm == 'n' :
                    break
                elif confirm == 'y' :
                    deleteFile(os.path.join(scriptDirPath, 'saves', savelist[int(choice)-1]))
                    savelist.pop(int(choice)-1)
                    if fromSaveError : return
                    break

    return savelist


def loadGame() :
    global saveFile
    _invalid = ''
    savefiles = glob.glob(os.path.join(scriptDirPath, 'saves', '*'))
    saves = [os.path.basename(file) for file in savefiles]
    saves.extend(['-EMPTY-', '-EMPTY-', '-EMPTY-'])

    while True :
        _1, _2, _3 = saves[:3]
        clearScreen()
        print(display['loadgame'].format(_1, _2, _3) + _invalid)
        _invalid = ''

        choice = userInput()
        if choice not in '123db' :
            _invalid = '\n    [ Please choose valid option ]\n'
        elif choice == 'd' :
            saves = deleteSave(saves)
        elif choice == 'b' :
            return 'back'
        elif int(choice) > len(savefiles) :
            _invalid = '\n    [ This save file is empty ]\n'
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
    print(display['confirm'].format('QUIT'))

    if userInput() == 'y':
        return 'quit'
    else:
        return 'back'
