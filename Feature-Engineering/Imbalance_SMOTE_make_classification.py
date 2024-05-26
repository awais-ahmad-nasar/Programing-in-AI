from imblearn.over_sampling import SMOTE
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Generate an imbalanced classification dataset
X, y = make_classification(n_samples=10000, weights=[0.95], flip_y=0, random_state=1)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Apply SMOTE to the training set
smote = SMOTE()
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Train a logistic regression model on the resampled training set
model = LogisticRegression()
# model.fit(X_train_resampled, y_train_resampled)
model.fit(X_train,y_train)

# Evaluate the performance of the trained model on the testing set
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))