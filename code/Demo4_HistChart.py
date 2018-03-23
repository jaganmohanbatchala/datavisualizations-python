
# coding: utf-8

# ###  histograms tend to show distribution by grouping segments together

# In[4]:

import matplotlib.pyplot as plt


# In[5]:

population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,122,130,111,151,115,112,80,75,65,54,44,42,48]


# In[6]:

bins = [0,10,20,30,40,50,60,70,80,90,100,120]


# In[7]:

plt.hist(population_ages, bins , histtype='bar', rwidth=0.8)


# In[8]:

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph: Hist Chart')


# In[9]:

plt.legend()


# In[10]:

plt.show()


# In[ ]:



