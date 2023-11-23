import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

df = pd.read_csv('database_cities.csv')

dfIn = df[(df.en_seattle == "dentro")]
dfOut = df[(df.en_seattle == "fuera")]

dfIn = dfIn.sort_values(by='price', ascending=False)
dfOut = dfOut.sort_values(by='price', ascending=False)
dfIn = dfIn[:100]
dfOut = dfOut[:100]

preciosIn = np.array(dfIn['price'])
preciosOut = np.array(dfOut['price'])
#print(preciosIn)

ttest = ttest_ind(preciosIn, preciosOut, equal_var=False)
#print(ttest)

sts, pvalue = ttest

if pvalue*100 < 10 or pvalue*100 < 5:
    print("Se rechaza la hipostesis de un parecido significativo entre los precios dentro y fuera de Seattle")
else:
    print("Los precios dentro y fuera de Seattle poseen un parecido significativo")
