# Author: Thomas Fenaroli
# Date: 02/25/2021
# Purpose: Create a city class with six instance variables

# creates class as described above
class City:
    # assigns to instance variables
    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.country_code = country_code
        self.name = name
        self.region = region
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    # returns four instance variables separated by a comma
    def __str__(self):
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)
