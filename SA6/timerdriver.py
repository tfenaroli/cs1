# Author: Thomas Fenaroli
# Date: 02/10/21
# Purpose: Create a timer driver that prints out all times between and including
# 01:30:00 and 00:00:00 using the Timer class
from timer import Timer

# creates timer1 object
timer1 = Timer(1, 30, 0)

# prints and ticks timer1
for i in range(5401):
    print(timer1)
    timer1.tick()
