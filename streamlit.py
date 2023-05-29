# -*- coding: utf-8 -*-
"""streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/122dFmFjH49Cb6pAt5hPinnkPfNh5kO5b
"""

# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Importing augmented Training data
url_traindata='https://drive.google.com/file/d/1ZDOXYMSUzUPA1lmN23j_gCbFfy6ZkqF2/view?usp=share_link'
url_traindata='https://drive.google.com/uc?id=' + url_traindata.split('/')[-2]
traindata = pd.read_csv(url_traindata)

# Drop duplicates
traindata = traindata.drop_duplicates(subset='sentence')

"""## Support Vector Machines method"""

# Split the data into training and test sets
X_train = traindata['sentence']
y_train = traindata['difficulty']

# Preprocess the data
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)


# Create a SVM object
svm = SVC()


# Test the SVM model with the best hyperparameters
svm_best = SVC(C=20, kernel='rbf', gamma='scale')
svm_best.fit(X_train, y_train)

# Prompt the user for input
user_input = input("Type a French phrase you want to classify: ")

# Print the input value
print("You entered:", user_input)

df=pd.DataFrame()
X_test_submission = vectorizer.transform([user_input])

testdata_pred=svm_best.predict(X_test_submission)

print(testdata_pred)

"""end"""
