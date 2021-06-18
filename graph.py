# Imports
import matplotlib.pyplot as plt
from matplotlib import style
import csv
import datetime
from altitude_conversion import altitude_converter


def graph(xval, yval, xlable, ylable, xunit, yunit, save_location, show_figure=False):

    style.use('seaborn')

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)

    line_count = 0
    csvfile = open('Meta_Data/test-data.csv', 'r', encoding='utf-8-sig')
    csv_reader = csv.reader(csvfile)
    xs = []
    ys = []
    for line in csv_reader:
        # if len(line) > 1:
        if line_count == 0:
            line_count += 1
        else:
            x, y = line[xval], line[yval]
            if xval == 4:
                x1 = datetime.datetime.fromtimestamp(float(x)).strftime('%H:%M')
                xs.append(x1)
            else:
                xs.append(float(x))
            if yval == 4:
                y1 = datetime.datetime.fromtimestamp(float(y)).strftime('%H:%M')
                ys.append(y1)
            else:
                ys.append(float(y))
    ax1.plot(xs, ys)
    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=60)
    plt.xlabel(f'{xlable} - ({xunit})')
    plt.ylabel(f'{ylable} - ({yunit})')
    plt.savefig(save_location)
    plt.tight_layout()
    if show_figure:
        plt.show()

    plt.close()


if __name__ == '__main__':
    graph(int(4), int(3), 'TIME', 'ALTITUDE', 'GMT +1', 'ft',
          'C:/Users/noaha/PycharmProjects/balloon-2/OBS_Data/OBS_Figures/Altitude.png', True)
