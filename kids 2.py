fun_list = []
fun_ages = []
active_kids = []
active_ages_ = []
avergae_fun = ""
avergae_active = ""
number_of_ages = ""
number_of_ages_active = ""
name = ""
active_number = 0
fun_number = 0
active_number_ = ""
childs_age_fun = ""

# main routie

while name != "X".upper():
    name = str(input("Please enter the child's name: "))
    if name == "X".upper():

        avergae_active = sum.active_ages_ / active_number
        avergae_fun = sum.childs_age_fun / fun_number

        print(f"The average age for the Fun in the sun program is {avergae_fun} and "
              f"the avergae age for the active kids program is {avergae_active} ")
    else:
        option = input("Which holiday program would you like? press 1 for fun is the sun"
                       " and press 2 for active kids: ")
        if option == "1":
            fun_list.append(name)
            childs_age_fun = int(input("Enter the child's age in integers: "))
            fun_number += 1

        elif option == "2":
            active_kids.append(name)
            active_ages_ = int(input("Enter the child's age in intergers: "))
            active_ages.append(active_ages_)
            active_number += 1

        else:
            print("you need to use the intergers 1 or 2")
