import random # gives access to the random module

x = random.randint(1, 6) # Gives a random integer between 1 and 6, inclusive
y = random.random() # Gives a random floating point between 0 and 1
print(x)
print(y)

myList = ["rock", "paper", "scissors"]
z = random.choice(myList) # chooses a random element from myList

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]

random.shuffle("cards")

print("cards")