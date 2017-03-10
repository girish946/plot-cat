#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

setup(
    name = 'plotcat',
    version = '1.0.4',
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
