#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[16]:


valores = []
for i in range(5):
    valor = np.random.binomial(1, 0.1)
    valores.append(valor)
porcentaje = sum([1 for i in valores if i==0])/5
valores = np.array(valores)
print(valores)
print(porcentaje)


# In[ ]:




