import pyautogui
import time

def sky_move_forward(duration=1):
    pyautogui.keyDown('w')
    time.sleep(duration)
    pyautogui.keyUp('w')

def sky_move_back(duration=1):
    pyautogui.keyDown('s')
    time.sleep(duration)
    pyautogui.keyUp('s')

def sky_move_left(duration=1):
    pyautogui.keyDown('a')
    time.sleep(duration)
    pyautogui.keyUp('a')

def sky_move_right(duration=1):
    pyautogui.keyDown('d')
    time.sleep(duration)
    pyautogui.keyUp('d')

def sky_jump():
    pyautogui.press('space')

def sky_sneak():
    pyautogui.press('ctrl')

def sky_interact():
    pyautogui.press('e')

def sky_attack():
    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.mouseUp(button='left')

def sky_block():
    pyautogui.mouseDown(button='right')
    time.sleep(0.5)
    pyautogui.mouseUp(button='right')

def sky_shout():
    pyautogui.press('z')

def sky_favorites():
    pyautogui.press('q')

def sky_quicksave():
    pyautogui.press('f5')

def sky_quickload():
    pyautogui.press('f9')
