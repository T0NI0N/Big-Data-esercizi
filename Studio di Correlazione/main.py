from pandas.io.pytables import IndexCol
from ast import increment_lineno
import matplotlib.pyplot as mat
import numpy as np
import scipy.stats as sci
import pandas as pd

# salvo il csv in un dataframe, sistemiamo le colonne della tabella
di = pd.read_csv('Circolante_Basailicata.csv',usecols=[5,7],names=['Cilindrata','co2']) 

# stampo csv 
print(di)

# calcolo il coefficiente di correlazione r tra le due colonne e stampo
print(di.corr(method='pearson').iloc[0]['co2'])

# elevo alla seconda r
print(di.corr(method='pearson').iloc[0]['co2']**2) 

group1 = di.Cilindrata
group2 = di['co2']
# converto liste in array
x = np.array(group1)
y = np.array(group2)
  
# calcolo pvalue
def f_test(group1, group2):
    f = np.var(group1, ddof=1)/np.var(group2, ddof=1)
    nun = x.size-1
    dun = y.size-1
    p_value = 1-sci.f.cdf(f, nun, dun)
    return f, p_value

f, pvalue = f_test(group1, group2)

# stampo p value
print(pvalue)
# true quindi è significativo
print(pvalue < 0.05)


plotter = mat.subplot()
plotter.plot(x, y, "yo")
