
# ### stack plots is to show "parts to the whole" over time

import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([],[],color = 'm',label = 'sleeping') 
plt.plot([],[],color = 'c',label = 'eating')
plt.plot([],[],color = 'r',label = 'working')
plt.plot([],[],color = 'y',label = 'playing') # linewidth

plt.stackplot(days,sleeping,eating,working,playing ,colors =['m','c','r','y'])

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Graph: Stack Plot')

plt.show()
