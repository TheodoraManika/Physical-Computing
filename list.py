import random

# Πώς ορίζουμε μία λίστα
favorite_num = [7, 4, 12, 19, 1, 2034, 22]
names = ["alex", "konsta", "elena", "marinos", "mario", "jim", "theodora"]

# Πώς εκτυπώνω ένα συγκεκριμένο 
print(names[4])

#Εκτυπώνουμε όλα τα στοιχεία μίας λίστας
for i in range(7): 
    print("the favorite number of ", names[i], " is ", favorite_num[i])

#Εκτυπώνουμε όλα τα στοιχεία μίας λίστας ανάποδα
for i in range(7): 
    print("the favorite number of ", names[6 - i], " is ", favorite_num[6 - i])

# Αλλάζουμε μία τιμή στη λίστα
names[6] = "violetta"
print(names)

# Αλλάζουμε πολλές τιμές στη λίστα
for i in range(7): 
    favorite_num[i] = int(input("update your number"))

print(favorite_num)

# Προσθέτουμε ένα στοιχείο στις λίστες
names.append("elli")
favorite_num.append(88)

print(names)
print(favorite_num)

# Διαγράφουμε ένα στοιχείο από κάθε λίστα
del names[6]
del favorite_num[6]

print(names)
print(favorite_num)

# Διαλέγουμε ένα στοιχείο τυχαία
winner = random.choice(names)
print(winner)