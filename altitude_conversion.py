import csv
import datetime
import matplotlib.pyplot as plt
from matplotlib import style


def altitude_converter(yval, ylable, yunit, save_location, show_figure=False):
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
            x, y = line[3], line[yval]
            xs.append(float(x))
            ys.append(float(y))

    ascending_values = []
    descending_values = []

    last_input = -1.0
    for lines in xs:
        if lines <= last_input:
            descending_values.append(lines)

        else:
            ascending_values.append(lines)
        last_input = lines
    ax1.plot(ascending_values, ys[0:len(ascending_values)])
    ax = plt.gca()
    ax.tick_params(axis='x', labelrotation=60)
    plt.xlabel('ALTITUDE - (ft)')
    plt.ylabel(f'{ylable} - ({yunit})')
    plt.savefig(save_location)
    plt.tight_layout()
    if show_figure:
        plt.show()

    plt.close()


if __name__ == '__main__':
    altitude_converter(int(5), 'Temp', 'Particles per M^3',
                       '    balloon-2/OBS_Data/OBS_Figures/Oxygen_Graph', True)  #full address
