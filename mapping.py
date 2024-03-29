# pip install matplotlib
# pip install basemap-1.2.2-cp39-cp39-win_amd64.whl


import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import csv
# import datetime


def find_location():
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

    def plot_point(lat, lon, symbol, size):
        xpt, ypt = m(lon, lat)
        xs.append(xpt)
        ys.append(ypt)
        m.plot(xpt, ypt, symbol, markersize=size)

    csvfile = open('Meta_Data/test-data.csv', 'r', encoding='utf-8-sig')
    csv_reader = csv.reader(csvfile)

    line_count = 0
    for line in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if len(line) > 1:
                latitude, longitude = line[1], line[2]
                plot_point(float(longitude), float(latitude), 'r.', 10)
    lines = int(csv_reader.line_num)

    line_count_1 = 0
    y = True
    while y is True:
        if line_count_1 == lines:
            latitude, longitude = line[1], line[2]
            plot_point(float(longitude), float(latitude), 'b*', 10)
            y = False
        else:
            line_count_1 += 1

    m.plot(xs, ys, color='yellow')
    plt.savefig('     balloon-2/OBS_Data/OBS_Figures/Figure_1.png')    #full adress

    plt.close()


if __name__ == '__main__':
    find_location()
