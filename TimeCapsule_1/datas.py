import pandas as pd
import numpy as np
import random

###### EJERCICIO 1
print('\n')
print('PREGUNTA UNO')
# a
datas = pd.read_csv('bank_edited.csv', sep=';')
# print('PREGUNTA UNO')
nomenclatura = set(datas['marital'])
print(len(nomenclatura))
print(nomenclatura)

# b
datas.loc[datas.marital == 'DIVORCED', 'marital'] = 'divorced'
datas.loc[(datas.marital == "Single") | (datas.marital == "sing") | (datas.marital == "SINGLE"), "marital"] = "single"
datas.loc[(datas.marital == "maried") | (datas.marital == "Married") | (datas.marital == "MARRIED") | (
        datas.marital == "marrid"), "marital"] = "married"

# c
nomenclatura = set(datas['marital'])  # devuelve nuevamente los valores de 'marital', pero ahora unificados
print(nomenclatura)


###### EJERCICIO 2
# a
print('\n')
print('PREGUNTA DOS')
def any_is_null(x):
    return any(pd.isnull(x))
atributos = np.array(list(datas))
a = datas.apply(any_is_null)
M = np.array(a)
columnas = atributos[M]
print(columnas)
#b
df = pd.DataFrame(np.array(datas))
a = df.isnull().sum()
a = np.array(list(a))
alMenosUno = len(a[a > 0])  # al menos un valor perdido
print(alMenosUno)
# c
alMenosTres = len(a[a >= 3])  # al menos tres valores perdidos
print(alMenosTres)
# d
df = df.dropna()

###### EJERCICIO 3
print('\n')
print('PREGUNTA TRES')
#a
datas = datas.dropna()  # elimina los valores nulos, permitiendo discretizar la columna 'duration'

# desc = datas['duration'].describe()
# a
datas['disc_1'] = pd.qcut(datas['duration'], 10)
disc1 = datas.loc[1:1000, ['duration', 'disc_1']]
print(disc1)

# b
datas['disc_2'] = pd.cut(datas['duration'], 10)
disc2 = datas.loc[1:1000, ['duration', 'disc_1', 'disc_2']]
print(disc2)

datas3 = datas
###### EJERCICIO 4
print('\n')
print('PREGUNTA CUATRO')
datas['disc_balance'] = pd.cut(datas['balance'], 4)
disc = datas.loc[1:4000, ['balance', 'disc_balance']]
dat_balance = datas["balance"]  # datos del balance

intervalos = []
cuantiles = set(datas["disc_balance"])
for i in cuantiles:
    intervalos.append(i)

atributosBinarios = []
for i in dat_balance:
    ceros = [0, 0, 0, 0]
    if i in intervalos[0]:
        ceros[0] += 1
        atributosBinarios.append(ceros)
    elif i in intervalos[1]:
        ceros[1] += 1
        atributosBinarios.append(ceros)
    elif i in intervalos[2]:
        ceros[2] += 1
        atributosBinarios.append(ceros)
    elif i in intervalos[3]:
        ceros[3] += 1
        atributosBinarios.append(ceros)
M_balance = np.array(atributosBinarios)
b1 = M_balance[:, 0]
b2 = M_balance[:, 1]
b3 = M_balance[:, 2]
b4 = M_balance[:, 3]
datas['balance_01'] = pd.DataFrame(b1)
datas['balance_02'] = pd.DataFrame(b2)
datas['balance_03'] = pd.DataFrame(b3)
datas['balance_04'] = pd.DataFrame(b4)
datas = datas.dropna()
balance_binario = datas.loc[900:1100, ['balance', 'balance_01', 'balance_02', 'balance_03', 'balance_04']]
print(balance_binario)


###### EJERCICIO 5
print('\n')
print('PREGUNTA CINCO')
M_data = np.array(datas)
l_data = []
list_yes = []
list_no = []
a = len(list_yes) + len(list_no)

while a < 20:
    indices = set()
    while len(list_yes) < 10:
        a = random.randrange(4400)
        if a not in indices:
            atributos = list(M_data[a, :])
            if atributos[4] == 'yes':
                list_yes.append(atributos)
                l_data.append(atributos)
                indices.add(a)
    while len(list_no) < 10:
        a = random.randrange(4400)
        if a not in indices:
            atributos = list(M_data[a, :])
            if atributos[4] == 'no':
                list_no.append(atributos)
                l_data.append(atributos)
                indices.add(a)
datas2 = datas
m_data = np.array(l_data)
atributos = list(datas2)
for i in range(len(atributos)):
    valores = m_data[:,i]
    datas2[atributos[i]] = pd.DataFrame(valores)
datas2 = datas2.dropna()
print(datas2)


###### EJERCICIO 6

# Escogeria la columna siguiente, "y"
# muestra los datos unicos por cada cliente afirmando o negando su deposito a largo plazo
# la funcion .corr() requiere de datos de dos en dos
# dada la asigncion de escoger una unica columna -lo que restringe la utilizacion de la funcion .corr()- la mejor opcion es la columna "y"

# Asi se mostraria por pantalla:
#datas3 = datas3.dropna()
#siOno = list(datas3['y'])
#unocero = ['si', 'no']
#for i in range(len(siOno)):
#    if siOno[i] == 'yes':
#        print('El cliente #' + str(i+1) + ' ' + unocero[0] + ' contrato un deposito a largo plazo.')
#    elif siOno[i] == 'no':
#        print('El cliente #' + str(i+1) + ' ' + unocero[1] + ' contrato un deposito a largo plazo.')
