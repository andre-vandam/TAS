import numpy as np
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

# Projection of a vector on a plane. By default it will project to XY plane.
def VEC_PROJECTION_PLANE(v1, b1 = np.array([1,0,0]), b2 = np.array([0,1,0])):
    projections = []
    for i in range(len(v1[0,:])):
        a1 = v1[:,i] * b1
        a2 = v1[:,i] * b2
        projections.append([a1[0], a2[1], 0])

    return np.array(projections).T

# Calculation of angle between two vectors
def VEC_ANGLE(v1,v2):
    angles = []
    for i in range(len(v1[0, :])):
        angle = np.arccos(np.dot(v1[:,i], v2[:,i]) / (np.sqrt(np.dot(v1[:,i], v1[:,i])) * np.sqrt(np.dot(v2[:,i], v2[:,i]))))
        angles.append(angle)
    return np.array(angles)

# Vector dot product for array of vectors
def VEC_DOT(v1,v2):
    vec_dot = []
    if len(v1[0,:]) == len(v2[0,:]):
        for i in range(len(v1[0,:])):
            print(i)
            dot = np.dot(v1[:,i],v2[:,i])
            vec_dot.append(dot)
        return vec_dot

    else: raise ValueError("Dimensions of the arrays are not the same: "+"(dim"+str(len(v1[0,:]))+'!= '+"(dim"+str(len(v2[0,:])))
#
# # Sqrt
# def VEC_SQRT(v1):
#     vec_sqrt = []
#     for i in range(len(v1[0,:])):
#         sqrt = np.sqrt(v1[0,i])
#         vec_sqrt.append(sqrt)
#     return vec_sqrt

class data(object):

    def __init__(self, filename):
        self.filename = filename
        self.time = []

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
                    self.data[i, 1 + j] = 0

        # Defining the components as attributes
        zero = np.zeros(len(self.data[:,0]))

        self.u_x = self.data[:, 1].astype(float)
        self.u_y = self.data[:, 2].astype(float)
        self.u_z = self.data[:, 3].astype(float)

        self.V = self.u_x
        self.V = np.vstack([self.V, self.u_y])
        self.V = np.vstack([self.V, self.u_z])

        self.u_xy = self.V; self.V[2,:] = 0
        self.Uxy = np.sqrt(VEC_DOT(self.u_xy, self.u_xy))


        # THETA VARIABLE CALCULATION (between z component and xy plane)
        #---------------------------------------------------------------------------
        # V projected on xy-plane for Uxy_hat
        self.Uxy_hat = VEC_PROJECTION_PLANE(self.V)

        # Angles between V[i] and Uxy
        self.theta = VEC_ANGLE(self.Uxy_hat, self.V)
        print(self.theta)

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

x = data('3')
#
# print(x.col(1))

