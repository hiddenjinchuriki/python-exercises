# Step 1 - Print 'Welcome to the Basic PyPassword Generator!'
# Step 2 - Ask the user how many letters they would like in their password and store that in num_of_letters
# Step 3 - Ask the user how many symbols they would like in their password and store that in num_of_symbols
# Step 4 - Ask the user how many numbers they would like in their password and store that in num_of_numbers
# Step 5 - Generate a password that has x amount of letters, y amount of symbols, and z amount of numbers
# Step 6 - Print 'Your password is: letters + symbols + numbers'

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("************* Welcome to the Basic Password Generator! *************\n")
# num_of_letters = int(input("How many letters would you like in your password?\n "))
# num_of_symbols = int(input("How many symbols would you like?\n "))
# num_of_numbers = int(input("How many numbers would you like?\n "))
# new_password = []
#
# for char in range(0, num_of_letters):
# 	new_password.append(random.choice(letters))
# for char in range(0, num_of_symbols):
# 	new_password.append(random.choice(symbols))
# for char in range(0, num_of_numbers):
# 	new_password.append(random.choice(numbers))
#
# new_password = "".join(new_password)
#
# print(f"Your new password is: {new_password}")


# How to improve
# Randomize the password so it is not a predictable letters, symbols, numbers

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("************* Welcome to the Basic Password Generator! *************\n")
num_of_letters = int(input("How many letters would you like in your password?\n "))
num_of_symbols = int(input("How many symbols would you like?\n "))
num_of_numbers = int(input("How many numbers would you like?\n "))
new_password = []
shuffled_password = []

for char in range(0, num_of_letters):
	new_password.append(random.choice(letters))
for char in range(0, num_of_symbols):
	new_password.append(random.choice(symbols))
for char in range(0, num_of_numbers):
	new_password.append(random.choice(numbers))

random_password = list(new_password)
random.shuffle(random_password)
random_password = "".join(random_password)

print(f"Your new password is: {random_password}")

