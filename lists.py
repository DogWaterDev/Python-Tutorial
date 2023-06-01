# list = used to store multiple items (datapoints) within a single variable

italianFood = ["pizza", "pasta", "pesto", ]
# store every value as normal, but within square brackets and separated by commas
print(italianFood)
print("-------")
# In order to access a single value from a list, use an index like with string slicing

# The first value of italianFood would be pizza at index 0

print(italianFood[0]) # this will print pizza
#print(italianFood[3]) # this will give an error because there is no value at index 3

# you can always update the items in a list later on
italianFood[1] = "spaghetti"

print(italianFood[1]) # this will now print spaghetti instead of pasta
print("-------")

for i in italianFood:
    print(i)
print("-------")
# you can add things to the end of a list using listName.append(item)
italianFood.append("tiramisu")
# remove with listName.remove(item)
italianFood.remove("spaghetti")
# pop will remove the last element of a list
italianFood.pop() # will remove tiramisu
italianFood.insert(0, "lasagna") # will put lasagna at the first spot and push everything else back


for i in italianFood:
    print(i)
print("-------")

italianFood.sort() # this will sort alphabetically
for i in italianFood:
    print(i)
print("-------")

italianFood.clear()
for i in italianFood:
    print(i)
print("-------")