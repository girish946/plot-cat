#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

description = '''
plot-cat is the python library for plotting live serial input. plotcat works on
python 2.7 and later. plotcat comes handy when you want to plot live data that 
is coming form different sensors over the serial port, SPI, websocket, tcp socket etc.

For example you have to plot the output of a temperature sensor that is coming 
from an [arduino](https://www.arduino.cc/) or any other microcontroller for
that matter; plotcat comes handy for such tasks.

plotcat sits on the top of [matplotlib](http://matplotlib.org/) and does all 
the initialization and drawing stuff itself. you just have to provide the list 
of values to be plotted.

plotcat works on linux osx and windows. plotcat also works well with 
[Raspberry Pi](https://www.raspberrypi.org/)

## install plotcat

from pip 
```bash 
pip install plotcat
```

or from github


```bash
git clone https://github.com/girish946/plot-cat.git

pip install -r requirements.txt

python install setup.py install

```

on fedora 22 and above

```bash

dnf copr enable girish946/plotcat

dnf install python-plotcat
```

for ubuntu

```bash

wget https://github.com/girish946/plot-cat/blob/master/dist/python-plotcat_1.0.0.1-1_all.deb

sudo dpkg -i python-plotcat_1.0.0.1-1_all.deb
```
'''

setup(
    name = 'plotcat',
    version = '1.0.5',
    author = 'girish joshi',
    author_email = 'girish946@gmail.com',
    description = ("""tool to plot live serial input"""),
    packages = ['plotcat'], 
    install_requires = ['matplotlib', 'pyserial'], 
    keywords = 'serial input plotting realtime data matplotlib Raspberry_pi ',
    scripts = ['live_plot.py'], 
    long_description = """tool to plot live serial input""",
    license="GPL v3",
    
  )
