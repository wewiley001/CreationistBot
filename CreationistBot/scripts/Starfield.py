import pyautogui
import time

pyautogui.PAUSE = 0.1  # Optional: adds slight pause between commands


# === Movement ===
def move_forward(duration=1):
    pyautogui.keyDown('w')
    time.sleep(duration)
    pyautogui.keyUp('w')

def move_backward(duration=1):
    pyautogui.keyDown('s')
    time.sleep(duration)
    pyautogui.keyUp('s')

def move_left(duration=1):
    pyautogui.keyDown('a')
    time.sleep(duration)
    pyautogui.keyUp('a')

def move_right(duration=1):
    pyautogui.keyDown('d')
    time.sleep(duration)
    pyautogui.keyUp('d')

def sprint(duration=1):
    pyautogui.keyDown('shift')
    pyautogui.keyDown('w')
    time.sleep(duration)
    pyautogui.keyUp('w')
    pyautogui.keyUp('shift')

def jump():
    pyautogui.press('space')

def crouch():
    pyautogui.press('ctrl')

# === Combat ===
def fire_weapon():
    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.mouseUp(button='left')

def aim_down_sights(duration=1):
    pyautogui.mouseDown(button='right')
    time.sleep(duration)
    pyautogui.mouseUp(button='right')

def reload():
    pyautogui.press('r')

def throw_grenade():
    pyautogui.press('g')

def melee():
    pyautogui.press('v')

def switch_weapon_scroll(up=True):
    pyautogui.scroll(1 if up else -1)

def switch_weapon_slot(slot=1):
    pyautogui.press(str(slot))

# === Interaction ===
def interact():
    pyautogui.press('e')

def holster_weapon():
    pyautogui.press('h')

def open_scanner():
    pyautogui.press('f')

def toggle_flashlight():
    pyautogui.press('l')

# === Menus ===
def open_inventory():
    pyautogui.press('i')

def open_map():
    pyautogui.press('m')

def open_missions():
    pyautogui.press('l')

def open_character_menu():
    pyautogui.press('tab')

def open_ship_menu():
    pyautogui.press('b')

def pause_menu():
    pyautogui.press('esc')

def quick_save():
    pyautogui.press('f5')

def quick_load():
    pyautogui.press('f9')

# === Scanner Action ===
def scan_ping():
    open_scanner()
    time.sleep(0.5)
    pyautogui.click()
