#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plotcat import plotter
import sys
import serial
import time

if sys.version_info[0] < 3:
    import thread

else:
    import _thread as thread


ser = serial.Serial(sys.argv[1], sys.argv[2])
p = plotter(number_of_samples=1000)

data = [0 for i in range(0, 1000)]


def read_from_serial():

    while True:

        try:

            temp = ser.readline()
            try:

                data.append(int(temp))
                data.pop(0)
                time.sleep(0.0001)

            except ValueError:
                pass

        except AttributeError as Ae:
            pass

        except TypeError:
            pass

        except:
            pass


@p.plot_self
def setval():

    p.lines[0][0].set_data(p.currentAxis[0], data)

if __name__ == '__main__':

    thread.start_new_thread(read_from_serial, ())
    p.set_call_back(setval)
    plotter.show()
