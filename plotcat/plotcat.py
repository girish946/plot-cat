#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pylab
import random


class plotter:

    """plotter initiates a matplotlib plot. This plot is used to plot the
    serial input."""

    def __init__(self, number_of_samples=100, total_plots=1, rows=1,
                 cols=1, y_low_lim=0, y_high_lim=1024,
                 plot_lines=1, names='serial-graph', time_interval=10):

        """initializes the figure with the specified number of subplots
           (arg: total_plots)
        """
        self.fig = pylab.figure(1)
        self.currentAxis = []
        
        self.plots = []
        self.lines = []
        if (type(number_of_samples) == int):
            NOS_val = number_of_samples
            number_of_samples = [NOS_val for i in range(total_plots)]

        elif type(number_of_samples) == list and not len(number_of_samples) == total_plots:
            raise ValueError("lenght of list number_of_samples must be equal to total number of plots")

        else:
            pass

        if type(names) == str:
            name_val = names
            names = [name_val for i in range(total_plots)]

        elif type(names) == list and  not len(names) == total_plots:
            raise ValueError("lenght of list of names must be equal to total number of plots")

        else:
            pass

        if (type(y_low_lim) == int):
            y_low_lim_val = y_low_lim
            y_low_lim = [y_low_lim_val for i in range(total_plots)]

        elif type(y_low_lim) == list and not len(y_low_lim) == total_plots:
            raise ValueError("lenght of list y_low_lim must be equal to total number of plots")

        else:
            pass

        if (type(y_high_lim) == int):
            y_high_lim_val = y_high_lim
            y_high_lim = [y_high_lim_val for i in range(total_plots)]

        elif type(y_high_lim) == list and not len(y_high_lim) == total_plots:
            raise ValueError("lenght of list y_high_lim must be equal to total number of plots")

        else:
            pass

        if (type(plot_lines) == int):
            plot_lines_val = plot_lines
            plot_lines = [plot_lines_val for i in range(total_plots)]

        elif type(plot_lines) == list and not len(plot_lines) == total_plots:
            raise ValueError("lenght of list y_high_lim must be equal to total number of plots")

        else:
            pass


        for i in range(total_plots):
            self.currentAxis.append(range(0, number_of_samples[i]))

        
        count = 1
        for i in range(rows):
            for j in range(cols):

                new_plot = self.fig.add_subplot(((rows * 100) + (cols * 10)
                                                 + count))
                for k in range(plot_lines[count-1]):

                    samples = number_of_samples[count -1]
                    new_line = new_plot.plot(self.currentAxis[count-1],
                                         [random.randint(y_low_lim[count-1],
                                                         y_high_lim[count-1])
                                          for i in
                                          range(0, samples)])
                    self.lines.append(new_line)

                pylab.title(names[count-1])
                self.plots.append(new_plot) 
                if count == total_plots:
                    break
                count += 1
        self.manager = pylab.get_current_fig_manager()
        self.timer = self.fig.canvas.new_timer(interval=time_interval)

    def set_call_back(self, func):

        """sets callback function for updating the plot.
        in the callback function implement the logic of reading of serial input
        also the further processing of the signal if necessary has to be done
        in this
        callbak function."""

        self.timer.add_callback(func)
        self.timer.start()
        pylab.show()

    def plot_self(self, func):

        """define your callback function with the decorator @plotter.plot_self.
        in the callback function set the data of lines
        in the plot using self.lines[i][j].set_data(your data)"""

        def func_wrapper():

            func()

            try:

                self.manager.canvas.draw()

            except ValueError as ve:
                print(ve)
                pass

            except RuntimeError as RtE:
                print(RtE)
                pass

            except Exception as e:
                print(e)
                pass

        return func_wrapper
