# Step 1 - Print 'Let's Play Rock, Paper, Scissors!'
# Step 2 - Ask the user which one they pick
# Step 3 - Randomize a pick for the computer
# Step 4 - Compare the user's pick with the computer's pick
# Step 5 - Output the winner

import random

print("******************* Let's play Rock, Paper, Scissors! *******************\n")
options = ['rock', 'paper', 'scissors']
user_choice = input("What do you choose? Type 'rock', 'paper', or 'scissors'.\n").lower()
computer_choice = random.choice(options)

if user_choice == computer_choice:
	print(f"Computer picked {computer_choice}. Draw!")
elif user_choice == 'rock':
	if computer_choice == 'paper':
		print(f"Computer picked {computer_choice}. Computer wins!")
	elif computer_choice == 'scissors':
		print(f"Computer picked {computer_choice}. You win!")
elif user_choice == 'paper':
	if computer_choice == 'rock':
		print(f"Computer picked {computer_choice}. Computer wins!")
	elif computer_choice == 'scissors':
		print(f"Computer picked {computer_choice}. Computer wins!")
elif user_choice == 'scissors':
	if computer_choice == 'paper':
		print(f"Computer picked {computer_choice}. You win!")
	elif computer_choice == 'rock':
		print(f"Computer picked {computer_choice}. Computer wins!")



