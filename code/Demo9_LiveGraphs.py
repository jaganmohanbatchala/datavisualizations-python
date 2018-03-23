

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

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

ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()

