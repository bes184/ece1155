# imports
import random

'''
Question 1: Shift Cipher
'''
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shifttext(plaintext: str, shift: int):
    # the alphabet
    # shift, k
    shiftedalphabet = ALPHABET
    if shift != 0:
        shiftedalphabet = ALPHABET[shift:]+ALPHABET[0:shift-1]
    # encrypt
    plaintext = plaintext.upper()
    ciphertext = ''
    for char in plaintext:
        newchar = shiftedalphabet[ALPHABET.index(char)]
        ciphertext+=newchar
    return ciphertext

def decryptshifttext(ciphertext: str):
    for i in range(len(ALPHABET)):
        tempstring = shifttext(ciphertext, -1*i)
        print(tempstring, i)
    return

'''
Question 2: Random Substitution Cipher
'''
CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=[];,./!@#$%^&*()_+|:<>?'

def randomencoding():
    tempchars = CHARACTERS
    encodedalphabet = ''
    for i in range(len(ALPHABET)):
        index = random.randrange(len(tempchars))
        encodedalphabet+=tempchars[index]
        tempchars = tempchars.replace(tempchars[index], "")
    return encodedalphabet

def randomsubstitution(plaintext: str):
    encodedalphabet = randomencoding()
    plaintext = plaintext.upper()
    ciphertext = ''
    for char in plaintext:
        newchar = encodedalphabet[ALPHABET.index(char)]
        ciphertext+=newchar
    return [ciphertext, encodedalphabet]

def decryptrandomsubstitution(ciphertext: str, encodedalphabet: str):
    ciphertext = ciphertext.upper()
    plaintext = ''
    for char in ciphertext:
        newchar = ALPHABET[encodedalphabet.index(char)]
        plaintext+=newchar
    return plaintext