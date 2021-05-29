# pip install matplotlib
# pip install basemap-1.2.2-cp39-cp39-win_amd64.whl


import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import csv
# import datetime

fig, ax = plt.subplots()
fig.canvas.manager.set_window_title('test')

m = Basemap(projection='mill',
            llcrnrlat=49.339441,
            llcrnrlon=-6.336610,
            urcrnrlat=52.736292,
            urcrnrlon=2.918485,
            resolution='i')

m.drawcoastlines()
m.fillcontinents(color='g')
m.drawmapboundary(fill_color='lightblue')

xs = []
ys = []

SORlat, SORlon = 50.816446, -0.435163
xpt, ypt = m(SORlon, SORlat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'r^', markersize=15)


def plot_point(lat, lon):
    xpt, ypt = m(lon, lat)
    xs.append(xpt)
    ys.append(ypt)
    m.plot(xpt, ypt, 'r*', markersize=15)


csvfile = open('C:/Users/noaha/PycharmProjects/balloon-2/test-data.csv', 'r', encoding='utf-8-sig')
csv_reader = csv.reader(csvfile)
for line in csv_reader:
    if len(line) > 1:
        latitude, longitude = line[0], line[1]
        plot_point(float(longitude), float(latitude))

# plot_point(51, -1)
# plot_point(52, -1)
# plot_point(51, 0)
# plot_point(50, 0)
# plot_point(50, -1)

m.plot(xs, ys, color='yellow')


plt.title('Southern England')
plt.show()
