import random
import questions
import os

def play_game():
    
    rand_person_list = random.choices(questions.data,k=2)
    while True:
        first_question = f"{rand_person_list[0]["name"]},is a {rand_person_list[0]["profession"]} from {rand_person_list[0]["country"]}"
        second_question = f"{rand_person_list[1]["name"]},is a {rand_person_list[1]["profession"]} from {rand_person_list[1]["country"]}" 
        
        print(first_question)
        
        print("\nVS\n")
        
        print(second_question)
        
        user_guess = int(input("Which person do you think has more followers(1 or 2):\n"))

        other_index = 1 if user_guess == 1 else 0
        
        if (rand_person_list[user_guess-1]["followers"] > rand_person_list[other_index]["followers"]):
            print("You won")
            rand_person_list[other_index] = random.choice(questions.data)
            os.system("cls")
        else:
            os.system("cls")
            print("You lose")
            break
        


def main():
    print("Welcome to Higher lower , the game")
    play_game()


if __name__ == "__main__":
    main()