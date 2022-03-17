def calculate_double(number):
    double = number * 2
    return double

def calculate_half(number):
    half = number / 2
    return half

def calculate_ten_more(number):
    ten_more = number + 10
    return ten_more

# main routine
question = int(input("How much? "))
answer = calculate_double(question)
print(f"Double {question} is {answer}")

answer = calculate_half(question)
print(f"Half {question} is {answer}")

answer = calculate_ten_more(question)
print(f"ten more then {question} is {answer}")
