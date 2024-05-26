from sklearn.preprocessing import RobustScaler
import pandas as pd
import numpy as np

df =  pd.read_csv("titanic.csv",usecols=['Age','Fare'])
df['Age'].fillna(df.Age.mean(),inplace=True)

data = np.array(df)
data = np.array([[1, 100],
                [2, 200],
                [3, 300],
                [4, 400],
                [5, 500],
                [65, 600],
                [100, 10000]
                ])
# print(data)
#Quartile
Q25,Q50,Q75 = np.percentile(data,[25,50,75],axis=0)
print(Q25)
print(Q50)
print(Q75)
#Robust Scaler using numpy
data_ans = (data-Q50)/(Q75-Q25)#with_centering=False means data/(Q75-Q25)
print('========Method-A')
print(data_ans)

print("========Method-B")
from sklearn.preprocessing import RobustScaler

rscaler = RobustScaler() #with_centering = False
data_scaled = rscaler.fit_transform(data)
print(data_scaled)
