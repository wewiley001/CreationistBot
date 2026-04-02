# CreationistBot

A PyQt5 desktop GUI for automating keyboard and mouse inputs in Bethesda games using `pyautogui`. Select a game script, queue up actions, and execute them with optional delays and looping.

## Supported Games

| Script | Game |
|---|---|
| `Fallout4.py` | Fallout 4 |
| `OblivionRemastered.py` | The Elder Scrolls IV: Oblivion Remastered |
| `Skyrim.py` | The Elder Scrolls V: Skyrim |
| `Starfield.py` | Starfield |

## Requirements

- Python 3.x
- [PyQt5](https://pypi.org/project/PyQt5/)
- [pyautogui](https://pypi.org/project/pyautogui/)

Install dependencies:

```bash
pip install PyQt5 pyautogui
```

## Usage

```bash
python main.py
```

1. **Choose Game Script** — select a game from the dropdown.
2. **Select Function** — pick an action from the list of available functions in that script.
3. **Confirm Selection** — adds the action to the queue.
4. Repeat steps 2–3 to build a multi-step queue.
5. **Wait before execution** — optionally set a delay (seconds) before the queue starts.
6. **Loop queue continuously** — check to repeat the queue indefinitely.
7. **Run Queue** — executes all queued actions in order.
8. **Clear Queue** — resets the queue and log.

The **Execution Log** displays real-time status with color-coded output:
- **Cyan** — action started
- **Green** — action completed successfully
- **Red** — error or exception

## Project Structure

```
CreationistBot/
├── main.py                   # PyQt5 GUI application
└── scripts/
    ├── Fallout4.py           # Fallout 4 input actions
    ├── OblivionRemastered.py # Oblivion Remastered input actions
    ├── Skyrim.py             # Skyrim input actions
    └── Starfield.py          # Starfield input actions
```

## Script Functions

### Fallout4.py
| Function | Description |
|---|---|
| `fo_move_forward` | Hold `W` to move forward |
| `fo_move_back` | Hold `S` to move backward |
| `fo_move_left` | Hold `A` to strafe left |
| `fo_move_right` | Hold `D` to strafe right |
| `fo_jump` | Press `Space` to jump |
| `fo_crouch` | Press `Ctrl` to crouch |
| `fo_interact` | Press `E` to interact |
| `fo_attack` | Left-click to attack |
| `fo_aim` | Right-click to aim down sights |
| `fo_reload` | Press `R` to reload |
| `fo_grenade` | Press `G` to throw grenade |
| `fo_pipboy` | Press `Tab` to open Pip-Boy |
| `fo_vats` | Press `Q` to activate VATS |
| `fo_quicksave` | Press `F5` to quick save |

### OblivionRemastered.py
| Function | Description |
|---|---|
| `ob_move_forward` | Hold `W` to move forward |
| `ob_move_back` | Hold `S` to move backward |
| `ob_strafe_left` | Hold `A` to strafe left |
| `ob_strafe_right` | Hold `D` to strafe right |
| `ob_jump` | Press `Space` to jump |
| `ob_sneak` | Press `C` to toggle sneak |
| `ob_interact` | Press `E` to interact |
| `ob_attack` | Left-click to attack |
| `ob_block` | Right-click to block |
| `ob_inventory` | Press `Tab` to open inventory |
| `ob_map` | Press `M` to open map |
| `ob_quicksave` | Press `F5` to quick save |
| `ob_quickload` | Press `F9` to quick load |

### Skyrim.py
| Function | Description |
|---|---|
| `sky_move_forward` | Hold `W` to move forward |
| `sky_move_back` | Hold `S` to move backward |
| `sky_move_left` | Hold `A` to strafe left |
| `sky_move_right` | Hold `D` to strafe right |
| `sky_jump` | Press `Space` to jump |
| `sky_sneak` | Press `Ctrl` to toggle sneak |
| `sky_interact` | Press `E` to interact |
| `sky_attack` | Left-click to attack |
| `sky_block` | Right-click to block |
| `sky_shout` | Press `Z` to shout |
| `sky_favorites` | Press `Q` to open favorites |
| `sky_quicksave` | Press `F5` to quick save |
| `sky_quickload` | Press `F9` to quick load |

### Starfield.py
| Function | Description |
|---|---|
| `move_forward` | Hold `W` to move forward |
| `move_backward` | Hold `S` to move backward |
| `move_left` | Hold `A` to strafe left |
| `move_right` | Hold `D` to strafe right |
| `sprint` | Hold `Shift+W` to sprint |
| `jump` | Press `Space` to jump |
| `crouch` | Press `Ctrl` to crouch |
| `fire_weapon` | Left-click to fire |
| `aim_down_sights` | Right-click to aim |
| `reload` | Press `R` to reload |
| `throw_grenade` | Press `G` to throw grenade |
| `melee` | Press `V` for melee attack |
| `switch_weapon_scroll` | Scroll to switch weapon |
| `switch_weapon_slot` | Press number key to switch weapon slot |
| `interact` | Press `E` to interact |
| `holster_weapon` | Press `H` to holster |
| `open_scanner` | Press `F` to open scanner |
| `toggle_flashlight` | Press `L` to toggle flashlight |
| `open_inventory` | Press `I` to open inventory |
| `open_map` | Press `M` to open map |
| `open_missions` | Press `L` to open missions |
| `open_character_menu` | Press `Tab` to open character menu |
| `open_ship_menu` | Press `B` to open ship menu |
| `pause_menu` | Press `Esc` to pause |
| `quick_save` | Press `F5` to quick save |
| `quick_load` | Press `F9` to quick load |
| `scan_ping` | Open scanner and click to ping |

## Adding a New Game Script

1. Create a new `.py` file in the `scripts/` folder.
2. Define functions using `pyautogui` for the desired inputs.
3. Restart the app — the new script will appear automatically in the dropdown.
