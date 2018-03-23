
# coding: utf-8

# ### scatter plots is usually to compare two variables, or three if you are plotting in 3 dimensions, looking for correlation or groups

# In[2]:

import matplotlib.pyplot as plt


# In[3]:

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]


# In[4]:

plt.scatter(x,y,label='skitcat', color='r',s=250)


# In[11]:

# google matplotlib marker option
plt.scatter(x,y,label='skitcat', color='r',s=200, marker = '*')


# In[12]:

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph: Scatter Plot')


# In[13]:

plt.show()


# In[ ]:



