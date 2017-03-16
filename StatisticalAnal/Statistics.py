import sys
sys.path.append ("../clean_scripts/")
import data_handler as dp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataFrames = []

# for i in range (5,11,1):
#     dataFrames.append(dp.DataFrame("../Data/"+str(i)+".csv"))

test1 = dp.DataFrame("../Data/5.csv")


# plt.plot(range(np.size(test1.df.Uxy)), test1.df.Uxy )
# plt.plot(range(np.size(test1.df.Uxy)), pd.rolling_mean(test1.df.Uxy,3000), c='r' )
plt.plot(range(np.size(test1.df.Theta)), test1.df.Theta )

plt.show()

class StatisticalAnal():
    def __init__(self,dataFrame):
        Uxy = dataFrame.df.Uxy
        timeStamps = dataFrame.df["Time-stamp"]
        print(Uxy)
        print(timeStamps)


    def men_std(vector):
        return np.mean(vector) , np.std(vector)

    def rolling(vector, deltaT):
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


statisticsTest = StatisticalAnal(test1)
