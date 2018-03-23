
# coding: utf-8

# In[4]:

import matplotlib.pyplot as plt


# In[5]:

x = [2,4,6,8,10]
y = [6,7,8,2,4]


# In[6]:

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]


# In[7]:

plt.bar(x, y, label="FirstBar", color='lightblue')
plt.bar(x2, y2, label="SecondBar", color='c')


# In[8]:

plt.xlabel('Bar Number')
plt.ylabel('Bar Height')
plt.title('Graph: Two Bars')


# In[9]:

plt.legend()


# In[10]:

plt.show()


# In[ ]:



