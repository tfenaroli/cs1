# Author: Thomas Fenaroli
# Date: 02/10/21
# Purpose: Create a timer class and define methods for this class
from counter import Counter


# creates class Timer
class Timer:
    # initializes instance variables
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(24, hours, 2)
        self.minutes = Counter(60, minutes, 2)
        self.seconds = Counter(60, seconds, 2)

    # ticks seconds, minutes, and hours accordingly
    def tick(self):
        if self.seconds.tick() and self.minutes.tick():
            self.hours.tick()

    # determines if timer reads 00:00:00
    def is_zero(self):
        if self.seconds.get_value() == 0 and self.minutes.get_value() == \
                0 and self.hours.get_value() == 0:
            return True
        return False

    # returns timer
    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
