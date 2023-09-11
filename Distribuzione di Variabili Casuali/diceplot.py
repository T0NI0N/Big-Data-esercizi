import random
import matplotlib.pyplot as plt

# numero delle facce del dado
NUM_SIDES = 6

dado = [x for x in range(1, NUM_SIDES+1)]
sums = []

# itero i dadi per il calcolo delle somme
for i in dado:
    for j in dado:
        tot = i + j
        sums.append(tot)

# calcolo della frequenza di ogni somma
freq = [sums.count(i) for i in range(2, 2*len(dado)+1)]

# calcolo della probabilità
prob = [f/len(sums) for f in freq]

# print(sums)
# print(freq)
# print(prob)

# creazione grafico
plt.step(range(2, 2*len(dado)+1), prob)
plt.title("PDF")
plt.xlabel("Possibili risultati")
plt.ylabel("Probabilità")
plt.show()
