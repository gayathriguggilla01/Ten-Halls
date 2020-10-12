import os
import platform

deleteFile = lambda filepath : os.remove(filepath)

OS = platform.system()
if OS == 'Windows' :
    from msvcrt import getch
    clearScreen = lambda : os.system('cls')
    userInput = lambda: getch().decode()
elif OS == 'Linux' :
    from getch import getch
    clearScreen = lambda : os.system('clear')
    userInput = lambda: getch()

def createSaveFile() :
    pass

display = {
    'title' : '\n'
              '     __________________________\n'
              '    |\n'
              '    |          T E N\n'
              '    |        H A L L S\n'
              '    |\n'
              '    |        (s) START\n'
              '    |\n'
              '    |\n',
    'mainmenu' : '\n'
                 '     __________________________\n'
                 '    |\n'
                 '    |       MAIN MENU\n'
                 '    |\n'
                 '    |    (n)  NEW GAME\n'
                 '    |    (l)  LOAD GAME\n'
                 '    |    (d)  DIFFICULTY\n'
                 '    |    (q)  QUIT\n'
                 '    |\n'
                 '    |\n',
    'newgame' : {
        'name' : '\n'
                 '     __________________________\n'
                 '    |\n'
                 '    |     CHARACTER NAME\n'
                 '    |\n'
                 '    |    Please enter your\n'
                 '    |    character\'s name\n'
                 '    |\n'
                 '    |    ',
        'saveerror' : '\n'
                      '     __________________________\n'
                      '    |\n'
                      '    |     SAVE SLOTS FULL\n'
                      '    |\n'
                      '    |    3 save files found.\n'
                      '    |       Delete one?\n'
                      '    |\n'
                      '    |        Y      N\n'
                      '    |\n'
                      '    |\n',
        'tutorial' : '\n'
                     '     __________________________\n'
                     '    |\n'
                     '    |    TUTORIAL : {}\n'
                     '    |\n'
                     '    |    Would you like to\n'
                     '    |    play the tutorial?\n'
                     '    |\n'
                     '    |        Y      N\n'
                     '    |\n'
                     '    |\n'
    },
    'deletesave' : '\n'
                   '     __________________________\n'
                   '    |\n'
                   '    |    DELETE SAVE FILE\n'
                   '    |\n'
                   '    |    (1)  {}\n'
                   '    |    (2)  {}\n'
                   '    |    (3)  {}\n'
                   '    |\n'
                   '    |    (b)  Back\n'
                   '    |\n'
                   '    |\n',
    'loadgame' : '\n'
                 '     __________________________\n'
                 '    |\n'
                 '    |    CHOOSE SAVE FILE\n'
                 '    |\n'
                 '    |    (1)  {}\n'
                 '    |    (2)  {}\n'
                 '    |    (3)  {}\n'
                 '    |\n'
                 '    |    (d)  Delete\n'
                 '    |    (b)  Back\n'
                 '    |\n'
                 '    |\n',
    'difficultylevel' : '\n'
                        '     __________________________\n'
                        '    |\n'
                        '    |    CHOOSE DIFFICULTY\n'
                        '    |\n'
                        '    |  {} (e)  Easy\n'
                        '    |  {} (h)  Hard\n'
                        '    |\n'
                        '    |    (b)  Back\n'
                        '    |\n'
                        '    |\n',
    'confirm' : '\n'
                 '     __________________________\n'
                 '    |\n'
                 '    |       {}\n'
                 '    |    Are you sure?\n'
                 '    |\n'
                 '    |      Y      N\n'
                 '    |\n'
                 '    |\n'
}