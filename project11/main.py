import assets
import random


def print_scoreboard(user_hand, comp_hand, user_score, comp_score, game_state):
    if game_state == "continue":
        print(f"Your cards: {user_hand}, curent score: {user_score}")
        print(f"Computers first card: {comp_hand[0]}")
    if game_state == "end":    
        print(f"Your final hand: {user_hand}, final score: {user_score}")
        print(f"Computers final hand: {comp_hand}, final score: {comp_score}")


def draw_card(deck,user_score,comp_score,cards_to_draw,person_to_draw):
    
    if person_to_draw == "user":
        if cards_to_draw == 2:
            return [deck.pop(),deck.pop()]

        elif (user_score // 2) <= 10:
            return deck.pop()

        elif (user_score // 2) > 10:    

            card = deck.pop()

            if card == 11:
                card = 1
                return card
            else:
                return card
    if person_to_draw == "comp":
        if cards_to_draw == 2:
            return [deck.pop(),deck.pop()]

        elif (comp_score // 2) <= 10:
            return deck.pop()

        elif (comp_score // 2) > 10:    

            card = deck.pop()

            if card == 11:
                card = 1
                return card
            else:
                return card
        

def compare_score(user_score,comp_score):

    if comp_score > user_score or user_score > 21:
        return "You Lose bozo!"
    elif user_score > comp_score or comp_score > 21:
        return "You Win!"
    else:
        return "draw"


def start_game():
    print(assets.BLACKJACKLOGO) 
    deck = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
    random.shuffle(deck)
    user_score = 0
    comp_score = 0
    user_hand = []
    comp_hand = []
    user_hand += draw_card(deck,user_score,comp_score,cards_to_draw=2,person_to_draw="user")
    comp_hand += draw_card(deck,user_score,comp_score,cards_to_draw=2,person_to_draw="comp")
    user_score = sum(user_hand)
    comp_score = sum(comp_hand)
    winner = ""
    
    if comp_score == 21 or user_score == 21:
        winner = compare_score(user_score,comp_score)
        return winner 
    
    while (user_score <= 21 and comp_score <= 21):

        print_scoreboard(user_hand, comp_hand, user_score, comp_score, "continue")

        draw = input("Enter 'y' to draw another card, type 'n' to pass: ")
       
        if (draw == 'n' and comp_score < 17):
            comp_hand += draw_card(deck,user_score,comp_score,cards_to_draw=1,person_to_draw="comp")
            comp_score = sum(comp_hand)
       
        elif (draw == 'n' and comp_score >= 17):
            winner = compare_score(user_score,comp_score) 
            break   

        elif (draw == 'y' and comp_score < 17):
            user_hand += draw_card(deck,user_score,comp_score,cards_to_draw=1,person_to_draw="user")
            comp_hand  += draw_card(deck,user_score,comp_score,cards_to_draw=1,person_to_draw="comp")
            user_score = sum(user_hand)
            comp_score = sum(comp_hand)
            continue
        elif (draw == 'y' and comp_score >= 17):
            user_hand += draw_card(deck,user_score,comp_score,cards_to_draw=1,person_to_draw="user")
            user_score = sum(user_hand)
            continue
    
    print_scoreboard(user_hand, comp_hand, user_score, comp_score, "end")
    winner = compare_score(user_score,comp_score)
    return winner


def main():

    RoundStringChange = "a"

    while True:
        try:                       
            playGame = input(f"Do you want to play {RoundStringChange} game of blackajck(Yes or no):")
            if (playGame.lower() == "no" or playGame.lower().startswith('n')):
                break
            elif(playGame.lower() == "yes" or playGame.lower().startswith('y')):
                result = start_game()
                print(result)
                RoundStringChange = "another"    
        except:
            print("Invalid Input")


if __name__ == "__main__":
    main()