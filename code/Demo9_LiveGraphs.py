
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


# In[2]:

style.use('fivethirtyeight')


# In[10]:

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


# In[11]:

def animate(i):
    graph_data = open('DemoData.txt','r').read()
    lines = graph_data.split('\n')
    xaxis = []
    yaxis = []
    for line in lines:
        if len(line) > 1:
            x, y =line.split(',')
            xaxis.append(x)
            yaxis.append(y)
    ax1.clear()
    ax1.plot(xaxis,yaxis)


# In[12]:

ani = animation.FuncAnimation(fig, animate, interval=1000)


# In[13]:

plt.show()


# In[ ]:




# In[ ]:



