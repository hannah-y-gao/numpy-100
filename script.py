from initialise import*
import random

print("Welcome to numpy-100!")

while(True):
    next = input("Would you like another question? (y/n) ")
    if(next=="y"):
        n = random_number = random.randint(1, 100)
        question(n)
        while(True):
            print("Enter your guess, or enter 'h' to get a hint and 'a' to get the answer: ")
            guess = input("")
            if(guess=="h"):
                hint(n)
            elif(guess=="a"):
                answer(n)
                break
            else:
                print("Your guess", guess)
    else:
        break