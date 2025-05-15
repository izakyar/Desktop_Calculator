import numpy as np
import string
from output import yay, nay, info, out

"""
This file initalizes the lists and matrices

We will use a 2d vector to store lists as lists are single columns with many elements
TODO:
Matrices will use a 3d vector, x: Matrix, y: x cord, z: y cord, basically
X will determine which matrix to use
Y will choose which Row
Z will choose which column
"""


lists = np.zeros((6, 10),dtype=float, order='C', like=None)

# out(lists)
# ^^^^^^^^^^ TEST LISTS


