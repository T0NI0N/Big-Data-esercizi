###############   Task3: Test di Permutazione    ##################

import numpy as np
import random as rn
import matplotlib.pyplot as plt

n = 1000000
permutazioni = []
frequenze = [0 for i in range(4*3*2)]

for n in range(0, n):

    elem = ["1","2","3","4"]
    temp = []

    # ciclo che genera la permutazione
    for n in range(0, 4):
        temp.append(rn.choice(elem))
        elem.remove(temp[-1])

    # controllo sulla presenza della permutazione nella lista
    temp = "".join(temp)
    if temp not in permutazioni:
        permutazioni.append(temp)

    # incremento del contatore della permutazione
    ind = permutazioni.index(temp)
    frequenze[ind] = frequenze[ind] + 1

for n in range(len(permutazioni)):    
    print(f"Permutazione: {permutazioni[n]} Frequenza: {frequenze[n]}")

plt.figure(figsize=(12, 6))
ax = plt.subplot()
p = ax.barh(permutazioni, frequenze, edgecolor="white", linewidth=0.7)
ax.bar_label(p)
ax.set_xlabel("Frequenza")
ax.set_ylabel("Permutazioni")
ax.set_title('Frequenze delle permutazioni di 4 numeri')

plt.show()