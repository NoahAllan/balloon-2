# where all programs run

from threading import Thread
import threading
from mapping import find_location
from graph import graph
import keyboard
from altitude_conversion import altitude_converter

time_interval = 10
event = threading.Event()

z = True
while z is True:
    graph(int(4), int(3), 'TIME', 'ALTITUDE', 'Hours : Minutes', 'ft',
          'C:/Users/noaha/PycharmProjects/balloon-2/OBS_Data/OBS_Figures/Altitude.png',
          False)
    print('Altitude Graph')
    find_location()
    print('Map')
    altitude_converter(int(7), 'Humidity', 'Particles per M^3',
                       'C:/Users/noaha/PycharmProjects/balloon-2/OBS_Data/OBS_Figures/Oxygen_Graph', False)
    print('Humidity Graph')
    altitude_converter(int(6), 'Oxygen Levels', 'Particles per M^3',
                       'C:/Users/noaha/PycharmProjects/balloon-2/OBS_Data/OBS_Figures/Humidity_Graph', False)
    print('Oxygen')
