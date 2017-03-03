from numpy import genfromtxt
from math import sqrt

# Lambda Function to calculate magnitude of vector from components.
mag = lambda x,y,z: sqrt(float(x)**2+float(y)**2+float(z)**2)

# Calculation of time interval between two time-stamps
def deltaT(t1, t2):
    t1 = t1; t2 = t2
    dh = float(t2[:-6]) - float(t1[:-6])
    dm = float(t2[2:-3]) - float(t1[2:-3])
    ds = float(t2[5:]) - float(t1[5:])
    Dt = dh*60*60 + dm*60 + ds #[s]
    return Dt

class data(object):

    def __init__(self, filename):
        self.filename = filename
        self.time = []

        # Loading data file
        self.data = genfromtxt(self.filename,
                   delimiter = ',',
                   skip_header = 5,
                   skip_footer = 1,
                   dtype = str)

        # Definition of initial starting time.
        self.initial_datetime = self.data[0,10]

        # Time stamp stripping of date
        for i in range(len(self.data[:, 10])):
            time = self.data[i, 10]
            time = time[11:]
            self.data[i, 10] = time

        # Appending of time to list, measured in seconds from start
        for i in range(len(self.data[:, 1])):
            self.time.append(deltaT(self.data[0, 10], self.data[i, 10]))

        # Conversion of velocity components into float, and ignoring of empty cells.
        for j in range(3):
            for i in range(len(self.data[:, 1 + j])):
                if self.data[i, 1 + j] == '':
                    self.data[i, 1 + j] = 0

                # Should the cell be empty, the value 0 will be assigned
                elif self.data[i, 1 + j] != '':
                    self.data[i, 1 + j] = float(eval(self.data[i, 1]))

    # Method to return column
    def col(self, number):
        col = self.data[number,:]
        return col

    # Method to return row
    def row(self, number):
        row = self.data[:, number]
        return row

# x = data('Gill Log [WM1]-4.csv')
#
# print(x.col(1))
#

def ConvertToINTstamp(time):
    return re.sub(":","",time)

def TransformTime (data):

    time = data[:,10]
    t0 = ConvertToINTstamp(time[0])

    t0h = int(t0[0])
    t0m= int(t0[1:3])
    t0s= int(t0[3:5])
    tstamp = t0h*60 *60 + t0m*60 +t0s
    for i in range(len(time)):
        localTime = ConvertToINTstamp(time[i])
        hour = int(localTime[0])
        minute = int(localTime[1:3])
        second = int(localTime[3:5])
        dt = (hour*60*60 + minute*60 + second)-tstamp
        data[i,10]=dt
    return data

print (TransformTime(data))
