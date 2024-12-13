import pandas as pd

# dataset = {"Name": ["Tushar", "Kumar", "Rakshit", "Shivam", "Ankit"], 
#             "Age": [20,21,30,32,12],
#             "Course": ["Btech", "BBa", "BCA", "MTech", "ITI"]}


# data = pd.DataFrame(dataset)
# print(data)

# print("===========================================================================")
# Accessing the columns Data from the Dataset..
# print(data['Name'])

# print("========= Accessing Rows into the Dataset ==================")
# print(data.iloc[0][0])       # Tushar
# print(data.iloc[0][0])       

# print("========= Label Based Indexing ==================")
# print(data.loc[1, 'Name'])       # Tushar
# print(data.loc[1, 'Age'])


# Integer Based Indexing..
# print(data.iloc[0,1])'

#  Getting the two rows from the Dataset..
# print(data.loc[[0,1,2]])
# print(data.iloc[0:2, :])


#  Read the data from the CSV File.. **********************************************************************************************
# df = pd.read_csv(r"data.csv", encoding="utf-8")
# df = pd.read_csv(r"C:\\Users\\USER\\OneDrive\\Desktop\\Github\\Github-anudip-work\\Data_Analysis_Training_Anudip_Foundation\\Day037_Pandas_Second_Class\\data.csv")
# df = pd.read_csv("Data_Analysis_Training_Anudip_Foundation\Day037_Pandas_Second_Class\data.csv")
# df = pd.read_csv(r"C:\\Users\\USER\\OneDrive\\Desktop\\Github\\Github-anudip-work\\Data_Analysis_Training_Anudip_Foundation\\Day037_Pandas_Second_Class\\data.csv")
# print(df)
# print(df.to_string())



#  Json Data with in the Python Dictionary.. **********************************************************************************************

# data = {"Duration": {
#              "0": 60,
#              "1": 60,
#              "2": 50,
# }, 
#         "Pulse": {
#                "0": 110,
#              "1": 117,
#              "2": 103,
#         }, "MaxPulse": {
#              "0": 130,
#              "1": 145,
#              "2": 135,
#         }}

# df = pd.DataFrame(data)
# print(df)
# print(df.to_string())


# ********************************************************8 Head and Tail of the Data.. **********************************************************************
# df = pd.read_csv("Data_Analysis_Training_Anudip_Foundation\Day037_Pandas_Second_Class\data.csv")
# print(df)
# print(df.head())
# print(df.tail())


# *********************************************************  Info Function . ******************************************************************
# df = pd.read_csv("Data_Analysis_Training_Anudip_Foundation\Day037_Pandas_Second_Class\data.csv")
# print(df)
# print(df.info())


# *************************************************************  DATA CLEANING ********************************************************************************
