import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snb

df = pd.read_csv("placement.csv")
print(df.shape)

sample = df.sample(5)
print(sample)

plt.figure(figsize=(16,5))
plt.subplot(1,2,1)
snb.distplot(df['cgpa'])
# plt.show()

plt.subplot(1,2,2)
snb.distplot(df['placement_exam_marks'])
# plt.show()

sk = df['placement_exam_marks'].skew()
print(sk)

sk = df['cgpa'].skew()
print(sk)

mean = df['cgpa'].mean()
std = df['cgpa'].std()
max= df['cgpa'].max()
min = df['cgpa'].min()

print("Mean value of cgpa",mean)
print("Std value of cgpa",std)
print("Min value of cgpa",min)
print("Max value of cgpa",max)

highestVal = mean + 3*std
lowestVal = mean - 3*std

print("Highest allowed",highestVal)
print("Lowest allowed",lowestVal)

#finding the outliers

outliers = df[(df['cgpa']>highestVal) | (df['cgpa']<lowestVal)]
print(outliers)

#Trimming
new_df = df[(df['cgpa']<=highestVal) & (df['cgpa']>=lowestVal)]
print(new_df.describe())