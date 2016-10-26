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
p = plotter(number_of_samples=[1000, 200, 300, 400], total_plots=4, rows=2, cols=2, names="serial-graph")

data = []

data.append([0 for i in range(1000)])
data.append([0 for i in range(200)])
data.append([0 for i in range(300)])
data.append([0 for i in range(400)])




def read_from_serial():

    while True:

        try:

            temp = ser.readline()
            try:

                [data[i].append(int(temp)/(i+1)) for i in range(4)]
                [data[i].pop(0) for i in range(4)]
                #time.sleep(0.1)

            except ValueError as Ve:
                #print(Ve)
                pass

        except AttributeError as Ae:
            #print(Ae)
            pass

        except TypeError as Te:
            #print(Te)
            pass

        except Exception as e:
            #print(e)
            pass


@p.plot_self
def setval():

    p.lines[0][0].set_data(p.currentAxis[0], data[0])
    p.lines[1][0].set_data(p.currentAxis[1], data[1])
    p.lines[2][0].set_data(p.currentAxis[2], data[2])
    p.lines[3][0].set_data(p.currentAxis[3], data[3])

if __name__ == '__main__':

    thread.start_new_thread(read_from_serial, ())
    p.set_call_back(setval)
