import random
number = random.randint(1,101)
count = 0
mode = ""
max_guesses = 0
mode_level = ""
while mode != "E" and mode != "H" and mode != "M" and mode != "R":
    mode = input("Which mode do you want: E for easy, M for medium, H for hard or R for really hard ").upper()
    if mode == "E":
        max_guesses = 19
        mode_level = "EASY"
    elif mode == "M":
        max_guesses = 11
        mode_level = "MEDIUM"
    elif mode == "H":
        max_guesses = 7
        mode_level = "HARD"
    else:
        max_guesses = 4
        mode_level = "Extremely HARD"
print(f"{mode_level} mode")
print(f"you have {max_guesses + 1} guesses")
guess = int(input("guess the number between 1 and 100: "))
while guess != number and count < max_guesses:
    count += 1
    if guess < number:
        guess = int(input("Too low try again: "))

    else:
        guess = int(input("Too high, try again: "))
if guess == number:
    print(f"You got it in {count + 1} guesses on {mode_level}!")
else:
    print(f"you ran out of guesses on {mode_level}!")
    print(f"the answer was {number}")
