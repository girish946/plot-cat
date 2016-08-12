# plot-cat
plot-cat is the python library for plotting live serial input.


## useage

To plot the incomming input from serial device directly.

Assuming there is one value on one line in the serial input, ie. the format of the serial input is roughly like:

    val | \r | \n 
    -----|----|----

    python live_plot.py /dev/tty<device> baudrate

### plot-cat api


To use plot-cat api.

```python 
import serial
from plotcat import *

p = plotter()

#init serial device
ser = serial.Serial('/dev/ttyAMA0', 9600)

#the callback function for plotting
@p.plot_self
def update_plot():

  data = [ser.readline() for i in range(100)]
  p.lines[0][0].set_data(p.currentAxis, data)

p.set_call_back(update_plot)

```

this is the example to recive the data from arduino (given in the example->communication->SerialEvent of the arduino IDE.)
