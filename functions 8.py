def result(new_price):
    return new_price * 1.15

# Main Routine
new_price_ = float(input("Enter the before GST price: "))
print(f"{result(new_price_):.2f}")



