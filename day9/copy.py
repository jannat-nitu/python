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
print(logo)
bids = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
  highest_bidding = 0
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount > highest_bidding:
      highest_bidding = bid_amount
      winner = bidder
      print(f"The winner is {winner} with a bid of ${highest_bidding}")
while not bidding_finished:
  name = input("what is your name?")
  price = int(input("what is your bid?"))
  bids[name] = price
  should_continue = input("are there any other bidders? type 'yes' or 'no'.")
  if should_continue== "no":
    bidding_finished = True
    find_highest_bidder(bids)

