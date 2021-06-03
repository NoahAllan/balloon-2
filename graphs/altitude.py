# Imports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import csv
import datetime
from matplotlib.ticker import NullFormatter
style.use('seaborn')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

line_count = 0
csvfile = open('C:/Users/noaha/PycharmProjects/balloon-2/test-data.csv', 'r', encoding='utf-8-sig')
csv_reader = csv.reader(csvfile)
xs = []
ys = []
for line in csv_reader:
    # if len(line) > 1:
    if line_count == 0:
        line_count += 1
    else:
        x, y = line[4], line[3]
        x1 = datetime.datetime.fromtimestamp(float(x)).strftime('%H:%M')
        xs.append(x1)
        ys.append(float(y))
ax1.plot(xs, ys)
ax = plt.gca()
ax.tick_params(axis='x', labelrotation=60)
plt.savefig('C:/Users/noaha/OneDrive/Desktop/Altitude.png')

plt.show()

