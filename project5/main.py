import random

char_sets = [
    [  # Uppercase A–Z
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ],
    [  # Lowercase a–z
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ],
    [  # Digits 0–9
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ],
    [  # Special characters (trimmed)
        '!', '#', '$', '&', '(', ')','<', '>', '?', '@',
        '[', '\\', ']', '^', '_', '`', '{', '}', '~'
    ]
]

password = []

lenPassword = int(input("How long do you want the password: \n"))
upp = int(input("How many upper case letters you want to include\n")) 
low = int(input("How many lower case letters you want to include\n"))
num = int(input("How many numbers you want to include\n"))
spec = int(input("How many special you want to include\n"))

char_num = (upp,low,num,spec)
char_set_idx = (0,1,2,3)

if ((upp+low+num+spec) != lenPassword):
    exit("Password length and total character count dont match")

itr = 0

for pool,k in zip(char_sets,(upp,low,num,spec)):
    password.extend(random.choices(pool,k=k))

random.shuffle(password)
                    
print(''.join(password))