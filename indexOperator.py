# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "who Code"

#if(name[0].islower()):
    #name = name.capitalize()

first_name = name[:3].upper() # fetches the first 3 characters, "who" and makes it all uppercase
last_name = name[3:].lower() # fetches all the characters after the third one and makes it all lowercase
last_character = name[-1] # you can access the last character using negative indexing
# normal indexing goes left to right the larger the number, negative indexing goes right to left the larger the number
print(first_name)
print(last_name)