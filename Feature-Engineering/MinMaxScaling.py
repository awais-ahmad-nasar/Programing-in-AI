
import numpy as np
import pandas as pd

dataset = pd.DataFrame(
    {
        "Age":[30,20,40,50,33,23,34,60,45,32],
        "SemNo":[1,5,6,2,3,7,8,9,3,2],
        "Attendance":[90,34,89,70,60,50,78,88,99,100]
    }
)

#Method-1
#Perform Normalization manually
#Min-Max Scaling
#Folrmula  NewVal = (CurVal - Xmin)/(Xmax - Xmin)

dataset_scaled = pd.DataFrame()

for feature in dataset.columns:
    feature_set = np.array(dataset[feature])
    min = feature_set.min()
    max = feature_set.max()
    feature_set = (feature_set-min)/(max-min)
    dataset_scaled[feature] = feature_set

print('=============Manually================')
print(dataset_scaled)


#method-2
print('=============SK-learn MinMax================')
from sklearn.preprocessing import MinMaxScaler
mmScaler = MinMaxScaler()
dataset_scaled1 = mmScaler.fit_transform(dataset)
dataset_scaled1 = pd.DataFrame(dataset_scaled1,columns=dataset.columns)
print(dataset_scaled1)

#Cross Check
difference = pd.DataFrame()
for feature in dataset.columns:
    difference[feature+'_D'] = np.where(round(dataset_scaled[feature],4)==round(dataset_scaled1[feature],4),0,1)

print(difference.sum())