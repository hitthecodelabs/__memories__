#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


G = nx.MultiDiGraph()
#R.add_nodes_from([1, 2, 3, 4, 5])
nudos = [1, 2, 3, 4, 5]
G.add_edge(1, 4, weight=1)
G.add_edge(4, 3, weight=1)
G.add_edge(3, 2, weight=1)
G.add_edge(2, 5, weight=1)
G.add_edge(2, 1, weight=1)
G.add_edge(5, 1, weight=1)
nx.draw_networkx(G)


# In[3]:


M = nx.to_numpy_matrix(G, nodelist=[1,2,3,4,5])
print(M)


# In[4]:


paths = []
lista1 = []

for i in range(len(nudos)):
    nudo = nudos[i]
    for j in nudos:
        path = nx.all_simple_paths(G, nudo, j)
        lista2 = list(path)
        paths.append(lista2)
P = []
lista3 = []
for i in paths:
    if len(i)==1:
        lista3 += i
    elif len(i)==2:
        for j in i:
            lista3+=[j]
    else:
        a = lista3
        b = lista3 + [[]]
        borrar = []
        for k in range(len(a)):
            frst = set(a[k])
            scnd = set(b[k+1])
            if frst.issubset(scnd) and a[k]==b[k+1][:-1]:
                borrar.append(k)
        dele = [a[i] for i in borrar]
        for l in dele:
            a.remove(l)
        for p in a:
            if p not in P:
                P.append(p)
        lista3 = []


# In[ ]:





# In[5]:


C = []
for camino1 in P:
    for camino2 in P:
        if camino1[-1]==camino2[0]:
            camino3 = camino1 + camino2[1:]
            if len(camino3)>=5:
                camino = camino3[:5]
                if camino not in C:
                    C.append(camino)
print(len(C))
C


# In[ ]:




