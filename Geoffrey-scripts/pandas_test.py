import pandas as pd
import numpy as np
import scipy as sp
import os.path
import matplotlib.pyplot as plt

data = np.genfromtxt('3',
                          delimiter=',',
                          skip_header=5,
                          skip_footer=1,
                          dtype=str)

# DATAFRAME CSV FUNCTIONS
def save_csv(filename, DataFrame):
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
                        ans = 'N'; return ans

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

# FUNCTIONS FOR ARRAY OF VECTORS       #i.e: [[x0,y0,z0],
def arr_vec_dot(arr1, arr2):                # [x1,y1,z1],
    arr_dots = []                           # [x2,y2,z2],
    for vec1,vec2 in zip(arr1,arr2):        # [x3,y3,z3],
        dot = np.dot(vec1,vec2)
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

    for vec1,vec2 in zip(arr1,arr2):
        try:
            angle = np.arccos(np.dot(vec1, vec2) / (np.sqrt(np.dot(vec1, vec1)) * np.sqrt(np.dot(vec2, vec2))))
            arr_angles.append(np.rad2deg(angle))
        except RuntimeWarning:
            print(np.dot(vec1, vec2),np.sqrt(np.dot(vec1, vec1)),np.sqrt(np.dot(vec2, vec2)))

    return np.array(arr_angles)

# Columns to be used for DataFrame
columns = ['?',"u_x","u_y","u_z","?","sos",'?',"?","?","?","Time-stamp"]

# Creating DataFrame
df = pd.DataFrame(data, columns =columns )

# Delete all rows with '' for u_x
df = df[df.u_x != '']

# Delete Columns with '?'
del df['?']

# Setting Data Types (this slows processing)
df['Time-stamp'] = df['Time-stamp'].apply(pd.to_datetime)
df[['u_x','u_y','u_z','sos']] = df[['u_x','u_y','u_z','sos']].apply(pd.to_numeric)

# Assigning the components of ux,uy,uz to an array for V
V = df[['u_x','u_y','u_z']].values

# Setting Uxy (component of velocity in xy-plane)
Uxy = df[['u_x','u_y']].values
Uxy = np.insert(Uxy, [2], [0], axis = 1)

# Calculating array of thetas using function
Theta = arr_vec_angle(Uxy,V)
df['Theta'] = Theta

plt.plot(df["Time-stamp"],df['Theta'])
plt.show()

# save_csv('test',df)