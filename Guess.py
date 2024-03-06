import random
def choose_word():
	words = ["beautiful", "serenity", "euphoria", "selenophile", "happiness", "solemn", "grief", "creativity", "mischief", "gullible", "freedom", "joy", "love", "hate", "forgiveness"]
	return random.choice(words)

def play_game():
	word = choose_word()
	guessed = False
	attempts = 0
	max_attempts = 5

	print("Welcome to guess the word!")
	print("Try to guess the word. It has {} letters.".format(len(word)))

	while not guessed and attempts < max_attempts:
		guess = input("Enter your guess:").lower()
		attempts += 1

		if guess == word:
			guessed = True
			print("Congratulations! You guessed the word '{}' correctly in {} attempts".format(word, attempts))

		else:
			print("Incorrect. Guess again.")

	if not guessed:
		print("Sorry, you ran out of attempts. The word was '{}'.".format(word))

play_game()


