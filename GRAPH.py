import numpy as np
import matplotlib.pyplot as plt

languages=['C++','Java','Python','Coal']
popularity2022=[60,70,80,20]
popularity2023=[10,30,60,80]
popularity2024=[30,50,100,10]


#............................................LINE GRAPHS.....................................................
#FOR simple LINE GRAPH
# plt.plot(languages,popularity2022,marker='o',color='b')
# plt.title('POPULARITY GRAPH')
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.show()


#FOR multine LINE GRAPH
#...........................for Two lines..........................
# plt.plot(languages,popularity2022,marker='o',label='pop-22',color='b')
# plt.plot(languages,popularity2023,marker='o',label='pop-23',color='black')
# plt.legend()
# plt.title('POPULARITY GRAPH')
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.xticks(rotation=20)
# plt.show()
#...........................for Three lines..........................
# plt.plot(languages,popularity2022,marker='o',label='pop-22',color='b')
# plt.plot(languages,popularity2023,marker='o',label='pop-23',color='black')
# plt.plot(languages,popularity2024,marker='o',label='pop-24',color='r')
#
# plt.legend()
# plt.title('POPULARITY GRAPH')
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.xticks(rotation=20)
# plt.show()





#............................................BAR GRAPHS.....................................................

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FOR simple BAR GRAPH<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# plt.bar(languages,popularity2022,color=['b','r'],width=0.2)
# plt.title('POPULARITY GRAPH')
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.xticks(rotation=20)
# plt.show()


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>FOR multiple BAR GRAPH<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# plt.bar(languages,popularity2022,color='b',width=0.2)#label='pop-22')
# plt.bar(languages,popularity2023,color='r',width=0.2)#label='pop-23')
# plt.title('POPULARITY GRAPH')
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.xticks(rotation=20)
# #plt.show()

#.................................OR................................
# p22=np.arange(len(popularity2022))
# p23=[j+0.2 for j in p22]
# plt.bar(languages,popularity2022,width=0.2,color='b',label='p-2022')
# plt.bar(languages,popularity2023,width=0.2,color='black',label='p-2023')
# plt.legend()
# plt.show()


#
#Actually i don't need this kind of multi Bar as above
#
# p22=np.arange(len(languages))
# p23=[j+0.2 for j in p22]
# plt.bar(p22,popularity2022,width=0.2,color='b',label='p-2022')
# plt.bar(p23,popularity2023,width=0.2,color='black',label='p-2023')
# plt.legend()
# plt.xticks(p22+0.2/2)
# plt.show()
#.........................OR you can also do this..................
# p22=np.arange(len(languages))
# p23=[j+0.2 for j in p22]
# plt.bar(p22,popularity2022,width=0.2,color='b',label='p-2022')
# plt.bar(p23,popularity2023,width=0.2,color='black',label='p-2023')
# plt.legend()
# plt.xticks(p22+0.2/2,languages)
# plt.show()


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PIE GRAPH>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#SIMPLE
score3=[50,100,60,70,90,20,80]
score4=[20,20,20,20,20]
score5=[20,20]
# plt.pie(score3)
# plt.show()

# plt.pie(score4)
# plt.show()

# plt.pie(score5)
# plt.show()


#..........................DIFFERENT TYPE......................
# programs=['CS','AI','SE']
# admissions=[200,250,100]
# plt.pie(admissions,labels=programs)
# plt.show()

#showing %age
# programs=['CS','AI','SE']
# admissions=[200,250,100]
# plt.pie(admissions,labels=programs,autopct='%2.1f%%')
# plt.show()


#highest value ko aleeda krna
# programs=['CS','AI','SE']
# admissions=[200,250,100]
# ex=[0,0.3,0]
# plt.pie(admissions,labels=programs,autopct='%2.1f%%',explode=ex)
# plt.show()

#lowest value ko aleeda krna
# programs=['CS','AI','SE']
# admissions=[200,250,100]
# ex=[0,0,0.3]
# plt.pie(admissions,labels=programs,autopct='%2.1f%%',explode=ex)
# plt.show()


##################
# programs=['CS','AI','SE','C++']
# admissions=[200,250,100,500]
# plt.pie(admissions,labels=programs,autopct='%2.1f%%',)
# plt.title("PIE GRAPH")
# plt.show()


#AND
# programs = ['CS', 'AI', 'SE', 'C++']
# admissions = [200, 250, 100, 500]
# plt.pie(admissions, labels=[f'{program} - {admission}' for program, admission in zip(programs, admissions)], autopct='%2.1f%%',)
# plt.title("PIE GRAPH")
# plt.show()



#............................................HISTOGRAM GRAPHS.....................................................
#FOR simple HIST GRAPH
# data1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
#
# # Create a histogram
# plt.hist(data1, bins=5, edgecolor='black')
#
# # Add labels and a title
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histogram')
# plt.show()





# data2 = [10,20,30,60,70,80,90]
# plt.hist(data2, bins=5, edgecolor='black',color='red')
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histogram')
# plt.show()



#FOR Mushkil HIST GRAPH
# data3 = np.random.randn(1000)  # Generating random data for the example
# plt.hist(data3, bins=20, edgecolor='black', color='#86bf91', alpha=0.7, rwidth=0.85)
#
# # Add labels and a title
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Fancy Histogram')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.xticks(fontsize=10)
# plt.yticks(fontsize=10)
# plt.gca().spines['right'].set_visible(False)
# plt.gca().spines['top'].set_visible(False)
# plt.legend(['Data'], loc='upper right')
# plt.show()



#SIMPLE
# data2 = [10,20,30,60,70,80,90]
# plt.hist(data2, bins=5, edgecolor='black',color='red')
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histogram')
# plt.show()

#DIFFERENT
# ppl_ages=[10,20,20,40,30,60,70,30,90,80,100,60]
# data=np.random.randint(20,81,200)
#
# plt.hist(data,edgecolor='red')
# plt.show()



# data=np.random.randint(20,81,200)
# plt.hist(data,edgecolor='red',bins=3)    #bins shows intervals(groups)
# plt.show()
#


# data=np.random.randint(20,81,200)
# plt.hist(data,edgecolor='red',bins=[19,30,60,81])    #bins shows intervals(groups)
# plt.show()






#.........................................Scattering Grapgh............................................

#FOR simple SCATTERING GRAPH
# plt.scatter(languages,popularity2022)
# plt.title("Scattering Simple Graph")
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.show()

##########################################################################################################
#########################################################################################################
##########################################################################################################
##########################################################################################################



import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")

# Generate a random univariate dataset
rs = np.random.RandomState(10)
d = rs.normal(size=100)

# Plot a simple histogram and kde
sns.histplot(d, kde=True, color="m")
plt.show()


# .................show only One Diamond....................
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# import seaborn as sns
#
# # Load Titanic dataset
# # You can use your own path or load the dataset from seaborn as shown below
# # import seaborn as sns
# # titanic = sns.load_dataset('titanic')
# titanic = pd.read_csv(r'B:\MY Documents\train_TitanicAnalysis.csv')
# tips = sns.load_dataset("titanic")
# print(tips.head(5))
#
# # Encode categorical variables if needed
# le = LabelEncoder()
# titanic['Sex'] = le.fit_transform(titanic['Sex'])
# titanic['Embarked'] = le.fit_transform(titanic['Embarked'])
#
# # Compute average values
# average_values = titanic[['Pclass', 'Age', 'Fare']].mean()
#
# # Create a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Scatter plot with a diamond marker
# ax.scatter(average_values['Pclass'], average_values['Age'], average_values['Fare'], marker='D', c='r', s=100)
#
# # Set labels
# ax.set_xlabel('Pclass')
# ax.set_ylabel('Age')
# ax.set_zlabel('Fare')
#
# # Show the plot
# plt.show()



# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# tips = sns.load_dataset("titanic")
# print(tips.head(5))
# df = pd.read_csv(r'B:\MY Documents\train_TitanicAnalysis.csv')
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
# x = df['Age']
# y = df['Fare']
# z = df['Pclass']
# hue = df['Sex']
# for gender in df['Sex'].unique():
#     ax.scatter(x[df['Sex']==gender], y[df['Sex']==gender], z[df['Sex']==gender], label=gender, marker='D')
# ax.set_xlabel('Age')
# ax.set_ylabel('Fare')
# ax.set_zlabel('Pclass')
# # ax.set_title('Diamond 3D Scatter Plot of Age, Fare, and Pclass by Gender')
# ax.set_title('Diamond 3D plot')
# ax.legend()
# plt.show()

#
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import seaborn as sns
#
# # Load Titanic dataset
# # You can use your own path or load the dataset from seaborn as shown below
# # import seaborn as sns
# # df = sns.load_dataset("titanic")
# df = pd.read_csv(r'B:\MY Documents\train_TitanicAnalysis.csv')
#
# # Create a 3D plot
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
#
# # Scatter plot with a diamond marker
# for gender in df['Sex'].unique():
#     subset = df[df['Sex'] == gender]
#     x = subset['Age']
#     y = subset['Fare']
#     z = subset['Pclass']
#     ax.scatter(x, y, z, label=f'{gender} (Count: {len(subset)})', marker='D')
#
# ax.set_xlabel('Age')
# ax.set_ylabel('Fare')
# ax.set_zlabel('Pclass')
# ax.set_title('Diamond 3D Scatter Plot')
# ax.legend()
# plt.show()
#
#
#
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import seaborn as sns
#
# # Load Titanic dataset
# # You can use your own path or load the dataset from seaborn as shown below
# # import seaborn as sns
# # df = sns.load_dataset("titanic")
# df = pd.read_csv(r'B:\MY Documents\train_TitanicAnalysis.csv')
#
# # Create a 3D plot
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
#
# # Plot lines instead of scatter points
# for gender in df['Sex'].unique():
#     subset = df[df['Sex'] == gender]
#     x = subset['Age']
#     y = subset['Fare']
#     z = subset['Pclass']
#     ax.plot(x, y, z, label=f'{gender} (Count: {len(subset)})', marker='D')
#
# ax.set_xlabel('Age')
# ax.set_ylabel('Fare')
# ax.set_zlabel('Pclass')
# ax.set_title('3D Line Plot of Age, Fare, and Pclass by Gender')
# ax.legend()
# plt.show()
#
#
#
#
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# # Load Titanic dataset from Seaborn
# df = sns.load_dataset("titanic")
# print('Columns of That Dataset',df.columns)
#
# # Create a 3D plot
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
#
# # Plot lines instead of scatter points
# for gender in df['sex'].unique():
#     subset = df[df['sex'] == gender]
#     x = subset['age']
#     y = subset['fare']
#     z = subset['pclass']
#     ax.plot(x, y, z, label=f'{gender} (Count: {len(subset)})', marker='D')
#
# ax.set_xlabel('Age')
# ax.set_ylabel('Fare')
# ax.set_zlabel('Pclass')
# ax.set_title('3D Line Plot')
# ax.legend()
# plt.show()