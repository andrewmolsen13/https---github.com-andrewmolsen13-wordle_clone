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

def get_guess():
    player_guess = input("Guess a 5 letter word: ").lower()
    while len(player_guess) != 5:
        player_guess = input("Your guess must be 5 letters. Try again: ")

    return str(player_guess)

guess = get_guess()
word = choose_word()

