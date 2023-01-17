#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,np.pi*2,100)

y1 = 0.62*652*0.192 * np.sin(x)*np.cos(x) 
y2 = (np.sqrt(1-1.42*np.sin(x)))+62*652*np.sin(x)

y = y1 / y2

z1 = 263564.48*0.192*np.cos(2*x)+0.036864*np.sin(x)
z2 = np.power((1-1.42*np.sin(x)),1.5)+np.cos(x)
z  = z1 / z2


plt.plot(x,y)
plt.plot(x,z)

plt.show()


# In[ ]:




