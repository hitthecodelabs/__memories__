#!/usr/bin/env python
# coding: utf-8

# In[17]:


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


# In[2]:


G = nx.MultiDiGraph()
nudos = [1, 2, 3, 4, 5]
G.add_edge(1, 2)
G.add_edge(2, 1)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 2)
G.add_edge(3, 5)
G.add_edge(5, 3)
edges = G.edges
edges = [i[:2] for i in edges]
print(edges)
nx.draw_networkx(G)


# In[3]:


M = nx.to_numpy_matrix(G)
print(M)


# In[79]:


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


# In[80]:


C = []
for camino1 in P:
    for camino2 in P:
        if camino1[-1]==camino2[0]:
            camino3 = camino1 + camino2[1:]
            if len(camino3)>=6:
                camino = camino3[:6]
                if camino not in C:
                    C.append(camino)
        elif tuple(camino2) in edges and tuple(camino2[::-1]) in edges:
            camino3 = camino2*3
            camino4 = camino2[::-1]*3
            if camino3 not in C:
                C.append(camino3)
                C.append(camino4)
    
print(len(C))
C.sort()
C


# In[20]:


a = set()
for i in range(1000):
    a.add(random.randrange(0, 2))
a


# In[ ]:


C = set()
for i in range(100000): 
    C.add(np.random.binomial(10, 0.3))
C


# In[ ]:




