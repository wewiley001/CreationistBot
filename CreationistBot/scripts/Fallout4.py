import pyautogui
import time

def fo_move_forward(duration=1):
    pyautogui.keyDown('w')
    time.sleep(duration)
    pyautogui.keyUp('w')

def fo_move_back(duration=1):
    pyautogui.keyDown('s')
    time.sleep(duration)
    pyautogui.keyUp('s')

def fo_move_left(duration=1):
    pyautogui.keyDown('a')
    time.sleep(duration)
    pyautogui.keyUp('a')

def fo_move_right(duration=1):
    pyautogui.keyDown('d')
    time.sleep(duration)
    pyautogui.keyUp('d')

def fo_jump():
    pyautogui.press('space')

def fo_crouch():
    pyautogui.press('ctrl')

def fo_interact():
    pyautogui.press('e')

def fo_attack():
    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.mouseUp(button='left')

def fo_aim():
    pyautogui.mouseDown(button='right')
    time.sleep(1)
    pyautogui.mouseUp(button='right')

def fo_reload():
    pyautogui.press('r')

def fo_grenade():
    pyautogui.press('g')

def fo_pipboy():
    pyautogui.press('tab')

def fo_vats():
    pyautogui.press('q')

def fo_quicksave():
    pyautogui.press('f5')
