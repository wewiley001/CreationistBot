import pyautogui
import time

def ob_move_forward(duration=1):
    pyautogui.keyDown('w')
    time.sleep(duration)
    pyautogui.keyUp('w')

def ob_move_back(duration=1):
    pyautogui.keyDown('s')
    time.sleep(duration)
    pyautogui.keyUp('s')

def ob_strafe_left(duration=1):
    pyautogui.keyDown('a')
    time.sleep(duration)
    pyautogui.keyUp('a')

def ob_strafe_right(duration=1):
    pyautogui.keyDown('d')
    time.sleep(duration)
    pyautogui.keyUp('d')

def ob_jump():
    pyautogui.press('space')

def ob_sneak():
    pyautogui.press('c')

def ob_interact():
    pyautogui.press('e')

def ob_attack():
    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.mouseUp(button='left')

def ob_block():
    pyautogui.mouseDown(button='right')
    time.sleep(0.5)
    pyautogui.mouseUp(button='right')

def ob_inventory():
    pyautogui.press('tab')

def ob_map():
    pyautogui.press('m')

def ob_quicksave():
    pyautogui.press('f5')

def ob_quickload():
    pyautogui.press('f9')
