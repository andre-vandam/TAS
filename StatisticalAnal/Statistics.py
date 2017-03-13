import sys
sys.path.append ("../clean_scripts/")
import data_handler as dp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataFrames = []

# for i in range (5,11,1):
#     dataFrames.append(dp.DataFrame("../Data/"+str(i)+".csv"))

test1 = dp.DataFrame("../Data/5.tas.csv")


plt.plot(range(np.size(test1.df.Uxy)), test1.df.Uxy )
plt.plot(range(np.size(test1.df.Uxy)), pd.rolling_mean(test1.df.Uxy,3000), c='r' )
# plt.plot(range(np.size(test1.df.Theta)), test1.df.Theta )

plt.show()
