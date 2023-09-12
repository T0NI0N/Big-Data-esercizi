import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


df = pd.read_csv("email.csv")
print(df)

data = pd.get_dummies(df, drop_first=True)

X = data.drop('valida_si', axis=1)
y = data['valida_si']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = GaussianNB()

model.fit(X_train, y_train)

acc_train = model.score(X, y)
print("Accuracy = %0.4f " % acc_train)

p = model.predict([[1,0,0,1,1]])
print(p)