import random 

answers = ["Yes", "No", "Maybe", "Dont know", "Mmmm...."]
play = input("Do you wanna play this game y/n")

while play != "n":
    question = input("Ask me something")
    
    r = random.choice(answers)
    print(r)
        
    play = input("Do you wanna play this game y/n")
  
print("end game")