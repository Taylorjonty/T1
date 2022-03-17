def days_overdue(charge):
    base_charge = 0.5
    daily_charge = 0.8
    max_charge = 30
    fine_ = (days * daily_charge) + base_charge
    if fine_ > max_charge:
        fine_ = max_charge
    else:
        return fine_



days = int(input("Days overdue: "))
print(f" Your fine is {days_overdue(days)}")




