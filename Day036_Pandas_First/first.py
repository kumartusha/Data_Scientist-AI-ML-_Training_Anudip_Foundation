#  Pandas implementation......

import pandas as pd

# list1 = [3,4,6,1,2,5,3,9,7,89]
# list2 = pd.Series(list1)
# print(list2)

# **********************  Change Index By User in pandas (labeling) *****************

# list1 = [3,4,6,1,2,5]
# list2 = pd.Series(list1, index=["adbb",'b','c','d','e','f'])
# print(list2)

# **********************  Change Index By User in pandas (labeling) *****************
# list1 = {'day1' : 2000, 'day2' : 3000, 'day3' : 4000, 'day4' : 5000}
# list2 = pd.Series(list1, index=["day1","day2","day3","day4"])
# print(list2)



##############################  DataFrames in Pandas #######################################
#  Creation of the DataFrame..
# data = {"cal": [400,500,600,700],
#            "dur": [570, 587, 985, 894]}

# datset = pd.DataFrame(data)
# print(datset)

# Locate Row **********************
data = {"cal": [400,500,600,700],
           "dur": [570, 587, 985, 894]}

datset = pd.DataFrame(data)
print(datset.loc[0])
print(datset.loc[0:3])
print(datset.loc[0:1, 0,1])


# Home work..
# name age salary and create the DataFrame and print
# That and perform access like iloc and print the Data.

