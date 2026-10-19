import random
words = [
    "apple", "beach", "brain", "bread", "chair",
    "chest", "cloud", "coast", "dance", "dream",
    "drink", "earth", "faith", "field", "flame",
    "floor", "fruit", "ghost", "glass", "grape",
    "grass", "green", "heart", "horse", "house",
    "juice", "knife", "lemon", "light", "magic",
    "money", "month", "mouse", "music", "night",
    "ocean", "paint", "paper", "party", "peace",
    "peach", "phone", "piano", "piece", "pilot",
    "pizza", "place", "plane", "plant", "plate",
    "point", "power", "queen", "quiet", "radio",
    "river", "robot", "round", "salad", "scale",
    "scene", "score", "shark", "sheep", "shirt",
    "shore", "sleep", "smile", "snake", "snowy",
    "sound", "space", "spoon", "sport", "stage",
    "stone", "store", "storm", "story", "sugar",
    "table", "teach", "tiger", "toast", "today",
    "total", "touch", "tower", "track", "train",
    "truck", "trust", "uncle", "value", "video",
    "voice", "water", "whale", "world", "youth"
]

def choose_word():
    secret_word = random.choice(words)
    return str(secret_word)

def get_guess(previous_guesses):
    player_guess = input("\nGuess a 5 letter word: ").lower()
    while player_guess in previous_guesses:
        player_guess = input("\nYou've already guessed that. Try again: ").lower()
    while len(player_guess) != 5:
        player_guess = input("\nYour guess must be 5 letters. Try again: ").lower()
    

    return str(player_guess)

def evaluate_guess(player_guess, secret_word):
    feedback = []
    for i in range(len(player_guess)):
        if player_guess[i] == secret_word[i]:
            feedback.append("G")
        elif player_guess[i] in secret_word:
             feedback.append("Y")
        else:
            feedback.append("-")
    return  " ".join(feedback)

def display_guess(player_guess, feedback):
    print(f"""\nGuess: {player_guess}
Feedback: {feedback}""")

def has_won(player_guess, secret_word):
    if player_guess == secret_word:
        has_won = True
    else:
        has_won = False
    return has_won
