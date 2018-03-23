
# coding: utf-8

# ### Pie Chart is used to show parts to the whole, and often a % share. 

# In[1]:

import matplotlib.pyplot as plt


# In[35]:

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]


# In[36]:

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['m','c','r','g']


# In[44]:

plt.pie(slices, labels = activities, colors=cols)
# startangle , shadow= , explode , autopct


# In[45]:

plt.title('Graph: Pie Chart')


# In[46]:

plt.show()


# In[ ]:




# In[ ]:



