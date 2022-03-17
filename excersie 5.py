year = int(input("What is the year you would like to find out about"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("it is a leap year")
        exit()

else:
    print(" it is not leap year")
    exit("goodbye")






