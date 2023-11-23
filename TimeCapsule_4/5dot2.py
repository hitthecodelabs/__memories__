import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('database_cities.csv')

dfIn = df[(df.en_seattle == "dentro")]
dfOut = df[(df.en_seattle == "fuera")]

dfIn = dfIn.sort_values(by='price', ascending=False)
dfOut = dfOut.sort_values(by='price', ascending=False)
dfIn = dfIn[:100]
dfOut = dfOut[:100]

ax = sns.scatterplot(x="sqft_living", y="price", data=dfIn, alpha = 0.5)
ax = sns.scatterplot(x="sqft_living", y="price", data=dfOut, alpha = 0.5)
plt.legend(title='Ubicacion', loc='upper left', labels=['Dentro', 'Fuera'])
plt.show()
