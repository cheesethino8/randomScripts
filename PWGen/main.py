import random
import string
from random import randrange

pwLength = input("Enter password length:")
pwLength = int(pwLength)

digChoice = input("Digits? (Y/N)")
letChoice = input("Letters? (Y/N)")
symChoice = input("Symbols? (Y/N)")

#print(digChoice + letChoice + symChoice)

digChoice = "y" in digChoice or "Y" in digChoice
letChoice = "y" in letChoice or "Y" in letChoice
symChoice = "y" in symChoice or "Y" in symChoice

#print(str(digChoice) + str(letChoice) + str(symChoice))

global n
n = pwLength
global passwd
passwd = ""

def generatePassword(n):
    global passwd, result

    if (n <= 0):
        print(passwd)
        result = 0
        return result
    rndNum = random.randint(0,2)

    if (digChoice == True and rndNum == 0):
        digPasswd = "".join({random.choice(string.digits)})
        passwd = passwd + digPasswd
        n = n - 1
        if (n == 0):
            print(passwd)
            return 0

    if (letChoice == True and rndNum == 1):
        letPasswd = "".join({random.choice(string.ascii_letters)})
        passwd = passwd + letPasswd
        n = n - 1
        if (n == 0):
            print(passwd)
            return 0

    if (symChoice == True and rndNum == 2):
        symPasswd = "".join({random.choice(string.punctuation)})
        passwd = passwd + symPasswd
        n = n - 1
        if (n == 0):
            print(passwd)
            return 0

    generatePassword(n)

print(passwd)
generatePassword(n)