from random import randint

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def generate_otp(sheets, length):
    #it creates the one-time pads 
    for sheet in range(sheets):
        with open("otp" + str(sheet) + ".txt","w") as f:
            for i in range(length):
                f.write(str(randint(0,26))+"\n")

#generate_otp(5,100)
#Calling the above function to generate 5 sheets with 100 characters each

def load_sheet(filename):
    #it reads the one-time pads and saves them into a list
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents

#sheet = load_sheet('otp0.txt')
#print(sheet)

def get_plaintext():
    #it gets the message from the user and changes all of the letters to lowercase
    plain_text = input('Enter your message: ')
    return plain_text.lower()

def load_file(filename):
    #it reads the file given from the user and saves its contents
    with open(filename, "r") as f:
        contents = f.read()
    return contents

def save_file(filename, data):
    #it writes the encryped message into a file
    with open(filename, 'w') as f:
        f.write(data)

def encrypt(plaintext, sheet):
    #it encrypts the message
    ciphertext = ''
    for position, character in enumerate(plaintext):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
            ciphertext += ALPHABET[encrypted]
    return ciphertext

#sheet = load_sheet('otp0.txt')
#encrypt('This is a secret message.', sheet)

def decrypt(ciphertext, sheet):
    #it decrypts the message
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in ALPHABET:
            plaintext += character
        else:
            decrypted = (ALPHABET.index(character) - int(sheet[position])) % 26
            plaintext += ALPHABET[decrypted]
    return plaintext

#decrypt(ciphertext, sheet)

#MENU
def menu():
    #menu for the user to choose what they want to do
    choices = ['1', '2', '3', '4']
    choice = '0'
    while True:
        while choice not in choices:
            print('MENU')
            print('____')
            print('1. Generate one-time pads')
            print('2. Encrypt a message')
            print('3. Decrypt a message')
            print('4. Quit the program')
            print('____')
            choice = input('Enter a number: ')
            if choice == '1':
                sheets = int(input('How many one-time pads would you like to generate? '))
                length = int(input('What will be your maximum message length? '))
                generate_otp(sheets, length)
            elif choice == '2':
                filename = input('Enter the filename of the OTP you want to use: ')
                sheet = load_sheet(filename)
                plaintext = get_plaintext()
                ciphertext = encrypt(plaintext, sheet)
                filename = input('Enter the name of the encrypted file: ')
                save_file(filename, ciphertext)
            elif choice == '3':
                filename = input('Enter the filename of the OTP you want to use: ')
                sheet = load_sheet(filename)
                filename = input('Enter the name of the file to be decrypted: ')
                ciphertext = load_file(filename)
                plaintext = decrypt(ciphertext, sheet)
                print('The message reads:')
                print('')
                print(plaintext)
            elif choice == '4':
                exit()
            choice = '0'
            print()

menu()


