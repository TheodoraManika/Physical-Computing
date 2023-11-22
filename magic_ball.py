import random 
#import time 

play = "y"

while play != "n":
    question = input("Ask me something")
    #time.sleep(5)

    answer = random.randint(1, 2)

    if answer == 1:
        print("Oxi")
    else:
        print("Nai")
        
    play = input("Do you wanna play this game y/n")
  
print("end game")  