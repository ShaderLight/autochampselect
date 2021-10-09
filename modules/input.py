from pyautogui import locateCenterOnScreen, click, ImageNotFoundException, getWindowsWithTitle, write
import pyautogui
from .isrunning import isrunning
import logging
from time import sleep

SELECT_X_RATIO = 309/1024
SELECT_Y_RATIO = 132/576

SEARCH_X_RATIO = 615/1024
SEARCH_Y_RATIO = 83/576

def pre_match_loop(window):
    while isrunning('LeagueClientUx.exe'):
        window.update()
        if accept_match() == -1:
            logging.debug('Match accepting failed, retrying...')
            for i in range(6):
                window.update()
                sleep(0.5)
            continue
        else:
            logging.debug('Match accepted!')
            break


def accept_match():
    try:
        acceptxy = locateCenterOnScreen('buttons/accept.png', confidence = 0.7)
    except ImageNotFoundException:
        return -1

    if acceptxy == None:
        return -1

    click(acceptxy[0], acceptxy[1])
    return 0

def searchbox_input(win, text):
    champ_x = win.size.width * SELECT_X_RATIO
    champ_y = win.size.height * SELECT_Y_RATIO

    win.clickRel(x=champ_x, y=champ_y)
    write(text, interval=0.1)

    return 0

def getlolwindow():
    win = getWindowsWithTitle('League of Legends')[0]
    logging.debug('LoL window: {}'.format(win.size))
    return win

def click_pickban():
    pass

def selectchamp(win):
    champ_x = win.size.width * SELECT_X_RATIO
    champ_y = win.size.height * SELECT_Y_RATIO

    win.clickRel(x=champ_x, y=champ_y)

    return 0