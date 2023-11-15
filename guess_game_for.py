import random

secret_number = random.randint(1, 100)

for i in range(3):
    guess = input("Which number i am thinking")
    if secret_number == guess: 
        print("You found it")
    elif secret_number > guess:
        print("My number is greater")
    else:
        print("My number is smaller")