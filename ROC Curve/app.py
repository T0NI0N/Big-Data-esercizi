import matplotlib.pyplot as plt
from sklearn import metrics

negativeObserved = [34, 74, 100, 127, 153, 114, 19, 6, 4, 0]
positiveObserved = [2, 6, 10, 12, 23, 55, 75, 41, 30, 15]

negativeCumulative = [0]
positiveCumulative = [0]

for i in range(len(negativeObserved)):
	negativeCumulative.append(negativeObserved[i] + negativeCumulative[i])
	positiveCumulative.append(positiveObserved[i] + positiveCumulative[i])

FPR = []
TPR = []

for i in range(len(negativeObserved)):
	FPR.append(1 - negativeCumulative[i] / negativeCumulative[-1])
	TPR.append(1 - positiveCumulative[i] / positiveCumulative[-1])


AUC = []

for i in range(len(TPR)-1):
	AUC.append( (FPR[i]-FPR[i+1])*TPR[i] )

plt.scatter(FPR, TPR)
plt.title("ROC Curve")
plt.xlabel("False Positive Rate (FPR)")
plt.ylabel("True Positive Rate (TPR)")
plt.annotate('AOC: %.3f'%(sum(AUC)), 
				xy=(0.95, 0.15), xycoords='data', 
				ha='right', va="center", 
				bbox=dict(boxstyle="round", fc="none", ec="gray"))

plt.show()
