#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plotcat import * 
import sys
import serial
import argparse
import time
if sys.version_info[0] < 3:
    import thread

else:
    import _thread as thread


def read_from_serial(ser, data):

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


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='tool for plotting live\
                                                  serial data')

    parser.add_argument('-d',
                        '--SerialDevice',
                        type=str,
                        default='/dev/ttyUSB0',
                        help='serial device from which the input is coming.')

    parser.add_argument('-b',
                        '--Baudrate',
                        type=int,
                        default=9600,
                        help='the baudrate of serial device.')

    parser.add_argument('-n',
                        '--Samples',
                        type=int,
                        default=1000,
                        help='number of samples to be plotted.')

    parser.add_argument('-ymin',
                        '--Yminimum',
                        type=int, default=0,
                        help='lower limit of Y-Axis')

    parser.add_argument('-ymax',
                        '--Ymaximum',
                        type=int,
                        default=1024,
                        help='upper limit of Y-Axis')

    parser.add_argument('-p',
                        '--Plots',
                        type=int,
                        default=1,
                        help='total number of subplots to be created')

    parser.add_argument('-r',
                        '--Rows',
                        type=int,
                        default=1,
                        help='number of rows on the figure.')

    parser.add_argument('-c',
                        '--Cols',
                        type=int,
                        default=1,
                        help='number of columns on the figure.')

    parser.add_argument('-t',
                        '--Titles',
                        nargs='+',
                        type=str,
                        default=['serial-graph'],
                        help='titles for plots.')

    args = parser.parse_args()

    data = [0 for i in range(0, args.Samples)]

    p = plotter(number_of_samples=args.Samples, total_plots=args.Plots,
                rows=args.Rows, cols=args.Cols, y_low_lim=args.Yminimum,
                y_high_lim=args.Ymaximum, names=args.Titles)

    @p.plot_self
    def setval():
        for i in range(len(p.lines)):
            p.lines[i][0].set_data(p.currentAxis[i], data)

    
    ser = serial.Serial(args.SerialDevice, args.Baudrate)
    thread.start_new_thread(read_from_serial, (ser, data, ))
    p.set_call_back(setval)
