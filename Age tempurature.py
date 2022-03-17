print("hi")
age = float(input("how old are you: "))
temp = int(input("Enter your temperature: "))
if age <= 2 and temp > 38:
    print("call a doctor")

if temp > 39.5:
    print("you have a high fever")

else:
    print("you are fine")
