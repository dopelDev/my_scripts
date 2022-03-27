#!/home/dopel/venv/scripts/bin/python3.9
################################################
#       __                 ______
#  ____/ /___  ____  ___  / / __ \___ _   __
# / __  / __ \/ __ \/ _ \/ / / / / _ \ | / /
#/ /_/ / /_/ / /_/ /  __/ / /_/ /  __/ |/ /
#\__,_/\____/ .___/\___/_/_____/\___/|___/
#          /_/
#
################################################
#Date : Fri 01 Jan 2021 07:17:08 PM -05
#GitHub :  https://github.com/dopelDev
#Facebook : https://www.facebook.com/profile.php?id=100036185774355
#Mail : 322kuroneko2@gmail.com
#Description :
#Version Note: espacios entre appends
#issue : no captura mas de una pantalla de terminal
################################################
"""
    version beta 0.0.4.2
"""
from pyperclip import paste, copy
from sys import argv
import curses
from random import randrange
from os import path

def fileNameOut(params):
    # entrada de params
    # option a (append)
    if len(params) == 1:
        fileName = str(randrange(100036185774355))
        objfile = open(fileName, mode='w')
    elif len(params) == 2:
        fileName = params[1]
        objfile = open(fileName, mode='w')
    elif len(params) == 3 and params[2] == '-a':
        if path.exists(params[1]):
            fileName = params[1]
            objfile = open(fileName, mode='a')
        else:
            print('file no exists')
            exit()

    return objfile

def writeFile(list2Write, objfile):
    if len(list2Write) > 0 and list2Write != None:
        for index, line in enumerate(list2Write):
            if objfile.tell() != 0:
                objfile.writelines('\n\n')
            if index < len(list2Write) - 1:
                objfile.writelines(line)
                objfile.writelines('\n')
            else:
                objfile.writelines(line)
        objfile.close()

def main(params):
    objfile = fileNameOut(params)
    list2Write = copyAndShow()
    writeFile(list2Write, objfile)


def copyAndShow():
    stdscr = curses.initscr()
    curses.curs_set(False)
    curses.noecho()
    curses.cbreak()
    tmp = ''
    newTmp = ''
    copy(newTmp)
    list2Write = []
    height, widght = stdscr.getmaxyx()
    stdscr.addstr(0, round(widght/2), 'aqui comienza')
    stdscr.refresh()
    while True:
        newTmp = paste()
        if tmp != newTmp:
            tmp = newTmp
            list2Write.append(tmp)
            stdscr.clear()
            stdscr.addstr(2, 0, tmp)
        stdscr.refresh()
        stdscr.nodelay(True)
        key = stdscr.getch()
        if key == ord('q'):
            break
    curses.curs_set(True)
    curses.echo()
    curses.nocbreak()
    curses.endwin()

    return list2Write

if __name__ == '__main__':
    params = argv
    main(params=params)
