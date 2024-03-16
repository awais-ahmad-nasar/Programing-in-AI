
#.....................By Logistic...........................

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn import datasets

iris= datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print("Accuracy:" ,accuracy*100)


################################################################################################
###############################################################################################
##############################################################################################
#.....................By KFOLD...........................

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

iris= datasets.load_iris()
X = iris.data
y = iris.target

model=LogisticRegression(max_iter=10000)

Accuracy=cross_val_score(model,X,y,cv=3)
print("Accuracy Score of Every Fold : ",Accuracy*100)



################################################################################################
###############################################################################################
##############################################################################################
#.....................By ConfusionMatrix...........................

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

# ... (previous code remains the same until model predictions)

# Calculate confusion matrix
cm = confusion_matrix(y_test, predictions)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='d',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Display classification report
print("Classification Report:")
print(classification_report(y_test, predictions, target_names=iris.target_names))
