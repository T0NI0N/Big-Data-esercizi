################## TASK 2 - Pearson vs. Spearman ######################

import matplotlib.pyplot as plt
import numpy as nm
import scipy.stats as sci

T = [0,5,10,15,20,30,40,60,80,100,150,200,250,300,374]
Vi = [0.0179,0.0179,0.0179,0.0179,0.0179,0.0180,0.0180,0.0183,0.0185,0.0187,0.0196,0.2070,0.0224,0.0252,0.0570]

pearsonCoefficient = sci.pearsonr(T,Vi)

rankT = sci.rankdata(T,'average')
rankVi = sci.rankdata(Vi,'average')

spearmanCoefficient = sci.spearmanr(rankT,rankVi,0,'propagate','two-sided')

plotter = plt.subplot()

plotter.scatter(T,Vi, c='yellow', edgecolors='black')
z=nm.polyfit(T,Vi,1)
p=nm.poly1d(z)

plotter.plot(T,p(T),color="purple", linewidth=3, linestyle="dotted")

plt.title('VI (I)')
plt.xlabel('T')
plt.ylabel('Vi')

plt.show()

print(pearsonCoefficient)
print(spearmanCoefficient)