import math

########################################################################

valProdA = [85, 85, 80, 70, 70, 60, 55, 50, 40, 40, 30, 30, 20, 20, 10]
print(f"Dati produttore A: {valProdA}")

mean = sum(valProdA) / len(valProdA)
variance = sum((v-mean)**2 for v in valProdA) / len(valProdA)
stdev = math.sqrt(variance)

print("Media produttore A: {:.2f}".format(mean))
print("Varianza produttore A: {:.2f}".format(variance))
print("Deviazione standard produttore A: {:.2f}".format(stdev))

########################################################################

valProdB = [49, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
print(f"Dati produttore B: {valProdB}")

mean = sum(valProdB) / len(valProdB)
variance = sum((v-mean)**2 for v in valProdB) / len(valProdB)
stdev = math.sqrt(variance)

print("Media produttore B: {:.2f}".format(mean))
print("Varianza produttore B: {:.2f}".format(variance))
print("Deviazione standard produttore B: {:.2f}".format(stdev))