avergae_fun = ""
avergae_active = ""
number_of_ages = ""
number_of_ages_active = ""
name = ""
# main routine
input_1 = 0
input_2 = 0
total_1 = 0
total_2 = 0
age_1 = 0
age_2 = 0
while name.upper() != "X":
    bad_answer = False
    if input_1 > 0:
        print(total_1 / input_1)
    name = input("Please enter the child's name or type X to exit: ")
    if name.upper() == "X":
        if age_1 > 0:
            print(f"The average age for the Fun in the sun program is {total_1 / input_1} and ")
        if age_2 > 0:
            print(f"the average age for the active kids program is {total_2 / input_2}")
    else:
        option = input("Which holiday program would you like? press 1 for fun is the sun"
                       "and press 2 for active kids: ")
        if option == "1":
            try:
                age_1 = int(input("Enter the child's age in numbers: "))
            except ValueError:
                print("Invalid answer")
                bad_answer = True
                age_1 = 0
            if bad_answer is False:
                input_1 = input_1 + 1
                total_1 = total_1 + age_1

        elif option == "2":
            try:
                age_2 = int(input("Enter the child's age in numbers: "))
            except ValueError:
                print("Invalid answer")
                bad_answer = True
            if bad_answer is False:
                input_2 = input_2 + 1
                total_1 = total_1 + age_2
        else:
            print("you need to use the numbers 1 or 2 to select an option")
