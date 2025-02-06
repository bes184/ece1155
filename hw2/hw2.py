# imports
import random

'''
Question 1: Shift Cipher
'''
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shifttext(plaintext: str, shift: int):
    # shifted alphabet based on shift value, k
    shiftedalphabet = ALPHABET
    if shift != 0:
        shiftedalphabet = ALPHABET[shift:]+ALPHABET[0:shift-1]
    # ensure plaintext is uppercase
    plaintext = plaintext.upper()
    # encrypt plaintext using shifted alphabet
    ciphertext = ''
    for char in plaintext:
        newchar = shiftedalphabet[ALPHABET.index(char)]
        ciphertext+=newchar
    return ciphertext

def decryptshifttext(ciphertext: str):
    # display all potential plaintext values depending on size of alphabet
    # (26 total possible shift values)
    for i in range(len(ALPHABET)):
        tempstring = shifttext(ciphertext, -1*i)
        print(tempstring, i)
    return

'''
Question 2: Random Substitution Cipher
'''
CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=[];,./!@#$%^&*()_+|:<>?'

def randomencoding():
    # make a random encoding key from list of characters
    tempchars = CHARACTERS
    encodedalphabet = ''
    for i in range(len(ALPHABET)):
        index = random.randrange(len(tempchars))
        encodedalphabet+=tempchars[index]
        tempchars = tempchars.replace(tempchars[index], "")
    return encodedalphabet

def randomsubstitution(plaintext: str):
    # get random encoding key
    encodedalphabet = randomencoding()
    # ensure plaintext is uppercase
    plaintext = plaintext.upper()
    # encrypt plaintext using encoding key
    ciphertext = ''
    for char in plaintext:
        newchar = encodedalphabet[ALPHABET.index(char)]
        ciphertext+=newchar
    return [ciphertext, encodedalphabet]

def decryptrandomsubstitution(ciphertext: str, encodedalphabet: str):
    # ensure ciphertext is uppercase
    ciphertext = ciphertext.upper()
    # decrypt ciphertext using encoding key
    plaintext = ''
    for char in ciphertext:
        newchar = ALPHABET[encodedalphabet.index(char)]
        plaintext+=newchar
    return plaintext