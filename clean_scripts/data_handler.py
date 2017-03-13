# IMPORTS
#---------------------------------------------------------------------------
import pandas as pd
import numpy as np
import os.path

# PREAMBLE
#---------------------------------------------------------------------------

# FUNCTIONS
# ---------------------------------------------------------------------------
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
        length = np.sqrt(np.dot(vec, vec))
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

# DataFrame OBJECT
#---------------------------------------------------------------------------
class DataFrame():
    def __init__(self, filename):

        self.filename = filename

        if filename[-7:] == 'tas.csv':
            self.df = pd.read_csv(filename, index_col='Unnamed: 0')

        elif filename[-3:] == 'csv':
            self.data = np.genfromtxt(filename,
                                      delimiter=',',
                                      skip_header=5,
                                      skip_footer=1,
                                      dtype=str)

            # INITIAL DATA PROCESSING FOR TSA ASSIGNMENT (MANUAL SETUP)
            # ---------------------------------------------------------------------------

            # DataFrame Setup
            # ================================================

            # Columns to be used for DataFrame
            self.columns = ['?', "u_x", "u_y", "u_z", "?", "sos", '?', "?", "?", "?", "Time-stamp"]

            # Creating DataFrame
            self.df = pd.DataFrame(self.data, columns=self.columns)

            # DataFrame Manipulation (first time running data)
            # ================================================

            # Delete all rows with '' for u_x
            self.df = self.df[self.df.u_x != '']

            # Delete Columns with '?'
            del self.df['?']

            # Setting Data Types (this slows processing)
            self.df['Time-stamp'] = self.df['Time-stamp'].apply(pd.to_datetime)
            self.df[['u_x', 'u_y', 'u_z', 'sos']] = self.df[['u_x', 'u_y', 'u_z', 'sos']].apply(pd.to_numeric)

            # Saving processed file
            filename = filename.replace('.csv','')
            self.df.to_csv(filename+'.tas.csv')

        # Assigning the components of ux,uy,uz to an array for V
        self.V = self.df[['u_x', 'u_y', 'u_z']].values
        self.df['V'] = arr_vec_length(self.V)

        # Setting Uxy (component of velocity in xy-plane)
        self.Uxy = self.df[['u_x', 'u_y']].values
        self.Uxy = np.insert(self.Uxy, [2], [0], axis=1)
        self.df['Uxy'] = arr_vec_length(self.Uxy)

        # Calculating array of thetas using function
        Theta = arr_vec_angle(self.Uxy, self.V)
        self.df['Theta'] = Theta

    # DataFrame Methods
    # ---------------------------------------------------------------------------
    def save_csv(self, filename):
        i = 0
        while True:
            if os.path.isfile(filename) == True:
                FileExistsError()

                while True:
                    ans = input("Would you like to change it yourself (Y/N)? ")

                    if ans == 'Y':
                        filename = input("New filename: ")

                        if os.path.isfile(filename) == False:
                            break
                        else:
                            ans = 'N';
                            return ans

                    elif ans == 'N':
                        while True:
                            i += 1
                            filename = str(filename) + "(" + str(i) + ")"
                            if os.path.isfile(filename) == False:
                                break
                            else:
                                continue
                        break
                    else:
                        print('Input not recognised')
            elif os.path.isfile(filename) == False:
                DataFrame.to_csv(filename)
                break







