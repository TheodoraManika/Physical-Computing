#Γράψτε έναν κώδικα που αφού του δίνεις το όνομα σου να ελέγχει ένα σε ξέρει 
#Εάν ναι να εμφανίζει I know you και το ονόμα 
#Εάν όχι να εμφανίζε Who are you? και το όνομα

my_name = "theodora"
name = input("whats your name")

if my_name == name:
    print("hi there", my_name)
else:
    print("who are you?", name)