#Ceasar Cipher

def encode(char,shiftVal):
    ascii_char = ord(char)
    shiftVal %= 26
    if char >= 'a' and char <= 'z':
        ascii_char = (ascii_char - ord('a') + shiftVal) % 26 + ord('a')
    elif char >= 'A' and char <= 'Z':
        ascii_char = (ascii_char - ord('A') + shiftVal) % 26 + ord('A')    
    
    enc_char = chr(ascii_char)

    return enc_char

def decode(char,shiftVal):
    encode(char=char,shiftVal=-shiftVal)
    

def ceasarCipher(mode):
    if(mode == "encode"):
        text = input("Input the text you want to encode(no space):\n")
        shiftVal = int(input("What shift value do you want to use(numeric):\n"))
        enc_text = ''
        for char in text:
            enc_text += encode(char,shiftVal)
        print(enc_text)
    elif(mode == "decode"):
        text = input("Input the text you want to decode(no space):\n")
        shiftVal = int(input("What shift value do you want to use(numeric):\n"))
        dec_text = ''
        for char in text:
            dec_text += decode(char,shiftVal)
        print(dec_text)    

def main():
    
    while True:
        print("Ceasar Cipher!!!")
        mode = input("do you want to encode or decode:\n")
        ceasarCipher(mode=mode)
        endProgram = input("Type 'yes' if you want to go again. Otherwise 'no': \n")
        if(endProgram == "no"):
            break


if __name__ == "__main__":
    main()    