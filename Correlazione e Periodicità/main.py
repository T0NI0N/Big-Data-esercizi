################## Task3: Correlazione e Periodicità ##################

import matplotlib.pyplot as plt
from scipy.stats import pearsonr

SHIFT = 7

data = [100, 90, 80, 80, 90, 60, 40, 105, 95, 80, 85, 95, 60, 35, 100, 90, 75, 80, 90, 65, 40, 105, 90, 80, 85, 90, 55, 35]
values = [x for x in range(len(data))]


base = data[0:7]
y = []

for i in range(1, len(data) + 1 - SHIFT):
	shifted = data[(i):(i + SHIFT)]
	corr, _ = pearsonr(base, shifted)
	y.append(corr)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4))

ax1.plot(values, data, 'r')
ax1.set_title("Traffico a Milano")
ax1.set_xlabel("Giorni")
ax1.set_ylabel("Indice traffico")

ax2.plot([x for x in range(len(y))], y, 'o-')
ax2.axhline(0, color='blue', linestyle=':')
ax2.set_title("Autocorrelazione")
ax2.set_xlabel("Shift")
ax2.set_ylabel("Coeff. Autocorr.")

fig.tight_layout()
plt.show()