
import matplotlib.pyplot as plt
import csv
from matplotlib import style

style.use('ggplot')

x = []
y = []

'''
with open('DemoData.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
        '''

import numpy as np
x, y = np.loadtxt('DemoData.txt', delimiter=',', unpack=True)

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Graph : Load Data from File')
plt.legend()

plt.show()

