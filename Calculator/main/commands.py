from output import yay, nay, info, out
from initalize import lists as ls 
import numpy as np
import string

mode = "DEG"


"""
Ts file contains all the commands, no this will not be a REPL
But it will make functional buttons easier to  reproduce

TODO:
JSON File for settings (float decimals, )
UI for Linux Systems.
functional Regex -> Converts Fractions inputted into functions as float for ease of use (Maybe potentially un needed)
stat tests
calculus (summunation, integral)
advanced equation solving (aka a mini CAS)
variable solver
equation testing (if x = ?, does x + 2 = 2x - 2, greater than, less than, etc.)
web app for desmos.
storing previous answer
REPL Mode.

Infographicals (teach user how to do X Y Z. cmd = howto ex: howto u-subsitution)

"""

def echo(msg: str) -> None:
    out(msg=msg)
    return None

def quit() -> None:
    yay("Exiting...")
    exit()
    return None # Most Likely unused.

def editlist(listnum: int, elementnum: int, element: float) -> None:
    ls[listnum][elementnum] = element
    return None

def zero_out_list() -> None:
    for i in range(len(ls)):
        ls[i][i] = 0
    return None

# Mathmatical Operators Arithmetic

def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mult(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float:
    return a / b

# Trig

def sin(a: float) -> float:
    if mode == "DEG":
        return np.sin(np.deg2rad(a))
    elif mode == "RAD":
        return np.sin(a)
    else:
        return None

def cos(a: float) -> float:
    if mode == "DEG":
        return np.cos(np.deg2rad(a))
    elif mode == "RAD":
        return np.cos(a)
    else:
        return None

def tan(a: float) -> float:
    if mode == "DEG":
        return np.tan(np.deg2rad(a))
    elif mode == "RAD":
        return np.tan(a)
    else:
        return None

# Inverse trig

def arcsin(a: float) -> float:
    if mode == "DEG":
        return np.rad2deg(np.arcsin(a))
    elif mode == "RAD":
        return np.arcsin(a)
    else:
        return None

def arccos(a: float) -> float:
    if mode == "DEG":
        return np.rad2deg(np.arccos(a))
    elif mode == "RAD":
        return np.arccos(a)
    else:
        return None

def arctan(a: float) -> float:
    if mode == "DEG":
        return np.rad2deg(np.arctan(a))
    elif mode == "RAD":
        return np.arctan(a)
    else:
        return None

# log ln

def log(a: float) -> float:
    return np.log10(a)

def ln(a: float) -> float:
    return np.log(a)






