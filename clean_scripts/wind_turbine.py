from math import cos

# The following intertia data is derived from CATIA.
IoxG = 10**(10)  # [kg m^2]
IoyG = 0.422  # [kg m^2]
IozG = 0.367  # [kg m^2] Propeller only considered for z rotation

vane_surface = 0.04 # [m^2]

rho = 1.225

import numpy as np

# Functions
def vec_angle(vec1, vec2):

        angle = np.arccos(np.dot(vec1, vec2) / (np.sqrt(np.dot(vec1, vec1)) * np.sqrt(np.dot(vec2, vec2))))

            # if  arr2[np.where(arr2 == vec2)][2] <=  0:
            #     angle = -np.rad2deg(angle)
            #
            # elif arr2[np.where(arr2 == vec2)][2] > 0:
            #     angle = np.rad2deg(angle)

        return angle

class WindTurbine_simulation():

    ############# REFERENCE FRAME #############
    # |               |y                      #
    # |               |   ___                 #
    # |  z____________| _____|  <---- Front   #
    # |               /   ___|                #
    # |              /                        #
    # |             /x                        #
    ###########################################

    def __init__(self, V_array, Uxy_array, timestamp_array, IoxG, IoyG, IozG):

        self.i = 0

        # The following intertia data is derived from CATIA.
        self.IoxG = IoxG
        self.IoyG = IoyG
        self.IozG = IozG
        self.IG = np.array([self.IoxG, self.IoyG, self.IozG])

        # Calling data arrays for velocity components and time-stamps.
        self.V_array = V_array
        self.timestamp_array = timestamp_array
        self.Uxy_list = Uxy_array

        # Defining initial orientation of wind turbine as initial Uxy.
        self.orientation = Uxy_array[0]
        self.orientation_list = np.linalg.norm([self.orientation])

    # def resistive_moment(self):

    def aerodynamic_moment(self, ):

        Cm_x = 0

        Cm_y = 0

        Cm_z = 0

        return Cm_x, Cm_y, Cm_z

    def vane_moment(self, vane_surface = 0.04, moment_arm = 1.0): # SET VANE SURFACE PARAMETERS FOR CORRECTION
        incident_angle = vec_angle(self.orientation, self.Uxy_list[self.i])

        self.vane_surface = vane_surface
        self.incident_surface = self.vane_surface * cos(incident_angle)
        vane_moment = moment_arm * (0.5 * rho * (self.V_array[self.i]) **2 * self.incident_surface)

        return vane_moment

    def update(self, vane_surface = 0):

        vane_moment = self.vane_moment(vane_surface)
        aerodynamic_moment = self.aerodynamic_moment()

        # sum_moment =
        #
        # alpha =

        sum_moment = sum(vane_moment, aerodynamic_moment)

        alpha = np.divide(sum_moment, self.IG)

        omega = alpha * dt

        theta = omega * dt



    # sum IoxG*M = 50N