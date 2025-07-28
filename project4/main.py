import random

def printRock():
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

        """)

def printPaper():
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

          """)

def printScissor():
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          
    """)

def hand(choice):
    if choice == 0:
        printRock()
    elif choice == 1:
        printPaper()
    elif choice == 2:
        printScissor()
    else:
        print("wrong choice")     
        exit

def evaluationFunc(userChoice, compChoice):
    if ((userChoice == 0 and compChoice == 1) or (userChoice == 1 and compChoice == 2)or (userChoice == 2 and compChoice == 0)):
        print("Computer won!")
    elif (userChoice == compChoice):
        print("Its a draw") 
    else:
        print("User won!")       


def main():
    userChoice = int(input("Enter your move (0: rock, 1: paper, 2:scissor):\n"))
    hand(userChoice)
    print("Computer chose: ")
    compChoice = random.randint(0,2)
    hand(compChoice)
    evaluationFunc(userChoice=userChoice, compChoice= compChoice)

if __name__ == "__main__":
    main()    
