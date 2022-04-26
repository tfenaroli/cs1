#AUTHOR: Thomas Fenaroli
#DATE: 01/13/2021
#PURPOSE: Create a program that calculates first year in which Brutus' balance
# exceeds Portia's balance and prints the year and the two balances in that year

brutus_wealth = 1
portia_wealth = 100000
BRUTUS_INTEREST_MULTIPLIER = 1.05
PORTIA_INTEREST_MULTIPLIER = 1.04

i = 0
while i < float("inf"):
    brutus_wealth = brutus_wealth * BRUTUS_INTEREST_MULTIPLIER
    portia_wealth = portia_wealth * PORTIA_INTEREST_MULTIPLIER
    i += 1
    if brutus_wealth >= portia_wealth:
        print("Brutus' balance first exceeds Portia's in " + str(i) + " A.D., when Brutus' balance is " + str(brutus_wealth) + " dollars and Portia's balance is " + str(portia_wealth) + " dollars")
        exit()
