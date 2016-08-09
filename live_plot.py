#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from plotcat import *
import serial


if __name__ == '__main__':
  ser = serial.Serial(sys.argv[1], sys.argv[2])
  p = plotter()

  data = []

  @p.plot_self
  def setval(self):
    data = [ser.readline() for i in range(100)]
    self.lines[0][0].set_data(self.currentAxis, data)

  p.set_call_back(setval)

