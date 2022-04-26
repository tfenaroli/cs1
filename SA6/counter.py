# Author: Thomas Fenaroli
# Date: 02/10/21
# Purpose: Create a counter class and define methods for this class

# creates class Counter
class Counter:
    # initializes variables
    def __init__(self, limit, initial=0, min_digits=1):
        self.limit = limit
        if initial in range(limit):
            self.value = initial
        else:
            print("Error: Invalid initial value")
            self.value = self.limit - 1
        self.min_digits = min_digits

    # gets the integer value of counter
    def get_value(self):
        return int(self.value)

    # ticks the counter
    def tick(self):
        self.value -= 1
        if self.value < 0:
            self.value = self.limit - 1
            return True
        return False

    # returns counter
    def __str__(self):
        if len(str(self.value)) < self.min_digits:
            value = "0" * (self.min_digits - len(str(self.value))) + str(self.value)
        else:
            value = str(self.value)

        return value
