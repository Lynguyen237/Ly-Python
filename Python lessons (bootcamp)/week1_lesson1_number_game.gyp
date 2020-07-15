import random

def play_game():

    secret_number = random.randint(1, 100)
    guess = None
    too_low = 0
    too_high = 101
    num_guesses = 0

    print(f"Shh... the secret number is {secret_number}")

    while secret_number != guess:
        num_guesses += 1
        guess = int((too_high - too_low) / 2) + too_low
        print(f"Too High = {too_high}, Too Low = {too_low}, Guess = {guess}")

        if guess > secret_number:
            too_high = guess
        if guess < secret_number:
            too_low = guess
    
    print (f"You guessed the number in {num_guesses} times.")

play_game ()