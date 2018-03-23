

import matplotlib.pyplot as plt

x,y = [1,2,4],[5,7,4]

x2,y2 = [1,2,5],[8,11,5]

plt.plot(x,y, label = "Firstline")

plt.plot(x2,y2, label = "Secondline")

plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Graph Title')

plt.legend()

plt.show()




