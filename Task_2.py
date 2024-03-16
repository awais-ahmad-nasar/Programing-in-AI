
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# Import data
df = pd.read_csv("heart.csv")

# Splitting the data into features (X) and the target (y)
X = df.drop(columns=['target'])
y = df['target']

target_counts = df['target'].value_counts()
print(target_counts)
# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
predicted_result = model.predict(X_test)

# Calculate and print the accuracy
accuracy = accuracy_score(y_test, predicted_result)
print("...............................................................\nAccuracy: ", accuracy)
'''

#***************************************************************************************************************
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score

df=pd.read_csv('heart.csv')

X=df.drop(columns=['target'],axis=1)
Y=df['target']

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=10)

# print(X)
# print()
# print(Y)

models=[LogisticRegression(max_iter=100000),svm.SVC(kernel='linear'),KNeighborsClassifier(),RandomForestClassifier()]

for model in models:
    model.fit(x_train,y_train)
    result=model.predict(x_test)
    accuracy=accuracy_score(y_test,result)
    print(model,accuracy)
    print("Stratified K-fold")
    score=cross_val_score(model,X,Y,cv=5)
    print(model,score,score.mean())
    print()
    print()
    print()
'''
#***************************************************************************************************************

'''
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# Import data
df = pd.read_csv("heart.csv")

# Data Splitting
X = df.drop(columns=['target'])
y = df['target']

# Model
model = LogisticRegression(max_iter=10000)  # Increase max_iter to a larger value

scores = cross_val_score(model, X, y, cv=5)

# Print Scores
print("Max Score : ",np.max(scores))
print("Min Score : ",np.min(scores))
avg = np.mean(scores)
print("Average    : ",avg)
'''
###############################################################################################
###############################################################################################
#########################################(K-FOLD PGRMS)########################################
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
digits=load_digits()


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(digits.data,digits.target)

#####################Logistic Regression####################
lr=LogisticRegression(solver='liblinear',multi_class='ovr')
lr.fit(X_train,y_train)

print("LOGISTIC REGRESSION SCORE : ",lr.score(X_test,y_test))

#################Cross Validation Score##########################
from sklearn.model_selection import cross_val_score
cvs=cross_val_score(LogisticRegression(solver='liblinear',multi_class='ovr'),digits.data,digits.target,cv=3)

print("CROSS VAL SCORE : ",cvs,"\n")

###################(By LOOPS same above PGRM)##################
#....................................................................................................
#.....Random values....
from sklearn.model_selection import KFold
digits = load_digits()
kf = KFold(n_splits=3)
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3)
print("...............................RANDOM DATA..................................\n")
for train_index,test_index in kf.split([1,2,3,4,5,6,7,8,9]):
    print(train_index,test_index)

print("....................................................................................")
lr=LogisticRegression(solver='liblinear',multi_class='ovr')
lr.fit(X_train,y_train)
a=lr.score(X_test,y_test)
print("Full Score :",a)


b=cross_val_score(LogisticRegression(solver='liblinear',multi_class='ovr'),digits.data,digits.target,cv=4)
print("Each Folds Score :",b)

#...................................................................................
#..... Build in values....
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits

# Load the digits dataset
digits = load_digits()

# Define the number of folds
n_splits = 3
kf = KFold(n_splits=n_splits)

# Initialize a list to store accuracy scores
score_Logistic = []

# Loop through the folds
for train_index, test_index in kf.split(digits.data):
    X_train, X_test = digits.data[train_index], digits.data[test_index]
    y_train, y_test = digits.target[train_index], digits.target[test_index]

    # Create and train the Logistic Regression model
    model = LogisticRegression(solver='liblinear', multi_class='ovr')
    model.fit(X_train, y_train)

    # Calculate and store the accuracy score
    score = model.score(X_test, y_test)
    score_Logistic.append(score)

print("\n.....DATA BUIDIN.....\nScores for each Fold:", score_Logistic)

