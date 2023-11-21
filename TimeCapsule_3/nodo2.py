#!/usr/bin/env python
# coding: utf-8

# In[14]:


import networkx as nx
import matplotlib.pyplot as plt
import random as rd
import numpy as np


# In[15]:


H=nx.DiGraph()
H.add_nodes_from([1, 2, 3, 4, 5])
H.add_edges_from([(1, 2), 
                  (2, 1), 
                  (2, 3), 
                  (3, 4), 
                  (4, 5), 
                  (5, 2), 
                  (3, 5), 
                  (5, 3)
                 ])

pos = nx.spring_layout(H)  # positions for all nodes
# nodes
nx.draw_networkx_nodes(H, pos)
# edges
nx.draw_networkx_edges(H, pos)
# node labels
nx.draw_networkx_labels(H, pos, font_family='sans-serif')
plt.axis('off')
plt.show()


# In[16]:


nodes = list(H.edges)
nodes


# In[34]:


def agregar(nodes, lista):
    idx = rd.choice([0, 1, 2, 3, 4, 5, 6, 7])
    x, y = nodes[idx]
    last = lista[-1]
    if x == last:
        cont = 0
        for nodo in nodes:
            z = nodo[0]
            if y == z:
                cont+=1
        if cont>0:
            lista+=[y]
    while len(lista)<6:
        #print(lista)
        if lista[-1]==5:
            i = rd.choice([0, 1])
            dt = [2, 3]
            lista+=[dt[i]]
        elif lista[-1]==2:
            i = rd.choice([0, 1])
            dt = [1, 3]
            lista+=[dt[i]]
        elif lista[-1]==1:
            lista+=[2]
        elif lista[-1]==3:
            i = rd.choice([0, 1])
            dt = [4, 5]
            lista+=[dt[i]]
        elif lista[-1]==4:
            lista+=[5]
    return lista[:6]


# In[35]:


ways = []
for i in range(10000):
    idx = rd.choice([0, 1, 2, 3, 4, 5, 6, 7])
    lista = []
    valor1, valor2 = nodes[idx]
    lista += [valor1, valor2]
    #print(lista)
    way = agregar(nodes, lista)
    if way not in ways:
        ways += [way]
    #print()

print(len(ways))
ways.sort()
ways


# In[ ]:





# In[ ]:





# In[6]:


estocastica = np.zeros((6,6), dtype='int')
for i, j in nodes:
    #print(estocastica[i, j])
    estocastica[i, j]+=1
print(estocastica)


# In[ ]:




