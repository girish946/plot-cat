Using Plotcat
=============

To plot the incomming input from serial device directly.
Assuming there is one value on one line in the serial input, 
ie. the format of the serial input is roughly like:

    +----------------+
    | val | \\r | \\n|
    +----------------+

You can use the command line tool live_plot.py

    .. code-block:: bash

        python live_plot.py -d /dev/tty<device> -b baudrate


