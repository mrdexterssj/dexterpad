print("Starting CircuitPython with KMK firmware")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from digitalio import DigitalInOut
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from statusled import statusLED

macropad = KMKKeyboard()
macropad.modules.append(Layers())
macropad.extensions.append(MediaKeys())

encoder_handler = EncoderHandler()
macropad.modules.append(encoder_handler)

status_led = statusLED(led_pins=[board.GP0, board.GP1, board.GP2, board.GP11])
macropad.extensions.append(status_led)

macropad.col_pins = (board.GP6, board.GP5, board.GP4)
macropad.row_pins = (board.GP1, board.GP2, board.GP3,)
macropad.diode_orientation = DiodeOrientation.COL2ROW

#4 keymaps (2 assigned for now)
macropad.keymap = [
    #Default: F13 to F21
    [
    KC.F13, KC.F14, KC.F15,
    KC.F16, KC.F17, KC.F18,
    KC.F19, KC.F20, KC.F21
    ],
    #Minecraft: F6 to F10, F12 to F15
    [
    KC.F6, KC.F7, KC.F8,
    KC.F9, KC.F10, KC.F12,
    KC.F13, KC.F14, KC.F15
    ],
    #Unassgined 3
    [
    KC.F13, KC.F14, KC.F15,
    KC.F16, KC.F17, KC.F18,
    KC.F19, KC.F20, KC.F21
    ],
    #Unassigned 4
    [
    KC.F13, KC.F14, KC.F15,
    KC.F16, KC.F17, KC.F18,
    KC.F19, KC.F20, KC.F21
    ]
]


#Note to self: remember to check divisor when the keypad is ready
encoder_handler.pins = (
    (board.GP11, board.GP12, board.GP13), #Turn A, Turn B, Push
)

encoder_handler.map = [
    ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.MEDIA_PLAY_PAUSE)),
    ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.MEDIA_PLAY_PAUSE)),
    ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.MEDIA_PLAY_PAUSE)),
    ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.MEDIA_PLAY_PAUSE)),
]

#Pending: add hold to switch functionality

if __name__ == "__main__":
    macropad.go()