#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from plotcat import plotter
import serial
import random

p = plotter(figure=1)
p1 = plotter(figure=2)

@p.plot_self
def setval():
    data = [random.randint(0,100) for i in range(100)]
    p.lines[0][0].set_data(p.currentAxis, data)

@p1.plot_self
def setval2():
    data = [random.randint(0,100) for i in range(100)]
    p1.lines[0][0].set_data(p.currentAxis, data)

p.set_call_back(setval)
p1.set_call_back(setval2)

plotter.show()
