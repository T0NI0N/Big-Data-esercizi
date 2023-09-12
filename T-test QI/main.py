import math
import statistics as st
from scipy.stats import skew
from scipy.stats import kurtosis
from scipy.stats import ttest_ind


qiF = [119, 126, 130, 121, 121, 117, 139, 130, 120, 114, 120]
qiM = [130, 113, 111, 117, 122, 118, 120, 114, 112, 116, 120]

print(f"QI F: {qiF}")
print(f"QI M: {qiM}")

n = len(qiF)
print(f"Numerosità dataset: {n}")

meanF = st.mean(qiF)
print(f"Media QI F: {meanF}")

meanM = st.mean(qiM)
print(f"Media QI M: {meanM}")


varF = sum((l-meanF)**2 for l in qiF) / (n-1) 
devstdF = math.sqrt(varF)
print(f"Deviazione standard QI F: {devstdF}")

varM = sum((l-meanM)**2 for l in qiM) / (n-1) 
devstdM = math.sqrt(varM)
print(f"Deviazione standard QI M: {devstdM}")

print(f"Mediana QI F: {st.median(qiF)}")
print(f"Mediana QI M: {st.median(qiM)}")

##############################################
asF = skew(qiF, bias=False)
print(f"Asimmetria F: {asF}")

asM = skew(qiM, bias=False)
print(f"Asimmetria M: {asM}")

print(f"Curtosi F: {kurtosis(qiF, bias=False)}")
print(f"Curtosi M: {kurtosis(qiM, bias=False)}")

normF = "si" if (asF < 2 and asF > -2) else "no"
print(f"QI F distrib. normale? {normF}")

normM = "si" if (asM < 2 and asM > -2) else "no"
print(f"QI M distrib. normale? {normM}")

##############################################

t_stat, p_value = ttest_ind(qiF, qiM)
print("Valore T: ", t_stat) 
print("Valore P: ", p_value)


t1 = [95, 0.05]
res1 = "si" if (p_value < t1[1]) else "no"
print(f"Livello significatività {t1[0]}%: p < {t1[1]}, significativo? {res1}")

t2 = [99, 0.01]
res2 = "si" if (p_value < t2[1]) else "no"
print(f"Livello significatività {t2[0]}%: p < {t2[1]}, significativo? {res2}")