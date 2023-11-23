import time
t1 = time.time()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from timeit import timeit

df = pd.read_csv('database_cities.csv')
#5.1
zipcodes = list(df["zipcode"])
dataZ = pd.read_csv('zipcode-database.csv')
zips = list(dataZ["zipcode"])
cities = list(dataZ["City"])
city = []
for i in range(len(zips)):
    zip = zips[i]
    citi = cities[i]
    for code in zipcodes:
        if zip == code:
            city += [citi]
df["city"] = city
Sciudad = []
Mciudad = []
Bciudad = []
Sprecio = []
Mprecio = []
Bprecio = []
sizes = list(df["size_label"])
precios = list(df['price'])
ciudades = list(df['city'])
for i in range(len(precios)):
    precio = precios[i]
    ciudad = ciudades[i]
    size = sizes[i]
    if size == 'small':
        Sciudad += [ciudad]
        Sprecio += [precio]
    elif size == 'medium':
        Mciudad += [ciudad]
        Mprecio += [precio]
    elif size == 'big':
        Bciudad += [ciudad]
        Bprecio += [precio]
def promedioCiudad(listaCiudadesPorTamanio, listaCiudadesPorPrecio):
    promCiud = []
    for city in listaCiudadesPorTamanio:
        total = 0
        cont = 0
        for i in range(len(listaCiudadesPorTamanio)):
            ciudad = listaCiudadesPorTamanio[i]
            precio = listaCiudadesPorPrecio[i]
            if city == ciudad:
                cont += 1
                total += precio
        promedio = total / cont
        promCiud += [(city, promedio)]
    return list(set(promCiud))
ciudadesPreciosSmall = promedioCiudad(Sciudad, Sprecio)
ciudadesPreciosMedium = promedioCiudad(Mciudad, Mprecio)
ciudadesPreciosBig = promedioCiudad(Bciudad, Bprecio)
def ciudadesPreciosTamanios(cSmall, cMedium, cBig):
    dict = {}
    for inf in cSmall:
        ciudad = inf[0]
        precio = inf[1]/1000
        precio= float(str(precio)[:6])
        if ciudad not in dict:
            dict[ciudad] = [precio]
        else:
            dict[ciudad] += [precio]
    for inf in cMedium:
        ciudad = inf[0]
        precio = inf[1]/1000
        precio= float(str(precio)[:6])
        if ciudad not in dict:
            dict[ciudad] = [precio]
        else:
            dict[ciudad] += [precio]
    for inf in cBig:
        ciudad = inf[0]
        precio = inf[1]/1000
        precio= float(str(precio)[:6])
        if ciudad not in dict:
            dict[ciudad] = [precio]
        else:
            dict[ciudad] += [precio]
    return dict
dict = ciudadesPreciosTamanios(ciudadesPreciosSmall, ciudadesPreciosMedium, ciudadesPreciosBig)
dfx = pd.DataFrame.from_dict(dict, orient='index', columns=['SMALL', 'MEMIUM', 'BIG'])
dfx = dfx.T
plt.figure(figsize=(10, 5))
plt.title('Precio medio en cada una de las distintas ciudades para cada tamaño', size = 9)
sns.heatmap(dfx, annot=True, fmt=".1f", linewidths=2, square = True, cmap = 'Blues_r', cbar_kws={'label': 'Precio en miles', 'orientation': 'horizontal'})
sns.set(font_scale=.5)
t2 = time.time()
t3 = t2-t1
print(t3)
print(t3/60)
plt.show()
#DUVALL POSEE LA CASA GRANDE MAS CARA