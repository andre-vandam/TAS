from numpy import genfromtxt
from math import sqrt
import sys
sys.path.append('C:\\Users\ggarr\Documents\TAS\Geoffrey-scripts')

# Lambda Function to calculate magnitude of vector from components.
mag = lambda x, y, z: sqrt(float(x) ** 2 + float(y) ** 2 + float(z) ** 2)


# Calculation of time interval between two time-stamps
def deltaT(t1, t2):
    t1 = t1
    t2 = t2
    dh = float(t2[:-6]) - float(t1[:-6])
    dm = float(t2[2:-3]) - float(t1[2:-3])
    ds = float(t2[5:]) - float(t1[5:])
    Dt = dh * 60 * 60 + dm * 60 + ds  # [s]
    return Dt


class data(object):
    def __init__(self, filename):
        self.filename = filename
        self.time = []
        self.vlist = []

        # Loading data file
        self.data = genfromtxt(self.filename,
                               delimiter=',',
                               skip_header=5,
                               skip_footer=1,
                               dtype=str)

        # Definition of initial starting time.
        self.initial_datetime = self.data[0, 10]

        # Time stamp stripping of date
        for i in range(len(self.data[:, 10])):
            time = self.data[i, 10]
            time = time[11:]
            self.data[i, 10] = time

        # Calculation of magnitude of wind vector
        for i in range(len(data[:, 1])):
            u, v, w = (self.data[i, 1],
                       self.data[i, 2],
                       self.data[i, 3])

            V = mag(u, v, w)
            self.vlist.append(V)

        # Appending of time to list, measured in seconds from start
        for i in range(len(self.data[:, 1])):
            self.time.append(deltaT(self.data[0, 10], self.data[i, 10]))

        # Conversion of velocity components into float, and ignoring of empty cells.
        for j in range(3):

            # Should the cell be empty, the value 0 will be assigned
            for i in range(len(self.data[:, 1 + j])):
                if self.data[i, 1 + j] == '':
                    self.data[i, 1 + j] = 0

                elif self.data[i, 1 + j] != '':
                    self.data[i, 1 + j] = float(self.data[i, 1 + j])

    # Method to return column
    def col(self, number):
        col = self.data[:, number]
        return col

    # Method to return row
    def row(self, number):
        row = self.data[number, :]
        return row

