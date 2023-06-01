# set = collection whic is unordered and unindexed. NO duplicate values

utensils = {"spoon", "fork", "knife"}
dishes = {"bowl", "plate", "fork", "cup"}
# they're faster to see if a value is in the set than a list would be or a tuple because they're unordered
for i in utensils:
    print(i)
    print("---------")
utensils.add("napkin")


for i in utensils:
    print(i)
print("---------")
utensils.remove("fork")
for i in utensils:
    print(i)
print("---------")
utensils.clear()
for i in utensils:
    print(i)
print("---------")
utensils = {"spoon", "fork", "knife"}
utensils.update(dishes) # this will add all elements within dishes to utensils
for i in utensils:
    print(i)
print("---------")
dinner_table = utensils.union(dishes)
for i in dinner_table:
    print(i)
print("---------")
utensils = {"spoon", "fork", "knife"}
# set.update() just changes the set
# set.union() makes a whole new set and returns that

utensils = {"spoon", "fork", "knife"}
dishes = {"bowl", "plate", "fork", "cup"}

print(utensils.difference(dishes)) # what does utensils have that dishes doesn't?
print("---------")
print(utensils.intersection(dishes)) # what does utensils have in common with dishes?
print("---------")