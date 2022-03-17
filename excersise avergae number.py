repeat_amount = int(input("how many numbers to be averaged? "))
count = 0
total = 0
while count < repeat_amount:
    count += 1
    number = int(input(f"Enter number {count}"))
    total += number
print(f"Total is {total}")
print(f"Average is {total / repeat_amount}")
