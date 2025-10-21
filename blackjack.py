import blackjack_art
import random

def deal_card():
	"""Returns random card from the deck"""
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards) # has an output
	return card

def calculate_score(cards):
	"""Takes a list of cards and returns the score calculated from the cards"""
	if sum(cards) == 21 and len(cards) == 2:
		return 0

	if 11 in cards and sum(cards) > 21:
		cards.remove(11)
		cards.append(1)

	return sum(cards)

def compare(u_score, c_score):
	if u_score == c_score:
		return "Draw 🙃"
	elif c_score == 0:
		return "You lose, computer has Blackjack."
	elif u_score == 0:
		return "User wins with Blackjack!"
	elif c_score > 21 and u_score > 21:
		return "You both bust. It's a draw."
	elif u_score > 21:
		return "You bust. Computer wins."
	elif c_score > 21:
		return "Computer busts. You win!"
	elif c_score < u_score:
		return "User wins!"
	else:
		return "You lose."

def play_game():
	print(blackjack_art.logo)
	user_cards = []
	computer_cards = []
	computer_score = -1
	user_score = -1
	is_game_over = False

	for _ in range(2):
		user_cards.append(deal_card())
		computer_cards.append(deal_card())

	while not is_game_over:
		user_score = calculate_score(user_cards)
		computer_score = calculate_score(computer_cards)
		print(f"Your cards: {user_cards}, current score: {user_score}")
		print(f"Computer's first card: {computer_cards[0]}")

		if user_score == 0 or computer_score == 0 or user_score > 21:
			is_game_over = True
		else:
			get_another_card = input(f"Type 'y' to get another card, type 'n' to pass: ")
			if get_another_card == 'y':
				user_cards.append(deal_card())
			else:
				is_game_over = True

	while computer_score < 17 and computer_score != 0:
		computer_cards.append(deal_card())
		computer_score = calculate_score(computer_cards)

	print(f"Your final hand: {user_cards}, final score: {user_score}")
	print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
	print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
	print("\n" * 20)
	play_game()