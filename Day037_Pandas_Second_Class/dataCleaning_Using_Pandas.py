import pandas as pd

# 
# df = pd.read_csv("Data_Analysis_Training_Anudip_Foundation\Day037_Pandas_Second_Class\Housing.csv")
# print(df.to_string())
# print(df)


# df = pd.read_csv("Data_Analysis_Training_Anudip_Foundation\Day037_Pandas_Second_Class\data.csv")
# # new_df = df.dropna()


# df["Volume"].fillna(1230, inplace=True)
# print(df)

#  fill the values into the emplty cell of any particular column.. ************************************************************************************
# df = pd.read_csv("Data_Analysis_Training_Anudip_Foundation\\Day037_Pandas_Second_Class\\data.csv")
# # df["Volume"] = df["Volume"].fillna(100)  # Returns a new Series and assigns it back
# df["Volume"].fillna(100, inplace=True)  # Returns a new Series and assigns it back
# print(df)


# df = pd.read_csv("Data_Analysis_Training_Anudip_Foundation\\Day037_Pandas_Second_Class\\data.csv")
# # df.fillna(df["Volume"].mean(), inplace=True)
# print(df)