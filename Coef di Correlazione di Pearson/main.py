
################## TASK 1 - Pearson vs. Spearman ######################

import numpy as np 
from matplotlib import pyplot as plt
import scipy.stats as sci

x = [-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3]
y = np.abs(x)

pearsonCoefficient = sci.pearsonr(x,y)

plt.title("Y=|X|")
plt.plot(x,y,"bo")
plt.grid(True)
plt.axvline(0, color='black')
plt.axhline(0, color='black')
plt.show()

print(pearsonCoefficient)
