#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plotcat import *
import sys
import serial
import argparse

if sys.version_info[0] < 3:
  import thread

else: 
  import _thread as thread

import time


p = plotter(number_of_samples = 1000)

data = [0 for i in range(0,1000)]

def read_from_serial(ser):

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

  p.lines[0][0].set_data(p.currentAxis, data)

if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='tool for plotting live serial data')
  parser.add_argument('-d', '--SerialDevice', type=str,
                    help='serial device from which the input is coming.')

  parser.add_argument('-b', '--Baudrate', type=int,
                    help='the baudrate of serial device.')



  args = parser.parse_args()
  #print (args.SerialDevice, args.Baudrate)

  ser = serial.Serial(args.SerialDevice, args.Baudrate)
  thread.start_new_thread(read_from_serial, (ser))
  p.set_call_back(setval)

