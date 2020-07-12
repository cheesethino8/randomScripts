import random
import string
import os

pwLength = input("Enter password length:") #asks user for an int to be used as the length of the password
pwLength = int(pwLength) #converts user input to an integer

digChoice = input("Digits? (Y/N)") #asks if user wants digits in generated passwords
letChoice = input("Letters? (Y/N)") #asks if user wants letters in generated passwords
symChoice = input("Symbols? (Y/N)")#asks if user wants symbols in generated passwords


digChoice = "y" in digChoice or "Y" in digChoice # convert answer to boolean
letChoice = "y" in letChoice or "Y" in letChoice # convert answer to boolean
symChoice = "y" in symChoice or "Y" in symChoice # convert answer to boolean

global n
n = pwLength #set n to equal to pwlength
global passwd
passwd = "" #creates empty variable for passwd

def generatePassword(n): #recrusive function
    global passwd, result

    rndNum = random.randint(0,2) #create random number between 0 & 2, used to randomize password

    if (digChoice == True and rndNum == 0): #checks if numbers are wanted for password
        digPasswd = "".join({random.choice(string.digits)}) #creates a random number
        passwd = passwd + digPasswd #adds previously created number to the end of the password
        n = n - 1 #increment n
        if (n == 0): #if n = 0, then print resulting password & exit
            print(passwd)
            return 0
                #above comments are basically the same for the 2 loops below(letters & symbols)
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

generatePassword(n) #runs recursive function
os.system("pause") #creates a pause so people can actually copy the damn result