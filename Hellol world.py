choice = 0
print('hello world')
print("my name is Windows")
print("what is yours?")
first_name = input("Enter your first name: ")
print("that's a nice name")
last_name = input("and now your last name")
name = (first_name + last_name)
age = input("how old are you: ")
print("wow that's old")
print(f"so {name}. What would you like to do")
while choice < 5:
    choice = int(input("press 1 to enter your bank, 2 to average your number, 3 to find out medical information, 4 to find what discounts you are eligible for"))
    password = "pineapple"
attempt_amount = 2
looping = "true"
password_attempt = input("enter password: ")
while looping == "true":
    if attempt_amount == 0:
        exit("Access denied")
    else:
        password_attempt = input("Enter password: ")
        if password_attempt == password:
            print("Granted")
        elif password_attempt != password:
            attempt_amount = attempt_amount - 1
print("Access granted")
