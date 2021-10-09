from cv2 import getWindowImageRect
from pyautogui import getWindowsWithTitle

def getlolwindow():
    win = getWindowsWithTitle('League of Legends')[0]

    return win