from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

df=pd.read_csv('titanic.csv',usecols=['Pclass','Age','Fare'])
df2=df.copy()

def Normalization(X,Xmin,Xmax):
    return (X-Xmin)/(Xmax-Xmin)

normAge=[Normalization(i,df['Age'].min(),df['Age'].max()) for i in df['Age']]
df['Age']=np.round(normAge,decimals=2)
normPclass=[Normalization(i,df['Pclass'].min(),df['Pclass'].max()) for i in df['Pclass']]
df['Pclass']=np.round(normPclass,decimals=2)
normFare=[Normalization(i,df['Fare'].min(),df['Fare'].max()) for i in df['Fare']]
df['Fare']=np.round(normFare,decimals=2)

mScalar=MinMaxScaler()

NormDf=np.round(mScalar.fit_transform(df2),decimals=2)
NormDf=pd.DataFrame(NormDf,columns=['Pclass','Age','Fare'])

match_count = (df == df2).sum().sum()
total_elements = df.size  # Total number of elements in the DataFrame
percentage_match = (match_count / total_elements) * 100
print(f"Percentage of matching elements: {percentage_match*100 :.2f}%")