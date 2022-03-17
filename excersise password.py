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

