#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[5]:


bernlli = []
for i in range(5):
    valor = np.random.binomial(1, 0.1)
    bernlli.append(valor)
print(bernlli)
distribucion = np.array(bernlli)
condicion = distribucion == 0
distribucion = distribucion[condicion]
par = []
for i in distribucion:
    if i==0:
        par.append(1)
porcent = sum(par)/5
porcent


# In[ ]:




