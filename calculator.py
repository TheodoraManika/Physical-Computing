#Να φτίαζετε ένα πρόγρμμα που θα είναι κουμπιουτεράκι
num1 = int(input("Give firest number"))
num2 = int(input("Give second number"))
symb = input("Give symbol")

# +, -, *, /, %, **

if symb == "+":
    print(num1 + num2)
elif symb == "-":
    print(num1 - num2)
elif symb == "*":
    print(num1 * num2)
elif symb == "/":
    print(num1 / num2)
elif symb == "%":
    print(num1 % num2)
elif symb == "**":
    print(num1 ** num2)
else:
    print("wrong symbol")