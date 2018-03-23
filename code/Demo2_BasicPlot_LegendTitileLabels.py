
# coding: utf-8

# In[21]:

import matplotlib.pyplot as plt


# In[22]:

x,y = [1,2,4],[5,7,4]


# In[47]:

x2,y2 = [1,2,5],[8,11,5]


# In[48]:

plt.plot(x,y, label = "Firstline")


# In[49]:

plt.plot(x2,y2, label = "Secondline")


# In[50]:

plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Graph Title')


# In[51]:

plt.legend()


# In[52]:

plt.show()


# In[ ]:



