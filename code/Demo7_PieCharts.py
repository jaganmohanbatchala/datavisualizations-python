
# ### Pie Chart is used to show parts to the whole, and often a % share. 

import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['m','c','r','g']

plt.pie(slices, labels = activities, colors=cols)
# startangle , shadow= , explode , autopct

plt.title('Graph: Pie Chart')

plt.show()



