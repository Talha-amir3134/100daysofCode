#auction app
import os

def main():
    print("Welcome to the auction program!")
    members_dictionary = {}
    while True:
        name = input("What is your name: ")
        bid = int(input("what is your bid: $"))
        members_dictionary[name] = bid
        bidAgain = input("is there another bidder(yes or no): ")
        os.system("cls")
        if (bidAgain == "no"):
            break

    maxBid = 0        
    winnerBid = ""
    for name in members_dictionary:
        if(maxBid < members_dictionary[name]):
            maxBid = members_dictionary[name]
            winnerBid = name

    print(f"Winner of the auction is {winnerBid} with the a whopping ${maxBid}")    


if __name__ == "__main__":
    main()    