import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# Map keys
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D6)
keyboard.row_pins = ()
keyboard.diode_orientation = None

# Map encoder
encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.D4, board.D5, 2),
)

# Define what all the keys do + the encoder

keyboard.extensions.append(MediaKeys())
keyboard.keymap = [
    [KC.MPRV, KC.MPLY, KC.MNXT, KC.MUTE],
]
encoder.map = [
    ((KC.VOLD, KC.VOLU),)
]
if __name__ == "__main__":
    keyboard.go()