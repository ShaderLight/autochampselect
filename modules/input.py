from pyautogui import locateCenterOnScreen, click, ImageNotFoundException
from .isrunning import isrunning
import logging
from time import sleep

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

def searchbox_input(text):
    pass
