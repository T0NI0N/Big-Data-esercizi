from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

spesaPub = [75.00, 110.00, 85.00, 115.00, 90.00, 135.00, 125.00, 140.00, 95.00, 125.00, 155.00, 145.00, 100.00, 85.00, 145.00, 105.00, 120.00, 145.00, 90.00, 80.00, 150.00, 155.00, 85.00, 100.00]
click = [15, 30, 14, 32, 20, 41, 39, 43, 27, 37, 50, 46, 28, 20, 44, 30, 36, 49, 25, 15, 47, 49, 17, 22]

spesaPub = np.reshape(spesaPub,[len(spesaPub), 1])
click = np.reshape(click, [len(click), 1])

model = LinearRegression()
model.fit(spesaPub.reshape(-1, 1), click.reshape(-1, 1))

r2 = round(model.score(spesaPub.reshape(-1,1), click.reshape(-1,1)), 3)
w1 = round(model.coef_[0][0], 3)
w0 = round(model.intercept_[0], 3)
eq = f"y = {w1}x - {abs(w0)}"

predictedValues = model.predict(spesaPub.reshape(-1, 1))

#predictionValue = int(input("inserisci coso: "))
#predicted = predictionValue * w1 + w0
#print(f"pred: {predicted}")

print(eq)
print(f"r^2 {r2}")

plt.scatter(spesaPub, click)
plt.plot(spesaPub, predictedValues, color="red")
plt.title("Regressione Lineare")
plt.xlabel("Spesa pubblicità")
plt.ylabel("Numero di click")
plt.show()