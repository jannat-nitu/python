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
bids = []

import os


def abc():
    flag = True
    while flag:
        name = input("Enter your name : ")
        bid = int(input("Enter your amount : "))
        bidding_function(name, bid)
        check = input("Is there other user wants to bit? Y or N ")
        if check == "Y":

        else:
            flag = False
            max_value()


def max_value():
    highest_value = 0
    highest_name = ""
    for index in range(0, len(bids)):
        if bids[index]["bid"] > highest_value:
            highest_value = bids[index]["bid"]
            highest_name = bids[index]["name"]

    print("Hurrey!!!" + highest_name + "'s bid is " + str(highest_value) + " and He is WIN")

def bidding_function(name, bid):

    new_entry = {}
    new_entry["name"] = name
    new_entry["bid"] = bid

    bids.append(new_entry)


abc()
