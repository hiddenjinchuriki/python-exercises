from guess_the_number_art import logo
from random import randint

EASY_ATTEMPTS_LEFT = 10
HARD_ATTEMPTS_LEFT = 5

def check_guess(user_guess, actual_answer, turns):
	"""Checks if the user guessed the correct number and returns the number of attempts remaining."""
	if user_guess > actual_answer:
		print(f"Too high. Guess again.")
		return turns - 1
	elif user_guess < actual_answer:
		print(f"Too low. Guess again.")
		return turns -1
	else:
		print(f"You got it! The answer was {actual_answer}.")

def set_difficulty():
	"""Sets the difficulty of the game."""
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if difficulty == "easy":
		return EASY_ATTEMPTS_LEFT
	else:
		return HARD_ATTEMPTS_LEFT

def game():
	"""Runs the game."""
	print(logo)
	print("Welcome to the Guess the Number Game!")
	print("I'm thinking of a number between 1 and 100.")
	answer = randint(1, 100)

	turns = set_difficulty()

	guess = 0
	while guess != answer:

		print(f"You have {turns} attempts remaining to guess the number.")
		guess = int(input("Make a guess: "))
		turns = check_guess(guess, answer, turns)

		if turns == 0:
			print(f"You've run out of guesses. You lose. The number was {answer}.")
			return

game()