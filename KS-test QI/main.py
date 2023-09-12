import math
import statistics as st
from scipy.stats import norm

qi = [119, 126, 130, 121, 121, 117, 139, 130, 120, 114, 120]
qi.sort()

print(f"QI F: {qi}")

n = len(qi)
print(f"Numerosità dataset: {n}")

# calcolo media
mediaF = st.mean(qi)
print(f"Media QI F: {mediaF}")

# calcolo deviazione standard
varF = sum((l-mediaF)**2 for l in qi) / (n-1) 
devstdF = math.sqrt(varF)
print(f"Deviazione standard QI F: {devstdF}")

# calcolo valore atteso
valAtteso = [i/n for i in range(n)]
print(f"Valore atteso QI F: {valAtteso}")

# calcolo vaolre reale tramite distribuzione normale
valReale = norm(mediaF, devstdF).cdf(qi)
print(f"Valore reale QI F: {valReale}")

# calcolo distanza
dist = [abs(r - a) for r, a in zip(valReale, valAtteso)]
print(f"Distanza valore reale - atteso: {dist}")

# calcolo distanza massima
maxDist = max(dist)
print(f"Distanza massima: {maxDist}")

# vaolre oracolo (da tabella)
valOracolo = 0.39122
print(f"Valore critico oracolo (n=11, alpha=0.05): {valOracolo}")

# stampa del risultato
res = "Distribuzione Normale" if (maxDist - valOracolo) else "Distribuzione non Normale"
print(f"Risultato KS-test su QI F: {res}")