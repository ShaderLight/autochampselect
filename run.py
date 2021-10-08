import pyautogui
from pyscreeze import ImageNotFoundException
from modules.isrunning import isrunning
from time import sleep

while True:
    try:
        acceptxy = pyautogui.locateOnScreen('buttons/accept.png', confidence = 0.5)
        if acceptxy == None:
            sleep(1)
            continue

    except ImageNotFoundException:
        sleep(1)
        continue

    pyautogui.click(acceptxy[0], acceptxy[1])
    break