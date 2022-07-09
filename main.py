from replit import clear
from art import logo

auction = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid amount ${highest_bid}.")

bidding_finished = False

while not bidding_finished:
    clear()
    print(logo)
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    auction[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n" )
    if should_continue.lower() == "no":
        bidding_finished = True
        find_highest_bidder(auction) 