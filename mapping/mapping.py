# pip install matplotlib
# pip install basemap-1.2.2-cp39-cp39-win_amd64.whl


import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import animation

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


plot_point(51, -1)
plot_point(52, -1)
plot_point(51, 0)
plot_point(50, 0)

m.plot(xs, ys, color='yellow')

plt.title('Southern England')
plt.show()
