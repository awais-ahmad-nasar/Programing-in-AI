import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

RANDOM_SEED = 42
LABELS = ['Normal','Fraud']

data = pd.read_csv('creditcard.csv')#,sep=',')
head= data.head()
print(head)

#Create independent and Dependent Features
columns = data.columns.tolist()
#Filter the columns to remove data we don't want
columns= [c for c in columns if c not in ['Class']]

#Store the variables we are predicting
target = 'Class'
X = data[columns]
y = data[target]

#Print the shapes of X&y
print(X.shape)
print(y.shape)

#checking null values
print(data.isnull().count())

fraud = data[data['Class']==1]
normal = data[data['Class']==0]
print("Fraud",fraud.shape)
print("Normal",normal.shape)


from imblearn.over_sampling import RandomOverSampler, SMOTE
#implement undersampling for handling imbalanced
ros = RandomOverSampler(random_state=42)
X_res,y_res = ros.fit_resample(X,y)
print(X_res.shape)
print(y_res.shape)
print(X_res)
print(y_res)
print(X_res.head(5))
#
print("...........Using SMOTE...............")
smote = SMOTE()#random_state=42) #default is 1
X_res1,y_res1 = smote.fit_resample(X,y)
print(X_res1.shape)
print(y_res1.shape)
print(X_res1.head(5))

