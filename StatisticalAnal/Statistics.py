import sys
sys.path.append ("../clean_scripts/")
import data_handler as dp

dataFrames = []

for i in range (5,11,1):
    dataFrames.append(dp.DataFrame("../Data/"+str(i)+".csv"))
