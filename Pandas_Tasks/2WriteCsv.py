import pandas as pd

dic = {'a':[1,2,3,4,5],'b':[6,7,8,9,10]}

df = pd.DataFrame(dic)

#add new row
df.loc[9] = [22,33]

#csv with index
df.to_csv("abc.csv")

#csv without index
df.to_csv("abcd.csv",index=False)

#csv with custom header name
df.to_csv("abcd.csv",index=False,header=[1,2])