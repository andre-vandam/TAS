import numpy as np
from math import sqrt
from numpy import delete

#---------------------------------------------------------------------------------
# FUNCTIONS                                                                      |
#---------------------------------------------------------------------------------
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

#---------------------------------------------------------------------------------
# OBJECTS                                                                        |
#---------------------------------------------------------------------------------
class data(object):
    def __init__(self, filename):
        self.filename = filename
        self.time = []
        self.ux = []
        self.uy = []
        self.uz = []
        self.V = []

        # Loading data file
        self.data = np.genfromtxt(self.filename,
                   delimiter = ',',
                   skip_header = 5,
                   skip_footer = 1,
                   dtype = str)

        # TIME VARIABLE INIT
        #--------------------------------------------------------------------------

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

        # VELOCITY COMPONENT INIT
        #--------------------------------------------------------------------------
        # Conversion of velocity components into float, and ignoring of empty cells.
        for j in range(3):
            for i in range(len(self.data[:, 1 + j])):
                if self.data[i, 1 + j] != '':
                    self.data[i, 1 + j] = float(self.data[i, 1+j])

                # Should the cell be empty, the value 0 will be assigned
                elif self.data[i, 1 + j] == '':
                    delete(self.data, (i), axis = 0)
                    # self.data[i, 1 + j] = 0

        # Defining the components as attributes
        self.Ux = self.data[:,1].astype(float)
        self.Uy = self.data[:,2].astype(float)
        self.Uz = self.data[:,3].astype(float)


        self.ux2 = np.power(self.Ux , 2)
        self.uy2 = np.power(self.Uy , 2)
        self.Uxy= np.sqrt(self.ux2 + self.uy2)
        print (self.Uxy)



        # Defining the magnitude of velocity vector
        for i in range(len(self.Ux)):
            V = mag(self.Ux[i],self.Uy[i],self.Uz[i])
            self.V.append(V)

        # THETA ANGLE INIT
        #---------------------------------------------------------------------------








    # Will potentially remove this
    # # Method to return column
    # def col(self, number):
    #     col = self.data[number,:]
    #     return col
    #
    # # Method to return row
    # def row(self, number):
    #     row = self.data[:, number]
    #     return row

x = data('1')
#
# print(x.col(1))
#
