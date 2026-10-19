#Welcome player to game
#bringin wordle_functions to run program
#give player 6 guesses
import wordle_functions
guesses = []
print("Welcome to Wordle! You will try to guess a 5 letter word. But I'm sure you know how it works")
secret_word = wordle_functions.choose_word()
guess_number = 0
has_won = False
while guess_number < 6 and not has_won:
    player_guess = wordle_functions.get_guess(guesses)
    feedback = wordle_functions.evaluate_guess(player_guess, secret_word)
    wordle_functions.display_guess(player_guess, feedback)
    has_won = wordle_functions.has_won(player_guess, secret_word)
    guess_number += 1
    guesses.append(player_guess)
    

if has_won == True:
    print(f"\nThe word was {secret_word}! You got it in {guess_number} guesses!")
else:
    print(f"\nThe word was {secret_word}! Better luck next time!")
    