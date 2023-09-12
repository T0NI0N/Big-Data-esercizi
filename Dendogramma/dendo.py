import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

df = pd.read_csv("housings.csv", sep=',')

print(df.head())
print(df.tail())

X = df.loc[:, ["median_income", "latitude", "longitude"]].head(100)

# Calcoliamo la matrice di linkage per l'albero di clustering agglomerativo
Z = linkage(X, 'ward')

# Disegniamo il dendrogramma
plt.title('Dendrogramma di un albero di clustering agglomerativo')
dendrogram(Z, leaf_rotation=90., leaf_font_size=8.,)
plt.show()