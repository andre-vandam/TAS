import sys
sys.path.append ("../clean_scripts/")
import data_handler as dp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataFrames = []
staisticObjects =[]
'''
Wm1 -> 1
wm4 -> 2
Wm5 -> 3
Wm6 -> 4
Wm7 -> 5
Wm8 -> 6
Wm9 -> 7
Wm10 -> 8




'''


# for data in dataFrames


# plt.plot(range(np.size(test1.df.Uxy)), test1.df.Uxy )
# plt.plot(range(np.size(test1.df.Uxy)), pd.rolling_mean(test1.df.Uxy,3000), c='r' )
# plt.plot(range(np.size(test1.df.Theta)), test1.df.Theta )
#
# plt.show()

class StatisticalAnal():
    def __init__(self,dataFrame,name, rollingDT):
        self.Uxy = dataFrame.df.Uxy
        self.Uz = dataFrame.df.u_z
        self.V = np.array(dataFrame.df.V)
        self.timeStamps = np.array(dataFrame.df.t)
        self.theta = np.array(dataFrame.df.Theta)
        self.name = str(name)
        ArrayTobeRolled = np.column_stack((self.theta, self.timeStamps))
        self.rolledTheta = self.rolling(ArrayTobeRolled,rollingDT)
        ArrayTobeRolled = np.column_stack((self.V, self.timeStamps))
        self.rolledV = self.rolling(ArrayTobeRolled,rollingDT)



    def PrintMeans (self):
        name = self.name
        file = open("file" + name+ ".txt","w")
        mean , std = self.men_std(self.Uxy)
        file.write("Mean Uxy : "+ str(mean) + " STD :" + str(std))
        mean , std = self.men_std(self.Uz)
        file.write("\n Mean Uz : "+ str(mean) + " STD :" + str(std))
        mean , std = self.men_std(self.theta)
        file.write("\n Mean Theta : "+ str(mean) + " STD :" + str(std))
        file.close()


    def plotTheta(self):
        plt.plot(np.array(self.timeStamps),np.array(self.theta))
        plt.xlabel("time [s]")
        plt.ylabel("Vertical Inflow Angle [deg]")
        plt.savefig(self.name+ ".png")
        plt.gcf().clear()

    def plotrolledTheta(self):
        plt.plot(np.array(self.rolledTheta)[:,2],np.array(self.rolledTheta)[:,0])
        plt.xlabel("time [s]")
        plt.ylabel("Vertical Inflow Angle rolling turbulence [deg]")
        plt.savefig(self.name+ "_rolled_tita_mean.png")
        plt.gcf().clear()

    def plotTurbulaceRolled(self):
        plt.plot(np.array(self.rolledTheta)[:,2],(np.array(self.rolledV)[:,1]/np.array(self.rolledV)[:,0]))
        plt.xlabel("time [s]")
        plt.ylabel("Vertical Inflow Angle rolling turbulence [deg]")
        plt.savefig(self.name+ "_rolled_turbulence.png")
        plt.gcf().clear()



    def men_std(self, vector):
        return np.mean(vector) , np.std(vector)


    def rolling(self, vector, deltaT):
        # assumig the vector is a 2 dimenional matrix, with the first column being the values
        # and the second column being the Time-stamp
        values = vector [:,0]
        times = vector[:,1]
        WhereStart = 0
        WhereEnd = 0
        EndTime = times[-1]
        stop = False
        subarray = []
        RolledArray = []
        WhereEnd = np.where(times ==  deltaT)[0][0]
        centerTimeIndex = np.where(times ==deltaT/2.) [0][0]
        while (not stop):
            subarray= values[WhereStart:WhereEnd]
            mean , stand = self.men_std(subarray)
            RolledArray.append([mean, stand,times[centerTimeIndex]])
            centerTimeIndex = centerTimeIndex +1
            WhereEnd = WhereEnd +1
            WhereStart = WhereStart +1
            if (WhereEnd >= EndTime):
                stop = True
        return np.array(RolledArray)
for i in range (1,9,1):
    currentDF =dp.DataFrame("../DATA/"+str(i)+".tas.csv")
    dataFrames.append(currentDF)
    currentStatObj = StatisticalAnal(currentDF, str(i),600)
    staisticObjects.append(currentStatObj)
    currentStatObj.plotTheta()
    currentStatObj.PrintMeans()
    currentStatObj.plotrolledTheta()
    currentStatObj.plotTurbulaceRolled



class InterpolateAnal():
    def __init__(self,InternaldataframeNumber1, InternaldataframeNumber2, height1,height2,desiredheight ):
        DataFrame1 = dp.DataFrame("../DATA/"+str(InternaldataframeNumber1)+".tas.csv")
        DataFrame2 = dp.DataFrame("../DATA/"+str(InternaldataframeNumber2)+".tas.csv")
        self.Theta1 = np.array(DataFrame1.df.Theta)
        self.Theta2 = np.array(DataFrame2.df.Theta)
        self.Time1 = np.array(DataFrame1.df.t)
        self.Time2 = np.array(DataFrame2.df.t)
        self.TimeList = [self.Time1,self.Time2]
        self.Interpolated , self.SelctedArray = self.interpolate(self.Theta1,self.Theta2,height1,height2,desiredheight)
        self.name = str(InternaldataframeNumber1) + "_" + str(InternaldataframeNumber2) + "_Interpolated"

    def plotTheta(self):
        plt.plot(self.TimeList[self.SelctedArray], self.Interpolated)
        plt.xlabel("time [s]")
        plt.ylabel("Vertical Inflow Angle [deg]")
        plt.savefig(self.name+ ".png")
        plt.gcf().clear()


    def interpolate (self,vector1, vector2 , height1, height2, desiredheight):
        ShorterArray = None
        interpolated = []
        heigts= np.array([height1, height2])

        if ( vector1.size >= vector2.size ):
            ShorterArray=1
            vector1=vector1[:vector2.size]
        else:
            ShorterArray=0
            vector2=vector2[:vector1.size]
        for i in range (vector1.size):
            tempValues = np.array([vector1[i],vector2[i]])
            interpolatedValue = np.interp(desiredheight,heigts,tempValues)
            interpolated.append(interpolatedValue)
        return interpolated , ShorterArray


Interpolation4_5 = InterpolateAnal(2,3,7.8,10.10,8.5)
Interpolation4_5.plotTheta()
Interpolation9_7 = InterpolateAnal(5,7,7.6,10,8.5) #Note annenmometers 9 7 are switched mistake in the data, so this is a correction
Interpolation9_7.plotTheta()
Interpolation1_6 = InterpolateAnal(1,6,6.3,10,8.5)
Interpolation1_6.plotTheta()
