# function to print name given number of times
def print_name(name, number):
    for item in range(0, number):
        print(name)


#main routine
name_ = input("name to print: ")
number_ = int(input("times to print: "))
print(print_name(name_, number_))
