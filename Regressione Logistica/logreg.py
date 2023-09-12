import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Importiamo i dati
df = pd.read_csv('Social_Network_Ads.csv')

# Scegliamo feature e target
X = df[['Age','EstimatedSalary']]
y = df['Purchased']

# Creazione modello
model_without_Scaling = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr').fit(X, y)
print(f'Accuracy senza scaling dei dati: {round(model_without_Scaling.score(X, y)*100,1)}%')

# Scaliamo i dati per una maggiore accuratezza
ss = StandardScaler()
X_scaled = ss.fit_transform(X)

# Divide il dataset in train set e test set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

# Creazione e addestramento del modello
reg = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr')
reg.fit(X_train, y_train)

# y_pred = reg.predict(X_test)

# Valutazione del modello e stampa accuratezza
print(f'Accuracy con dati scalati: {round(reg.score(X_test, y_test)*100)}%')

# Creazione e stampa equazione
coef = reg.coef_[0]
intercept = reg.intercept_
eq = "y = "
for i,c in enumerate(coef):
	eq +=  "{:.2f}x_{} + ".format(c,i)
eq += "{:.2f}".format(intercept[0])
print(f"Equazione: {eq}")

# Costruzione grafico
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.Paired)
plt.title("Regressione Logistica")
plt.xlabel(f"Età (scalata, min: {X['Age'].min()} max: {X['Age'].max()})")
plt.ylabel(f"Salario (scalato, min: {X['EstimatedSalary'].min()} max: {X['EstimatedSalary'].max()})")

# Calcolo curva di decisione
x_min, x_max = X_train[:, 0].min() - .5, X_train[:, 0].max() + .5
y_min, y_max = X_train[:, 1].min() - .5, X_train[:, 1].max() + .5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
Z = reg.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z = Z.reshape(xx.shape)

# Disegno curva di decisione
plt.contour(xx, yy, Z, levels=[0.5])
plt.show()