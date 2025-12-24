from numba import njit
import numpy as np
import glm
import math

#window resolution
WIN_RES = glm.vec2(1600, 900)

#color
BG_COLOR = glm.vec3(0.5, 0.8, 1.0)