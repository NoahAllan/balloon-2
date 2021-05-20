# pip install matplotlib
# pip install basemap-1.2.2-cp39-cp39-win_amd64.whl


import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m = Basemap(projection='mill',
            llcrnrlat=49.339441,
            llcrnrlon=-6.336610,
            urcrnrlat=52.736292,
            urcrnrlon=2.918485,
            resolution='i')

m.drawcoastlines()

SORlat, SORlon = 50.816446, -0.435163

xpt, ypt = m(SORlon, SORlat)
m.plot(xpt, ypt, 'g*', markersize=15)

plt.title('Southern England')
plt.show()