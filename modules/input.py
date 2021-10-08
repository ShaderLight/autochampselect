from pyautogui import locateCenterOnScreen, click, ImageNotFoundException

def accept_match():
    try:
        acceptxy = locateCenterOnScreen('buttons/accept.png', confidence = 0.5)
    except ImageNotFoundException:
        return -1

    if acceptxy == None:
        return -1

    click(acceptxy[0], acceptxy[1])
    return 0

def searchbox_input(text):
    pass
