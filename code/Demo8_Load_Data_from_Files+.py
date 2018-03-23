
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import csv
from matplotlib import style


# In[2]:

style.use('ggplot')


# In[3]:

x = []
y = []


# In[13]:

'''
with open('DemoData.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
        '''


# In[4]:

import numpy as np
x, y = np.loadtxt('DemoData.txt', delimiter=',', unpack=True)


# In[5]:

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Graph : Load Data from File')
plt.legend()


# In[6]:

plt.show()


# In[ ]:




# In[ ]:



