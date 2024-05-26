import pandas as pd

#read all csv
# df = pd.read_csv('../sample1.csv')
# print(df)


#Read limited rows
# df = pd.read_csv('../sample1.csv',nrows=30)
# print(df)

# #particular columns
# df = pd.read_csv('../sample1.csv',nrows=30,usecols=['STATUS','UNITS'])
# print(df)

# #particular columns
# df = pd.read_csv('../sample1.csv',nrows=30,usecols=[0,1,2,4,5,6])
# print(df)

# #particular columns with skipping rows
# df = pd.read_csv('../sample1.csv',nrows=30,usecols=[0,1,2,4,5,6],skiprows=[2,5,6])
# print(df)


# #particular column as index column
# df = pd.read_csv('../sample1.csv',nrows=30,usecols=[0,1,2,4,5,6],index_col=5)
# print(df)

# #change header names
# df = pd.read_csv('../sample1.csv',nrows=30,usecols=[0,1,2,4,5,6],skiprows=[0],names=['A','B','C','D','E','F'])
# print(df)

#change header names
df = pd.read_csv('../sample2.csv',nrows=30)
print(df)
print('++++++++++++')
df1 = df.dropna(thresh=1)
print(df1)

#
print(df.index)
# print(df.columns)
print(df.describe())
#
# #index list
# print(df.index.array)
#
# #slice
# print(df[4:8])
#
# #top five
print(df.head())
# #last five
print(df.tail())