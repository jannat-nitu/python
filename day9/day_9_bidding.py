import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bid_dictionary = {}
should_continue = False
while not should_continue:
    name = input("Enter your name: ")
    bid_price = int(input("Enter your bid price: "))
    bid_dictionary[name] = bid_price
    others_users = input("if there others bidders,type 'yes' or 'no'\n")

    if others_users == "no":
        highest_bid = 0
        winner = ""
        for bid in bid_dictionary:
            bid_amount = bid_dictionary[bid]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bid

        print(f"winner is {winner}  with {highest_bid}")
        clear()
        should_continue = True

