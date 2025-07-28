import random
import assets
def find_char(userGuessChar,word):
    posidx = []
    for i in range(len(word)):
        if(userGuessChar == word[i]):
            posidx.append(i)
    return posidx        

def printGameState(hangmanStatus,wordState):
    pad = 25
    lines = assets.HANGMANPICS[hangmanStatus].splitlines()
    wordState = ' '.join(wordState)
    for i,line in enumerate(lines):
        if (i == 4):
            line = line.ljust(pad) + wordState
        print(line)
    print(f"**********{hangmanStatus}/6 number of guess remaining**********")

def main():
    word = random.choice(assets.words)
    gameWon = False
    numGuess = 6
    guessWord = list()
    for i in range(len(word)):
        guessWord += "_"
        
    print(assets.HANGMANLOGO)
    print("\n")    

    print(word)

    charIdxArr = []
    while (numGuess > 0 and gameWon == False):
        userGuessChar = input("Enter your guess(single character):\n")
        charIdxArr = find_char(userGuessChar=userGuessChar,word=word)
        if (len(charIdxArr) == 0):
            numGuess -= 1
            printGameState(numGuess,guessWord)

        else:
            print("Correct Guess! Hangman gets to keep his limb")
            for pos in charIdxArr:
                guessWord[pos] = userGuessChar
            printGameState(numGuess,guessWord)    
            if("_" not in guessWord):
                gameWon = True   

    if(gameWon == True):
        print("You won!")
    else:
        print("You lose")    



    

if __name__ == "__main__":
    main()