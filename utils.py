import os
from msvcrt import getch

clearScreen = lambda : os.system('cls')
userInput = lambda : getch().decode()

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
    'loadgame' : '\n'
                 '     __________________________\n'
                 '    |\n'
                 '    |    CHOOSE SAVE FILE\n'
                 '    |\n'
                 '    |    (1)  {}\n'
                 '    |    (2)  {}\n'
                 '    |    (3)  {}\n'
                 '    |\n'
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
    'quitgame' : '\n'
                 '     __________________________\n'
                 '    |\n'
                 '    |        QUIT\n'
                 '    |    Are you sure?\n'
                 '    |\n'
                 '    |      Y      N\n'
                 '    |\n'
                 '    |\n'
}