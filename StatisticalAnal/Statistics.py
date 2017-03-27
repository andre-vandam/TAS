import sys
sys.path.append ("../clean_scripts/")
import data_handler as dp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataFrames = []
staisticObjects =[]



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
        self.timeStamps = np.array(dataFrame.df.t)
        self.theta = np.array(dataFrame.df.Theta)
        self.name = str(name)
        ArrayTobeRolled = np.column_stack((self.theta, self.timeStamps))
        self.rolledTheta = (ArrayTobeRolled)



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
        plt.plot(np.array(self.timeStamps),np.array(self.rolledTheta))
        plt.xlabel("time [s]")
        plt.ylabel("Vertical Inflow Angle rolling turbulence [deg]")
        plt.savefig(self.name+ "_turb_rolled.png")
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
        currentTime = times[0]
        EndTime = times[-1]
        stop = False
        subarray = 0
        RolledArray = []
        while (not stop):
            WhereEnd = np.where(times == currentTime + deltaT)[0]
            subarray= values[WhereStart:WhereEnd]
            mean , stand = men_std(subarray)
            RolledArray.append([mean, stand,currentTime+deltaT])
            currentTime = currentTime +deltaT
            if (currentTime >= EndTime):
                stop = True

        return np.array(RolledArray)
for i in range (1,9,1):
    currentDF =dp.DataFrame("../DATA/"+str(i)+".tas.csv")
    dataFrames.append(currentDF)
    currentStatObj = StatisticalAnal(currentDF, str(i),6000)
    staisticObjects.append(currentStatObj)
    currentStatObj.plotTheta()
    currentStatObj.PrintMeans()
    currentStatObj.plotrolledTheta()
