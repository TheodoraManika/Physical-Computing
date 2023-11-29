import random

favorite_num = [7, 4, 12, 19, 1, 2034, 22]
names = ["alex", "konsta", "elena", "marinos", "mario", "jim", "theodora"]

print(names[4])

for i in range(7): 
    print("the favorite number of ", names[i], " is ", favorite_num[i])

for i in range(7): 
    print("the favorite number of ", names[6 - i], " is ", favorite_num[6 - i])

names[6] = "violetta"
print(names)

for i in range(7): 
    favorite_num[i] = int(input("update your number"))

print(favorite_num)

names.append("elli")
favorite_num.append(88)

print(names)
print(favorite_num)

del names[6]
del favorite_num[6]

print(names)
print(favorite_num)

winner = random.choice(names)
print(winner)