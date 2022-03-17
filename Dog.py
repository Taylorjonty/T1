def drop_off():
    dogs_name = input("Please Enter The dogs name: ")
    roll.append(dogs_name)

def pick_up():
    dog_name = float(input("Please enter the name of the dog you want to pick up: "))
    if dog_name in roll:
        roll.remove(dog_name)
        print(f"{dog_name} has be removed from the dog roll")
    else:
        print("Sorry, but there is not dog with that name on our list")

def calc_cost(number):
    rate = 22.50
    days = int(input("How many days to charge for: "))
    cost = number * days * rate
    print(f" The cost for {number} of dogs for {days} days is ${cost} ")

def print_roll():
    print("Dog currently staying with DogsRus: ")
    for dog in roll:
        print(f"\t{dog}")
    print()

def end_program():
    print("Goodbye!")

roll = []

print(
    "--------------------------------------------------")
print("Welcome to DogsRus dog sitting service")
print("What would you like to do? Please choose one of the items below")
print(
    "--------------------------------------------------")

choice = 0
while choice !=5:
    print("What do you want to do?")
    print()
    print("1 Drop off a Dog")
    print("2 Pick up a dog")
    print("3 Calculate cost")
    print("4 Print dog roll")
    print("5 Exit the system")
    print()
    print(
    "--------------------------------------------------")

    choice = int(input("Enter your choice (number between 1 and 5):"))
    if choice == 1:
        drop_off()

    elif choice == 2:
        pick_up()

    elif choice == 3:
        calc_cost(len(roll))

    elif choice == 4:
        print_roll()

    elif choice == 5:
        end_program()

    else:
        print("Must be an Interger between 1 and 5")
