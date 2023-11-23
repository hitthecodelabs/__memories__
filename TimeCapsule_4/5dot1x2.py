import time
t1 = time.time()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('database_cities.csv')
#5.1
dfS = df[(df.size_label == "small")]
dfM = df[(df.size_label == "medium")]
dfB = df[(df.size_label == "big")]
meanS = dfS.groupby(['city']).mean()
meanM = dfM.groupby(['city']).mean()
meanB = dfB.groupby(['city']).mean()
means = meanS['price']
meanm = meanM['price']
meanb = meanB['price']
dict1 = dict(means)
dict2 = dict(meanm)
dict3 = dict(meanb)
v1 = list(dict1.values())
v2 = list(dict2.values())
v3 = list(dict3.values())
ciudades = list(dict1.keys())
di = {}
for i in range(len(v1)):
    small = v1[i]
    medium = v2[i]
    big = v3[i]
    ciudad = ciudades[i]
    di[ciudad] = [float(str(small/1000)[:5]), float(str(medium/1000)[:5]), float(str(big/1000)[:5])]

di = pd.DataFrame.from_dict(di, orient='index', columns=['SMALL', 'MEMIUM', 'BIG'])
di = di.T
plt.figure(figsize=(15, 7))
plt.title('Precio medio en cada una de las distintas ciudades para cada tamaño', size = 9)
sns.heatmap(di, annot=True, fmt=".1f", linewidths=2, square = True, cmap = 'Blues_r', cbar_kws={'label': 'Precio en miles', 'orientation': 'horizontal'})
sns.set(font_scale=.3)
t2 = time.time()
print(t2 - t1)
plt.show()