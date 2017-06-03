#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from plotcat import plotter
import serial

ser = serial.Serial(sys.argv[1], sys.argv[2])
p = plotter()

data = []


@p.plot_self
def setval():
    data = [ser.readline() for i in range(100)]
    p.lines[0][0].set_data(p.currentAxis[0], data)

p.set_call_back(setval)
plotter.show()
