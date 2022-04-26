#AUTHOR: Thomas Fenaroli
#DATE: 01/13/2021
#PURPOSE: Create a program that calculates current wealth accumulated from Brutus Balkcom's investment

BRUTUS_INITIAL_DEPOSIT = 1
brutus_wealth = 1

i = 0
while i < 2020:
    brutus_wealth = brutus_wealth * 1.05
    i += 1

print("In 2020, Brutus' wealth is " + str(brutus_wealth) + " dollars")