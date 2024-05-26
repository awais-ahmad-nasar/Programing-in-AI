from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load the titanic data with specific columns

df = pd.read_csv("titanic.csv",usecols=['Pclass','Age',"Fare",'Survived'])
print(df.head())
print(df.shape)
print(df.isnull().sum())
#Age column has NaN values, so fill them with median
df['Age'].fillna(df.Age.median(),inplace=True)
print('-------------')
print(df.isnull().sum())


### Independent and dependent features
X=df.iloc[:,1:]
y=df.iloc[:,0]

#divide train and test using split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


#Normalization : we use MinMaxScaler from sklearn library
from sklearn.preprocessing import MinMaxScaler
mmscaler = MinMaxScaler()
x_train_mmscale = mmscaler.fit_transform(X_train)

print('******************')
print("MIN",x_train_mmscale.min())
print("MAX",x_train_mmscale.max())
print(pd.DataFrame(x_train_mmscale).head())
df_age = df['Age']
min = df_age.min()
max = df_age.max()
result = [(v-min)/(max-min) for v in df_age]
print(pd.DataFrame(result).min())
print('******************')

#### standarisation: We use the Standardscaler from sklearn library
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
### fit vs fit_transform the X_train
X_train_scaled=scaler.fit_transform(X_train)
print('------X_train after fit_transform----')
print(X_train)
# print(round(X_train_scaled.sd(),3))

#Just transform the X_test
X_test_scaled=scaler.transform(X_test)

### Model Building
## fit() for training and predict for test
from sklearn.linear_model import LogisticRegression
classification=LogisticRegression()

classification.fit(X_train_scaled,y_train)
predicted_result = classification.predict(X_test_scaled)

from sklearn.metrics import accuracy_score

score = accuracy_score(y_test,predicted_result)
print(score)

classification1=LogisticRegression()
classification1.fit(X_train,y_train)
predicted_result = classification1.predict(X_test)
score = accuracy_score(y_test,predicted_result)
print(score)
# df_scaled=df_scaled.transform(df)