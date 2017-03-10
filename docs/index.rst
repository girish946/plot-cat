.. plotcat documentation master file, created by
   sphinx-quickstart on Wed Mar  1 17:21:33 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Plotting Live Serial Data Using Plotcat
=======================================

Plot-cat is the python library for plotting live serial input.
Plotcat works on python 2.7 and later.
Plotcat comes handy when you want to plot live data that is coming
form different sensors over the serial port.
For example when you have to plot the output of a temperature sensor 
that is coming from an arduino or any other microcontroller for that matter; 
plotcat provides a very easy way to do so.


plotcat sits on the top of `matplotlib <http://matplotlib.org/>`_. and does all the initialization and drawing stuff itself. you just have to provide the list of values to be plotted.

plotcat works on linux osx and windows.
plotcat also works well with Raspberry Pi

Contents:

.. toctree::
   :maxdepth: 2

   Installation
   Usage
   PlotcatApi


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

