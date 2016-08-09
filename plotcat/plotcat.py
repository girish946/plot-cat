#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pylab
import sys
import time


class plotter:

  def __init__(self, number_of_samples = 100, total_plots = 1):

    self.fig = pylab.figure(1)
    self.currentAxis = pylab.arange(0, number_of_samples, 1)

    self.plots = []
    self.lines = []
    for i in range(total_plots):
      new_plot = self.fig.add_subplot(111)
      new_line = new_plot.plot(self.currentAxis, self.currentAxis)
      self.plots.append(new_plot)
      self.lines.append(new_line)


    self.manager = pylab.get_current_fig_manager()
    self.timer = self.fig.canvas.new_timer(interval = 10)



  def set_call_back(self, func):

    self.timer.add_callback(func)
    self.timer.start()
    pylab.show()


  def plot_self(self, func):
    def func_wrapper():
      func(self)
      try:
        self.manager.canvas.draw()
      except ValueError:
        pass
      except RuntimeError as RtE:
        pass
      except:
        pass
    return func_wrapper
