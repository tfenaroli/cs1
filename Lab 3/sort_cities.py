# Author: Thomas Fenaroli
# Date: 02/25/2021
# Purpose: Create and sort the list of city objects in alphabetical order, decreasing population,
# and increasing latitude

# imports files
from quicksort import *
from city import City

# returns for alphabetical order
def compare_alpha(city1, city2):
    return city1.name.lower() <= city2.name.lower()

# returns for population (decreasing) order
def compare_pop(city1, city2):
    return city1.population >= city2.population

# returns for latitude (increasing) order
def compare_lat(city1, city2):
    return city1.latitude <= city2.latitude

# opens files
world_cities = open("world_cities.txt", "r")
cities_alpha = open("cities_alpha.txt", "w")
cities_population = open("cities_population.txt", "w")
cities_latitude = open("cities_latitude.txt", "w")

# creates city_list
city_list = []

# adds city objects to city_list
for line in world_cities:
    line.strip()
    split_city = line.split(",")
    city_list.append(City(split_city[0], split_city[1], split_city[2], split_city[3], split_city[4], split_city[5]))

# sorts in alphabetical order and writes in cities_alpha
sort(city_list, compare_alpha)
for city in city_list:
    cities_alpha.write(str(city) + "\n")

# sorts in order of increasing latitude and writes in cities_latitude
sort(city_list, compare_lat)
for city in city_list:
    cities_latitude.write(str(city) + "\n")

# sorts in order of decreasing population and writes in cities_population
sort(city_list, compare_pop)
for city in city_list:
    cities_population.write(str(city) + "\n")

# closes files
world_cities.close()
cities_alpha.close()
cities_population.close()
cities_latitude.close()
