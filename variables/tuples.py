# tuple = collection which is ordered and UNCHANGEABLE
# used to group together related data

student = ("Bro",21,"Male")

print(student.count("Bro")) # counts how many times "Bro" appears
print(student.index("Male")) # finds the index of Male

for i in student:
    print(i)

if "Bro" in student:
    print("Bro is here!")