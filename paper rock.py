import random
computer_choice = ""
player_choice = ""
rounds = 0
best_out_of_three = 0
computer_points = 0
player_points = 0

#main routine
print("Welcome to Paper, Scissors, Rock"
      "enter your choice")
player_choice = print(input("Type p for Paper, p Scissors or p Rock: "))
computer_choice = random.randint("Paper" or "Scissors" or "Rock")
print(f"You choose {player_choice}, and the computer choose {computer_choice}")

while rounds > best_out_of_three:
    if computer_choice == "p" and player_choice == "r":
        print("One point to Computer")
        computer_points += 1
        rounds += 1

    elif computer_choice == "r" and player_choice == " p":
        print("one point to Player")
        player_points += 1
        rounds += 1

    elif computer_choice == "p" and player_choice == "s ":
        print("one point to Player")
        player_points += 1
        rounds += 1

    elif computer_choice == "s" and player_choice == "p":
       print("one point to Computer")
       player_points += 1
       rounds += 1

    elif computer_choice == "s" and player_choice == "r":
        print("one point to player")
        player_points += 1
        rounds += 1

    elif computer_choice == "r" and player_choice == "s":
        print("one point to player")
        player_points += 1
        rounds +=1

    elif computer_choice == "r" and player_choice == "r":
        print("tie")

    elif computer_choice == "s" and player_choice == "s":
        print("tie")

    elif computer_choice == "p" and player_choice == "p":
        print("tie")

    else:
        print("needs to be a lower case p, r or s")

if computer_points > player_points:
    print("The Computer Wins")

else:
    print("The Player Wins")
