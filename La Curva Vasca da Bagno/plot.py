###############   TASK 2    ##################

import numpy as np
from scipy.stats import norm
import matplotlib
import matplotlib.pyplot as plt

ProdA = [85,85,80,70,70,60,55,50,40,40,30,30,20,20,10]
ProdB = [50,50,50,50,50,50,50,50,50,50,50,50,50,50,49]

MediaA = np.mean(ProdA)
DevStA = np.std(ProdA)

MediaB = np.mean(ProdB)
DevStB = np.std(ProdB)

plt.figure(figsize=(10,6))

Ax1 = plt.subplot(1,2,1)
Ax2 = plt.subplot(1,2,2)

Ax1.plot(ProdA,norm.pdf(ProdA,MediaA,DevStA),
       'r-', lw=5, alpha=0.6)
Ax1.set_title("Distribuzione normale ProdA")
Ax1.axis([0,100,0,0.018])
Ax1.grid()

Ax2.plot(ProdB,norm.pdf(ProdB,MediaB,DevStB),
       'r-', lw=5, alpha=0.6)
Ax2.set_title("Distribuzione normale ProdB")
Ax2.axis([0,100,0,2])  
Ax2.grid()

plt.show()