import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.tapdance import TapDance

from kmk.modules.holdtap import HoldTap

keyboard = KMKKeyboard()

holdtap = HoldTap()

tapdance = TapDance()

holdtap.tap_time = 200

keyboard.col_pins = (board.GP2,board.GP3,board.GP4,board.GP16,board.GP17,board.GP15,board.GP14,board.GP13,board.GP12,board.GP11)

keyboard.row_pins = (board.GP21,board.GP20,board.GP19,board.GP18)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(MouseKeys())

keyboard.modules.append(Layers())

keyboard.modules.append(holdtap)

keyboard.modules.append(tapdance)

keyboard.extensions.append(MediaKeys())

A_LCTL = KC.HT(KC.A, KC.LCTRL, prefer_hold=False, tap_interrupted=False)
R_LSFT = KC.HT(KC.R, KC.LSFT, prefer_hold=False, tap_interrupted=False)
S_LGUI = KC.HT(KC.S, KC.LGUI, prefer_hold=False, tap_interrupted=False)
T_LALT = KC.HT(KC.T, KC.LALT, prefer_hold=False, tap_interrupted=False)

N_RALT = KC.HT(KC.N, KC.RALT, prefer_hold=False, tap_interrupted=False)
E_RGUI = KC.HT(KC.E, KC.RGUI, prefer_hold=False, tap_interrupted=False)
I_RSFT = KC.HT(KC.I, KC.RSFT, prefer_hold=False, tap_interrupted=False)
O_RCTL = KC.HT(KC.O, KC.RCTRL, prefer_hold=False, tap_interrupted=False)

HOME_LCTL = KC.HT(KC.HOME, KC.LCTRL, prefer_hold=False, tap_interrupted=False)
PGDN_LSFT = KC.HT(KC.PAGEDOWN, KC.LSFT, prefer_hold=False, tap_interrupted=False)
PGUP_LGUI = KC.HT(KC.PAGEUP, KC.LGUI, prefer_hold=False, tap_interrupted=False)
END_LALT = KC.HT(KC.END, KC.LALT, prefer_hold=False, tap_interrupted=False)

L1_TAB = KC.HT(KC.TAB, KC.MO(1))
L2_SPC = KC.HT(KC.SPC, KC.MO(2))
L3_BSP = KC.HT(KC.BSPC, KC.MO(3))
L4_DEL = KC.HT(KC.DEL, KC.MO(4))

M_ENT = KC.TD(KC.M, KC.ENT, tap_time=170)
G_ENT = KC.TD(KC.G, KC.ESC, tap_time=170)

CNTRL_Z = KC.LCTL(KC.Z)
CNTRL_Y = KC.LCTL(KC.Y)
CNTRL_C = KC.LCTL(KC.C)
CNTRL_V = KC.LCTL(KC.V)

X = KC.NO

'''
layer0 = [
    X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,
    X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,
    X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,
    X,X,X,L3_BSP,L1_TAB,L2_SPC,L4_DEL,X,X,X,
    ]
'''

layer0 = [
    KC.Q     ,  KC.W      ,  KC.F     ,  KC.P     ,  X        ,  X        ,  KC.L     ,  KC.U     ,  KC.Y    ,  KC.J     ,
    A_LCTL   ,  R_LSFT    ,  S_LGUI   ,  T_LALT   ,  G_ENT    ,  M_ENT    ,  N_RALT   ,  E_RGUI   ,  I_RSFT  ,  O_RCTL   ,
    KC.X     ,  KC.C      ,  KC.D     ,  KC.V     ,  X        ,  X        ,  KC.H     ,  KC.B     ,  KC.K    ,  KC.Z     ,
    X        ,  X         ,  X        ,  L3_BSP   ,  L1_TAB   ,  L2_SPC   ,  L4_DEL   ,  X        ,  X       ,  X        ,
    ]

layer1 = [
    KC.DQT   ,  KC.QUOT   ,  KC.LPRN  ,  KC.LABK  ,  X        ,  X        ,  KC.RABK  ,  KC.RPRN  ,  KC.SCLN  ,  KC.COLN  ,
    KC.N1    ,  KC.N2     ,  KC.N3    ,  KC.N4    ,  KC.N5    ,  KC.N6    ,  KC.N7    ,  KC.N8    ,  KC.N9    ,  KC.N0    ,
    KC.TILD  ,  KC.GRV    ,  KC.LCBR  ,  KC.LBRC  ,  X        ,  X        ,  KC.RBRC  ,  KC.RCBR  ,  KC.COMM  ,  KC.DOT   ,
    X        ,  X         ,  X        ,  L3_BSP   ,  L1_TAB   ,  L2_SPC   ,  L4_DEL   ,  X        ,  X        ,  X        ,
    ]

layer2 = [
    KC.EXLM  ,  KC.AT     ,  KC.HASH  ,  KC.DLR   ,  X         ,  X        , KC.PERC    ,  KC.CIRC ,  KC.AMPR ,  KC.ASTR  ,
    HOME_LCTL,  PGDN_LSFT ,  PGUP_LGUI,  END_LALT ,  KC.ESC    ,  KC.ENT   ,  KC.LEFT   ,  KC.DOWN ,  KC.UP   ,  KC.RIGHT ,
    KC.QUES  ,  KC.PIPE   ,  KC.BSLS  ,  KC.SLSH  ,  X         ,  X        ,  KC.UNDS   ,  KC.MINS ,  KC.PLUS ,  KC.EQL   ,
    X        ,  X         ,  X        ,  L3_BSP   ,  L1_TAB    ,  L2_SPC   ,  L4_DEL    ,  X       ,  X       ,  X        ,
    ]

layer3 = [
    KC.F1    ,  KC.F2     ,  KC.F3    ,  KC.F4    ,  X         ,  X        ,  KC.MW_UP  ,  X       ,  X       ,  X        ,
    KC.MS_LT ,  KC.MS_DN  ,  KC.MS_UP ,  KC.MS_RT ,  X         ,  KC.PSCR  ,  KC.MB_LMB ,  KC.MB_RMB, X       ,  X        ,
    CNTRL_Z  ,  CNTRL_C   ,  CNTRL_V  ,  CNTRL_Y  ,  X         ,  X        ,  KC.MW_DN  ,  X       ,  X       ,  X        ,
    X        ,  X         ,  X        ,  L3_BSP   ,  L1_TAB    ,  L2_SPC   ,  L4_DEL    ,  X       ,  X       ,  X        ,
    ]

layer4 = [
    X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,
    X        ,  KC.BRID  ,  KC.BRIU  ,  X        ,  X        ,  KC.MUTE  ,  KC.MPLY  ,  KC.VOLD  ,  KC.VOLU  ,  X        ,  
    X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,  X        ,
    X,X,X,L3_BSP,L1_TAB,L2_SPC,L4_DEL,X,X,X,
    ]    

keyboard.keymap = [
    layer0, layer1, layer2, layer3, layer4
    ]
if __name__ == '__main__':
    keyboard.go()