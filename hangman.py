# Step 1 - Import the logo from hangman art and print it at the start of the game
# Step 2 - Randomly choose a word from the word_list as the chosen_word
# Step 3 - Ask the user to guess a letter and assign as guess
# Step 4 - Check if the letter the user guessed is in chosen_word. Print 'right' if it is, print 'wrong' if not
# Step 5 - Create a placeholder with the same number of blanks as letters in chosen_word
# Step 6 - Create a display that displays the guessed letter in the right spot of chosen_word, otherwise, print an '_'
# Step 7 - Use a while loop to let the user guess again
# Step 8 - Change the for loop so that you keep the previous correct guess in the display
# Step 9 - Set lives to be 6
# Step 10 - If the guess is not in chosen_word, a life should be lost. If lives reaches 0 the game is over.
# Step 11 - Print the ASCII are from 'stages' that corresponds to the number of lives left in the game
# Step 12 - Let the user know how many lives they have left at the beginning of each guess

import hangman_art
import random

print(hangman_art.logo, "\nWelcome to the Hangman Game!\n")
chosen_word = random.choice(hangman_art.word_list)

placeholder = ""
for letter in chosen_word:
	placeholder += "_"
# print(chosen_word)
print(f"The word is: {placeholder}")

keep_going = True
correct_letters = []
lives = 6

while keep_going:
	print(f"********** You have {lives}/6 lives remaining. **********")
	guess = input("Guess a letter: ").lower()
	display = ""

	if guess in correct_letters:
		print(f"You've already guessed the letter {guess}. Try again.")

	for char in chosen_word:
		if char == guess:
			display += char
			correct_letters.append(guess)
		elif char in correct_letters:
			display += char
		else:
			display += "_"

	print(display)

	if guess not in chosen_word:
		print(f"The letter '{guess}' is not in the word. Guess again.")
		lives -= 1
		if lives == 0:
			print(f"******************* You lose! The word was: {chosen_word} *******************")
			keep_going = False

	if "_" not in display:
		print("******************* You win! ******************* ")
		keep_going = False

	print(hangman_art.stages[lives])

