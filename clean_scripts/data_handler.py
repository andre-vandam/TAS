# IMPORTS
#---------------------------------------------------------------------------
import pandas as pd
import numpy as np
import os.path
import time, datetime
import functools, operator
import math
import matplotlib.pyplot as plt
# PREAMBLE
#---------------------------------------------------------------------------

# FUNCTIONS
# ---------------------------------------------------------------------------

def time_convert(t):

    x = time.strptime(t, '%H:%M:%S')
    return str(int(datetime.timedelta(hours = x.tm_hour, minutes = x.tm_min, seconds = x.tm_sec).total_seconds()))

strip_date = lambda time_stamp: time_stamp[11:]

SecsToMins = lambda s: s/60.0
MinsToSecs = lambda min: min*60.0

# def offset(t, t0):
#     return t-t0
#
# t_0_offset = lambda time: offset(time, 1)

# def t_0_offset(t):
#     global j
#     j = 0
#
#     if j==0:
#         global t0
#         t0 = t
#         j = 1
#     else:
#         t = t - t0
#
#     return t


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

            if  arr2[np.where(arr2 == vec2)][2] <=  0:
                arr_angles.append(-np.rad2deg(angle))

            elif arr2[np.where(arr2 == vec2)][2] > 0:
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

            self.data = self.data[np.where(np.isfinite(self.data))]

            # y = np.array(x.df.Theta)
            # print(y[np.where( np.isfinite(y))])

            # INITIAL DATA PROCESSING FOR TSA ASSIGNMENT (MANUAL SETUP)
            # ---------------------------------------------------------------------------


            # DataFrame Setup
            # ================================================

            print('DataFrame Setup Initialising..') # STATUS UPDATE

            # Columns to be used for DataFrame
            self.columns = ['?', "u_x", "u_y", "u_z", "?", "sos", '?', "?", "?", "?", "Time-stamp"]

            # Creating DataFrame
            self.df = pd.DataFrame(self.data, columns=self.columns)

            # DataFrame Manipulation (first time running data)
            # ================================================

            print('Filtering blank data lines...') # STATUS UPDATE

            # Delete all rows with '' for u_x
            self.df = self.df[self.df.u_x != '']

            # Delete Columns with '?'
            del self.df['?']

            # Manipulation of time-stamp column:
            # The following lines convert the time-stamp into seconds aggregate from t0

            print('Manipulating Time-stamps...') # STATUS UPDATE

            self.df['Time-stamp'] = self.df['Time-stamp'].apply(strip_date)
            self.df['t'] = self.df['Time-stamp']
            self.df['t'] = self.df['t'].apply(time_convert)
            self.df['t'] = self.df['t'].apply(pd.to_numeric)
            t0 = int(self.df['t'][0])
            subtract_t0 = lambda time: time - t0 # I apologise for making a lambda function here!
            self.df['t'] = self.df['t'].apply(subtract_t0)

            # Conversion of time-stamp to datetime data type (long processing)
            self.df['Time-stamp'] = self.df['Time-stamp'].apply(pd.to_datetime)

            # Conversion of velocity components into numeric data type
            self.df[['u_x', 'u_y', 'u_z', 'sos']] = self.df[['u_x', 'u_y', 'u_z', 'sos']].apply(pd.to_numeric)

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

            # Adding the turbulence intensity (%)

                # NOTE: For the data points located in the first and last 10 minutes,
                #       their values will be calculated using the range within 5 minutes up and below.
            # turb = []
            # for i in range(len(self.df.V)):
            #     try:
            #         interval = self.df[self.df.t.between(MinsToSecs( SecsToMins(self.df.t[i]) - 5 ), MinsToSecs( SecsToMins(self.df.t[i] + 5) ), inclusive=True)]
            #         mean = np.mean(interval.V)
            #         std = np.std(interval.V)
            #         turb_intensity = (std/mean) * 100
            #         turb.append(turb_intensity)
            #
            #     except KeyError: turb.append(turb[-1]); pass
            #
            # self.df['Turb_intensity'] = turb

            # Saving processed file
            filename = filename.replace('.csv','')
            self.df.to_csv(filename+'.tas.csv')




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

# USE FOR PRESENTATION

# Raw Data to be processed
# x = DataFrame('../Geoffrey-scripts/3.csv')

# Data already processed
# x = DataFrame('../Geoffrey-scripts/3.tas.csv')
#
# print(x.df[2750:2780])

# np.where(np.is)
#
# print(x.df)
# #
# #
# interval = x.df[np.where(np.isnan(x.df))]
# print(interval)