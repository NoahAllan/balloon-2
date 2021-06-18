# For the purpose of testing small amount of code

# Imports
import matplotlib.pyplot as plt
from matplotlib import style
import csv
import datetime
from altitude_conversion import altitude_converter

from threading import Thread
import threading

website = "AMIRADATA"


class first(Thread):
    def run(self):
        for l in website:
            event.wait(0.5)
            print("Give me a " + l + " !")


class second(Thread):
    def run(self):
        event.wait(5)
        print(website + " ! ")


event = threading.Event()
first().start()
second().start()