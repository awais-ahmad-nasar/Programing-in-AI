from sklearn.preprocessing import RobustScaler
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
#Perform Robust manually
#Robust Scaling
# Folrmula  Xnew = (X - Q50)/IQR
#where IQR = Q75-Q25

dataset_scaled = pd.DataFrame()

for feature in dataset.columns:
    feature_set = np.array(dataset[feature])
    # print(feature_set)
    q25,q50,q75 = np.percentile(feature_set,[25,50,75])
    iqr = q75-q25
    print(q25,q50,q75)
    feature_set = (feature_set - q50)/iqr
    dataset_scaled[feature] = feature_set

print('=============Withoud SK-Learn================')
print(dataset_scaled)


#method-2
print('=============SK-learn RobustScaler================')
sScaler = RobustScaler()
dataset_scaled1 = sScaler.fit_transform(dataset)
dataset_scaled1 = pd.DataFrame(dataset_scaled1,columns=dataset.columns)
print(dataset_scaled1)

#comparing both results
difference = pd.DataFrame()
for feature in dataset.columns:
    difference[feature+'_D'] = np.where(round(dataset_scaled[feature],4)==round(dataset_scaled1[feature],4),0,1)

print(difference.sum())