import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv('BankNote_Authentication.csv')

# print(df.columns)

X=df.iloc[:,:-1]
Y=df.iloc[:,-1]

# print(X.head())
# print(Y.head())


x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=0)

# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(y_test.shape)

# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(y_test.shape)

classifier=RandomForestClassifier()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)

from  sklearn.metrics import accuracy_score

score=accuracy_score(y_test,y_pred)

# print(score)

import pickle

pickle_out=open('classifier.pkl','wb')
pickle.dump(classifier,pickle_out)
pickle_out.close()

print(x_test)