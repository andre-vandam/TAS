# IMPORTS
#---------------------------------------------------------------------------
import pandas as pd
import numpy as np

# PREAMBLE
#---------------------------------------------------------------------------

# DATAFRAME OBJECT
#---------------------------------------------------------------------------
class DataFrame():
    def __init__(self, filename):
        self.filename = filename
        self.data = np.genfromtxt('3',
                             delimiter=',',
                             skip_header=5,
                             skip_footer=1,
                             dtype=str)

    # Functions for array of vectors        #i.e: [[x0,y0,z0],
    def arr_vec_dot(arr1, arr2):                 # [x1,y1,z1],
        arr_dots = []                            # [x2,y2,z2],
        for vec1, vec2 in zip(arr1, arr2):       # [x3,y3,z3],
            dot = np.dot(vec1, vec2)
            arr_dots.append(dot)
        return np.array(arr_dots)

    def arr_vec_length(arr):
        arr_lengths = []
        for vec in arr:
            length = np.sqrt(arr_vec_dot(vec, vec))
            arr_lengths.append(length)
        return np.array(arr_lengths)

    def arr_vec_angle(arr1, arr2):
        arr_angles = []

        for vec1, vec2 in zip(arr1, arr2):
            try:
                angle = np.arccos(np.dot(vec1, vec2) / (np.sqrt(np.dot(vec1, vec1)) * np.sqrt(np.dot(vec2, vec2))))
                arr_angles.append(np.rad2deg(angle))
            except RuntimeWarning:
                print(np.dot(vec1, vec2), np.sqrt(np.dot(vec1, vec1)), np.sqrt(np.dot(vec2, vec2)))

        return np.array(arr_angles)



