import random

def play_game(mode):
    
    num_guess = 0
   
    if mode == "easy":
        num_guess = 10
    else:
        num_guess = 5    
    
    number_to_guess = random.randint(0,100)

    while num_guess > 0:
        
        print(f"Number of guesses remaining is {num_guess}")
        user_guess = int(input("Enter your guess: \n"))
        
        if user_guess == number_to_guess:
            print("You guessed correctly!!!")
            break
        elif user_guess > number_to_guess:
            print("Oh you guessed too high!!!")
        else:
            print("Your guess is too low")

        num_guess -= 1


def main():
    print("Welcome to the number guessing game!")
    game_mode = input("Do you want to play the game on easy or hard mode: \n")
    play_game(mode=game_mode)

if __name__ == "__main__":
    main()    