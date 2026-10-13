#Welcome player to game
#bringin wordle_functions to run program
#give player 6 guesses
from wordle_functions import get_guess, choose_word

print("Welcome to Wordle! You will try to guess a 5 letter word. But I'm sure you know how it works")

player_guess = get_guess()
secret_word = choose_word()

print(player_guess)


