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
p = plotter(number_of_samples=1000, total_plots=4, rows=2, cols=2,)

data = [[0 for i in range(0, 1000)] for i in range(4)]


def read_from_serial():

    while True:

        try:

            temp = ser.readline()
            try:

                [data[i].append(int(temp)/(i+1)) for i in range(4)]
                [data[i].pop(0) for i in range(4)]
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

    p.lines[0][0].set_data(p.currentAxis, data[0][-1000:])
    p.lines[1][0].set_data(p.currentAxis, data[1][-1000:])
    p.lines[2][0].set_data(p.currentAxis, data[2][-1000:])
    p.lines[3][0].set_data(p.currentAxis, data[3][-1000:])

if __name__ == '__main__':

    thread.start_new_thread(read_from_serial, ())
    p.set_call_back(setval)
