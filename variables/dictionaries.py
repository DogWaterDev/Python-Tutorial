# dictionary = a changeable, unorder collection of unique key:value pairs
#              fast because they use hashing, allows us to access a value quickly

capitals = {"USA":"Washington, D.C.",
            "Russia":"Moscow",
            "India":"New Delhi",
            "China": "Beijing"}

print(capitals["Russia"])
# In order to access a dictionary, you need to use the key not the index because dictionaries don't have indexes
# THIS METHOD IS RISKY. IT CAN FAIL IF YOU ENTER A KEY THAT DOES NOT EXIST, CRASHING THE PROGRAM

# Instead, use dictionary.get(key)
print(capitals.get("Germany")) # this key doesn't exist but doesnt return an error. Instead it gives "None"
print(capitals.keys()) # prints all the keys in the dict (dictionary)
print(capitals.values()) # print all the values in the dict
print(capitals.items()) # prints the entire dictionary

for key,value in capitals.items():
    print(key + """'s Capital is: """ + value)
print("\n\n\n") #\n adds an empty line
# Add values to dictionaries with dictionary.update({key:value})
capitals.update({"Germany": "Berlin"})
for key,value in capitals.items():
    print(key + """'s Capital is: """ + value)
print("\n\n\n")
capitals.update({"USA":"Las Vegas"})
for key,value in capitals.items():
    print(key + """'s Capital is: """ + value)
print("\n\n\n")
capitals.pop("China") #removes china from dictionary
for key,value in capitals.items():
    print(key + """'s Capital is: """ + value)
print("\n\n\n")
capitals.clear() # this clears all values in a dictionary