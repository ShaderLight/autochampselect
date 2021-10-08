from pyautogui import locateCenterOnScreen, click, ImageNotFoundException
from modules.isrunning import isrunning

def pre_match_loop():
    while isrunning('LeagueClientUx.exe'):
        if accept_match() == -1:
            logging.debug('Match accepting failed, retrying...')
            sleep(3)
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
