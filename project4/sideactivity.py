import random


def main():
    friendsList = []
    for i in range(5):
        friendsList.append(f'friend{i+1}')

    randomFriend = round(random.random() * 5)
    print("The bill will be payed by " + friendsList[randomFriend])
               




if __name__ == "__main__":
    main()
