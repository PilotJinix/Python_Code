import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix

# referensi
# https://towardsdatascience.com/building-a-k-nearest-neighbors-k-nn-model-with-scikit-learn-51209555453a
# https://tatwan.github.io/How-To-Plot-A-Confusion-Matrix-In-Python/

# read data
df = pd.read_csv('data.csv')  # data hasil ekstraksi fitur praktikum
# check data has been read in properly
df.head()

print(df)

# create a dataframe with all training data except the target column
X = df.drop(columns=['class'])
# check that the target variable has been removed
X.head()
print('X:')
print(X)

# separate target values
y = df['class'].values

print('y:')
print(y)

from sklearn.model_selection import train_test_split

# split dataset into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4, stratify=y)

print('X_train: ')
print(X_train)
print('X_test: ')
print(X_test)
print('y_train: ')
print(y_train)
print('y_test: ')
print(y_test)

from sklearn.neighbors import KNeighborsClassifier

# Create KNN classifier
jml_k = 3
knn = KNeighborsClassifier(n_neighbors=jml_k)
# Fit the classifier to the data
knn.fit(X_train, y_train)

# show first 5 model predictions on the test data
result = knn.predict(X_test)
print('==============================')

print('y_test (true class): \n', y_test)

print('result (predicted class):\n', result)

akurasi = knn.score(X_test, y_test)
print('\nakurasi: %.3f%%' % (100 * akurasi))

conf_matrix = confusion_matrix(y_test, result)
print('================================ ')
print('Confusion matrik data testing: ')
print(conf_matrix)

plt.clf()
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Wistia)
classNames = ['Negative', 'Positive']
plt.title('Confusion Matrix Testing Data, Kelas Jambu atau Nangka')
plt.ylabel('True label')
plt.xlabel('Predicted label')
tick_marks = np.arange(len(classNames))
plt.xticks(tick_marks, classNames, rotation=45)
plt.yticks(tick_marks, classNames)
s = [['TN', 'FP'], ['FN', 'TP']]
# ~ s = [['TN (True negatif)','FP (False positif)'], ['FN (False negatif)', 'TP (True Positif)']]
for i in range(2):
    for j in range(2):
        plt.text(j, i, str(s[i][j]) + " = " + str(conf_matrix[i][j]))
plt.show()
