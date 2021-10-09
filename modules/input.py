from pyautogui import locateCenterOnScreen, click, ImageNotFoundException, getWindowsWithTitle, write
import pyautogui
from .isrunning import isrunning
import logging
from time import sleep

SELECT_X_RATIO = 309/1024
SELECT_Y_RATIO = 132/576

SEARCH_X_RATIO = 615/1024
SEARCH_Y_RATIO = 83/576

DODGE_FLAG = False

def pre_match_loop(window, with_ban_phase, selection):
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
    if with_ban_phase:
        ban_loop(window, with_ban_phase, selection)
    else:
        pick_loop(window, with_ban_phase, selection)


def ban_loop(window, with_ban_phase, selection):
    logging.debug('Entering ban loop')
    DODGE_FLAG = False
    while isrunning('LeagueClientUx.exe'):
        window.update()
        if accept_match() == 0:
            DODGE_FLAG = True
            break
        try:
            banxy = locateCenterOnScreen('buttons/ban.png', confidence = 0.7)
        except ImageNotFoundException:
            sleep(1)
            continue
        if banxy == None:
            sleep(1)
            continue
        
        win = getlolwindow()
        searchbox_input(win, selection['ban'])
        selectchamp(win)
        logging.debug('Clicking ban button')
        click_ban()
        break

    if DODGE_FLAG:
        DODGE_FLAG = False
        if isrunning('LeagueClientUx.exe'):
            return ban_loop(window, with_ban_phase, selection)
    
    if isrunning('LeagueClientUx.exe'):
        return pick_loop(window, with_ban_phase, selection)


def pick_loop(window, with_ban_phase, selection):
    logging.debug('Entering pick loop')
    DODGE_FLAG = False
    while isrunning('LeagueClientUx.exe'):
        window.update()
        if accept_match() == 0:
            DODGE_FLAG = True
            break
        try:
            pickxy = locateCenterOnScreen('buttons/lockin.png', confidence = 0.7)
        except ImageNotFoundException:
            sleep(1)
            continue

        if pickxy == None:
            sleep(1)
            continue

        win = getlolwindow()
        searchbox_input(win, selection['pick'])
        selectchamp(win)
        logging.debug('Clicking pick button')
        click_pick()
        break

    if DODGE_FLAG:
        DODGE_FLAG = False
        return pre_match_loop(window, with_ban_phase, selection)

    if with_ban_phase and isrunning('LeagueClientUx.exe'):
        return ban_loop(window, with_ban_phase, selection)
    elif not with_ban_phase and isrunning('LeagueClientUx.exe'):
        return pick_loop(window, with_ban_phase, selection)


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
    champ_x = win.size.width * SEARCH_X_RATIO
    champ_y = win.size.height * SEARCH_Y_RATIO

    logging.debug('Inputting: {}'.format(text))
    click(win.left + champ_x, win.top + champ_y)
    write(text, interval=0.1)

    return 0


def getlolwindow():
    win = getWindowsWithTitle('League of Legends')[0]
    logging.debug('LoL window: {}'.format(win.size))
    return win


def click_ban():
    try:
        banxy = locateCenterOnScreen('buttons/ban.png', confidence=0.7)
    except ImageNotFoundException:
        return -1
    
    if banxy == None:
        return -1

    click(banxy[0], banxy[1])
    return 0

def click_pick():
    try:
        pickxy = locateCenterOnScreen('buttons/lockin.png', confidence=0.7)
    except ImageNotFoundException:
        return -1
    
    if pickxy == None:
        return -1

    click(pickxy[0], pickxy[1])
    return 0

def selectchamp(win):
    champ_x = win.size.width * SELECT_X_RATIO
    champ_y = win.size.height * SELECT_Y_RATIO

    click(win.left + champ_x, win.top + champ_y)

    return 0