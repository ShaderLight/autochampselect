import pyautogui

def getlolwindow():
    win = pyautogui.getWindowsWithTitle('League of Legends')[0]

    return win