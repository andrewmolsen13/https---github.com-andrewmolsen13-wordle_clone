from wonderwords import RandomWord

def choose_word():
    r = RandomWord()
    secret_word = r.word(word_min_length=5, word_max_length=5)
    return secret_word

def get_guess():
    player_guess = input("Guess a 5 letter word: ").lower()
    while len(player_guess) != 5:
        player_guess = input("Your guess must be 5 letters. Try again: ")

    return player_guess

guess = get_guess()
word = choose_word()

print(guess)
print(word)