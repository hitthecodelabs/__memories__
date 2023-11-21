#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt
import random as rd
import numpy as np


# In[2]:


limits=plt.axis('off')  # turn of axis
R=nx.Graph()
nodes = [(1, 2), (1, 5), (5, 2), (2, 3), (3, 4), (4, 1)]
R.add_nodes_from([1, 2, 3, 4, 5])
R.add_edges_from([(1, 2),
                  (1, 5),
                  (5, 2), 
                  (4, 1), 
                  (2, 3), 
                  (3, 4)])
nx.draw_networkx(R)
plt.show()


# In[ ]:





# In[3]:


for i in range(len(nodes)):
    par = nodes[i]
    if par == (2, 5):
        nodes[i] = (5, 2)
    elif par == (1, 4):
        nodes[i] = (4, 1)


# In[4]:


def agregar(nodes, lista):
    idx = rd.choice([0, 1, 2, 3, 4, 5])
    x, y = nodes[idx]
    last = lista[-1]
    alast = lista[-2]
    if x == last and y != alast:
        cont = 0
        for nodo in nodes:
            z = nodo[0]
            if y == z:
                cont+=1
        if cont>0:
            lista+=[y]
    while len(lista)<5:
        if lista[-1]==5:
            lista+=[2]
        elif lista[-1]==4:
            lista+=[1]
        elif lista[-1]==3:
            lista+=[4]
        elif lista[-1]==1:
            lista+=[rd.choice([2, 5])]
        elif lista[-1]==2:
            lista+=[3]
    return lista[:5]


# In[5]:


ways = []
for i in range(10000):
    idx = rd.choice([0, 1, 2, 3, 4, 5])
    elementos = []
    valor1, valor2 = nodes[idx]
    elementos += [valor1, valor2]
    way = agregar(nodes, elementos)
    if way not in ways:
        ways += [way]
Ways = np.array(ways)
print(len(Ways))
print(Ways)


# In[6]:


print(nodes)
estocastica = np.zeros((6,6), dtype='int')
for i, j in nodes:
    #print(estocastica[i, j])
    estocastica[i, j]=1
print(estocastica)


# In[ ]:





# In[ ]:





# In[ ]:




