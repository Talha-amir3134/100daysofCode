import assets
import random
#inital move
    #print game state
        #reveal only first card of computer
    #user input 
    #evalute game state
        #show second computer card 
            #if comp < 17 -> hit
            #if comp >= 17 but comp < user --> comp loses

def allocate_cards():
    ...

def print_game_state():
    ...


def start_game():
    print(assets.BLACKJACKLOGO) #ignore
    deck = [2,3,4,5,6,7,8,9,10,10,10,1,11]
    userHand  = []
    compHand = []
    while True:
        ...


def main():

    RoundStringChange = "a"

    while True:
        try:                       
            playGame = input(f"Do you want to play {RoundStringChange} game of blackajck(Yes or no):")
            if (playGame.lower() == "no" or playGame.lower().startswith('n')):
                break
            elif(playGame.lower() == "yes" or playGame.lower().startswith('y')):
                start_game()
                RoundStringChange = "another"    
        except:
            print("Invalid Input")


if __name__ == "__main__":
    main()