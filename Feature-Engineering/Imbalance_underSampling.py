import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# rcParams['figure.figsize'] = 10,6
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
print("------")
print(data.isnull().count())
print("------")

count_classes =  pd.Series(y).value_counts()
count_classes.plot(kind='bar',rot=0)
plt.title("Transaction Class Distribution")
plt.xticks(range(2),LABELS)
plt.xlabel("Class")
plt.ylabel('Frequency')
plt.show()

fraud = data[data['Class']==1]
normal = data[data['Class']==0]
print("Fraud",fraud.shape)
print("Normal",normal.shape)
#
from imblearn.under_sampling import RandomUnderSampler, NearMiss
#implement undersampling for handling imbalanced
rus = RandomUnderSampler(random_state=42)
X_res,y_res = rus.fit_resample(X,y)
print(X_res.shape)
print(y_res.shape)
#
nm1 = NearMiss(version=1) #default is 1
X_res1,y_res1 = nm1.fit_resample(X,y)
print(X_res1.shape)
print(y_res1.shape)
print(X_res1.head(5))
#
#
nm2 = NearMiss(version=2)
X_res1,y_res1 = nm2.fit_resample(X,y)
print(X_res1.shape)
print(y_res1.shape)
print(X_res1.head(5))
#
#
nm3 = NearMiss(version=3)
X_res1,y_res1 = nm3.fit_resample(X,y)
print(X_res1.shape)
print(y_res1.shape)
print(X_res1.head(5))

# from imblearn.under_sampling import TomekLinks
# tl = TomekLinks()
# X_res1,y_res1 = tl.fit_resample(X,y)
# print(X_res1.shape)
# print(y_res1.shape)
# print(X_res1.head(5))

import  seaborn as sns
print(data[columns[5]].max())
print(data[columns[5]].min())
sns.scatterplot(x=columns[1],y=columns[2],hue=target,data=data)
plt.show()