# Imports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import csv
import datetime
style.use('fast')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def animate(i):
    csvfile = open('C:/Users/noaha/PycharmProjects/balloon-2/test-data.csv', 'r', encoding='utf-8-sig')
    csv_reader = csv.reader(csvfile)
    xs = []
    ys = []
    for line in csv_reader:
        if len(line) > 1:
            x, y = line[3], line[2]
            x1 = datetime.datetime.fromtimestamp(float(x)).strftime('%H:%M:%S')
            xs.append(x1)
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
