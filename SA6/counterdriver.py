# Author: Thomas Fenaroli
# Date: 02/10/21
# Purpose: Create a counter driver that demonstrates functionality
# of counter class
from counter import Counter

# creates count1 and count2 objects
count1 = Counter(60, 70, 4)
count2 = Counter(60, 20, 2)

# prints each counter and its value and then ticks the counters
for number in range(70):
    print(count1)
    print(count1.get_value())
    print(count2)
    print(count2.get_value())
    print(count1.tick())
    print(count2.tick())
    print("-----")
