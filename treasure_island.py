# Step 1 - Print the Treasure Island Game Logo
# Step 2 - Display the 'Welcome to Treasure Island Game\n' 'Your mission is to find the treasure.' message
# Step 3 - Let the user know 'You're at a crossroad. Do you want to go "Left" or "Right"?'
# Step 4 - 'Left' takes them to a lake with an island in the middle. Ask if they want to 'Wait' or 'Swim'.
#			Chose 'Right' and they fall into a drap and die. Game over.
# Step 5 - 'Swim' finds them eaten by a shark. 'Wait' a boat comes and picks them up and takes them to another island
# Step 6 - Upon arrival at the island, they are greeted with three doors: 'Red', 'Yellow', and 'Blue'.
# Step 7 - 'Red' door finds them burned alive by lava. 'Blue' door finds them eaten by a beast. 'Yellow' door takes
# 			them to the treasure and they win. Any other answers beside 'Red', 'Yellow', or 'Blue' they were stung by a
# 			poisonous spider.

from treasure_island_logo import logo
print(logo)
print("Welcome to the Basic Treasure Island Game! Can you find the treasure?\n")
print("You follow a trail and come across a fork in the trail. \n")
first_choice = input("Do you go left or right? (Type 'left' or 'right')\n")

keep_going = True
while keep_going:

	if first_choice == 'right':
		print("You fell into a cavern and starved to death. Sucks to be you. ")
		print("************** Game Over Loser **************")
		keep_going = False
	elif first_choice == 'left':
		print("You made it past the cavern and are now facing the ocean. There is an island barely in the distance.")
		second_choice = input("Do you wait for a boat to come which could take days or do you swim? Type 'wait' or 'swim'.\n")
		if second_choice == 'swim':
			print("You were eaten by a sea creature. You're dead.")
			print("************** Game Over Loser **************")
			keep_going = False
		elif second_choice == 'wait':
			print("A boat finally came and you've arrived at the island. You now see a house with three doors.")
			third_choice = input("One red, one yellow, one blue. Which door do you choose? Type 'red', 'yellow', or 'blue'.\n")
			if third_choice == 'red':
				print("You fell into a trap and got yourself blowed up. Iiiidiot")
				print("************** Game Over Loser **************")
				keep_going = False
			elif third_choice == 'blue':
				print("You were mauled by a werewolf. You dead bruh.")
				print("************** Game Over Loser **************")
				keep_going = False
			else:
				print("You found the treasure chest with the treasure. You rich bitch!")
				print("I'll take my share please.")
				keep_going = False



