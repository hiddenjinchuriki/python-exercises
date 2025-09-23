# Step 1 - Print out 'Welcome to the Band Name Generator'
# Step 2 - Ask the user to provide their favorite city but on a new line
# Step 3 - Store that in a variable fav_city
# Step 4 - Ask the user to provide their favorite pet's name but on a new line
# Step 5 - Store that in a variable fav_pet
# Step 6 - Print out 'Your band name could be <fav_city> <fav_pet>'
#
# print("Welcome to the Basic Band Name Generator!\n")
# fav_city = input("What is your favorite city? \n")
# fav_pet = input("What is your favorite pet's name? \n")
# print(f"Your band name could be {fav_city} {fav_pet}!")

#==============================================================

# How to improve
# Use lists so that users can provide their top ten favorite cities and top ten favorite animals and pick randomly
#   from the lists

import random

print("Welcome to the New and Improved Band Name Generator!")
list_of_cities = []
list_of_animals = []
keep_asking_cities = True
keep_asking_animals = True

while keep_asking_cities:
	list_of_cities.append(input("Enter the name of a city: "))
	city_answer = input("Would you like to keep providing a city name? (Type 'y' or 'n'): ").lower()
	if city_answer == 'n':
		keep_asking_cities = False

while keep_asking_animals:
	list_of_animals.append(input("Enter the name of a animal: "))
	animal_answer = input("Would you like to keep providing an animal? (Type 'y' or 'n'): ").lower()
	if animal_answer == 'n':
		keep_asking_animals = False

print(f"Your band name could be {random.choice(list_of_cities)} {random.choice(list_of_animals)}!")

# How to improve further
# Ask user how many words they would like their band name to be (2-4)
# Ask them what categories they would like the words to be chosen from (City, Animal or Car brand, City, Planet)
# Have prepopulated lists for each optional category, list of Planets, list of 100 cities, list of 100 animals, etc