import random

secret_number = random.randint(1, 100)

guess = input("Which number i am thinking")

if secret_number == guess: 
    print("You found it")
elif secret_number > guess:
    print("My number is greater")
else:
    print("My number is smaller")

# Περιγράψτε τι κάνει ο κώδικας 

# Γίνετε με κάποιο τρόπο να να μαντεύουμε συνεχώς μέχρι να το πετυχούμε;
#Αν ναί πώς;

# Γίνετε με κάποιο τρόπο να να μπορούμε να μαντέψουμε συγκεκριμένες φορές πχ 6;
