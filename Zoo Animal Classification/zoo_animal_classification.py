import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv('zoo.csv')
print(df.head())

df.drop('class_type')
df.remove('animal_name')
X = df.values.astype(np.float32)
Y = df.class_type
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5, random_state = 0)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, Y_train)
print("training accuracy :", model.score(X_train, Y_train))
print("testing accuracy :", model.score(X_test, Y_test))
