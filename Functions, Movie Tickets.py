def main_routine(gift=None):
    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    total_sales =0
    tickets_sold = 0

    ticket_wanted = input("Do you want to sell a ticket? (Y/N): ").upper()
    while ticket_wanted != "N":
        ticket = sell_ticket()

        num_tickets = int(input("How many of these tickets do you want: "))
        confirm = input(f"Confirm purchase of {num_tickets} type {ticket}"
                        f"ticket(s)? (Y/N): ").upper()
        if confirm == "Y":
            price = num_tickets * float(get_price(ticket))
            total_sales += price
            tickets_sold += num_tickets
            if ticket == "A":
                adult_tickets += num_tickets
            elif ticket == "C":
                student_tickets += num_tickets
            elif ticket == "s":
                child_tickets += num_tickets
            else:
                gift_tickets += num_tickets

            ticket_wanted = input("\nDo you want to sell "
                                  "another ticket? (Y/N):").upper()

        print("==============================================")
        print(f"The total tickets sold today was {tickets_sold}\n")
        f"\t{adult_tickets}"; for adults; and \n"
            f"\t{student_tickets}"; for students; and \n"
            f"\t{child_tickets}"; for children; and \n"
            f"\t{gift_tickets}"; for  gift and\n"
        print(f"Sales for the day came to ${total_sales:.2f}")
        print("====================================================")

def sell_tickets():
    ticket_type_ = input("What kind of ticket do you want: \n"
                         "\tA for adult, or\n"
                         "\tS for Student, or\n"
                         "\tC for Children, or\n"
                         "\tG for Gift Cards, or\n"
                         ">> ".upper()
    return ticket_type_


def get_price(type_):
    prices = [["A", 12.5], ["S", 9],["C", 7], ["G", 0]]
    for price in prices:
        if price[0] == type_:
            return price[1]

#main routine
print("**************** FanFare Movies - ticketing system ************\n")
main_routine()
