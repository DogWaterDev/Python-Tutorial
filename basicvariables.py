# variable = a container for a value. Behaves as the value that it contains

# -----------------------------------------------------------------
# String
# -----------------------------------------------------------------
print(""" -----------------------------------------------------------------
 String
 -----------------------------------------------------------------""")
first_name = "Carmen"
last_name = "Winsten"
full_name = first_name + " " + last_name
print("Hello " + full_name)
print(type(first_name))

# -----------------------------------------------------------------
# Integer
# -----------------------------------------------------------------
print(""" -----------------------------------------------------------------
 Integer
 -----------------------------------------------------------------""")
age = 16
age += 1
print("You are " + str(age) + " years old.")
print(type(age))

# -----------------------------------------------------------------
# Float
# -----------------------------------------------------------------
print(""" -----------------------------------------------------------------
 Float
 -----------------------------------------------------------------""")
height = 180.5
print("You are " + str(height) + " cm tall.")
print(type(height))

# -----------------------------------------------------------------
# Boolean
# -----------------------------------------------------------------
print(""" -----------------------------------------------------------------
 Boolean
 -----------------------------------------------------------------""")
humanity = True
print("Are you a human? | " + str(humanity))
print(type(humanity))

# -----------------------------------------------------------------
# Multiple Assignment
# -----------------------------------------------------------------
print(""" -----------------------------------------------------------------
 Multiple Assignment
 -----------------------------------------------------------------""")
# You can turn
John = 5
Joe = 4
Hank = 3
Steve = 2
Carmen = 1
print(str(John) + str(Joe) + str(Hank) + str(Steve) + str(Carmen))
# into
John, Joe, Hank, Steve, Carmen = 5, 4, 3, 2, 1,
print(str(John) + str(Joe) + str(Hank) + str(Steve) + str(Carmen))
# or something like this
Sandy = 30
Spongebob = 30
Squidward = 30
Patrick = 30
# into
Sandy = Spongebob = Squidward = Patrick = 30


# -----------------------------------------------------------------
# String Methods
# -----------------------------------------------------------------
print(""" -----------------------------------------------------------------
 String Methods
 -----------------------------------------------------------------""")
chez = "bruh u good?"
print(len(chez))
print(chez.find("u"))
print(chez.capitalize())
print(chez.upper())
print(chez.lower())
print(chez.isdigit())
print(chez.isalpha()) # Is it only alphabetical letters? Nah there's a space man
print(chez.count("o"))
print(chez.replace("o", "e"))
print(chez*3) # prints the chez variable 3 times

# -----------------------------------------------------------------
# Typecasting
# -----------------------------------------------------------------
print(""" -----------------------------------------------------------------
 Typecasting
 -----------------------------------------------------------------""")
x = 1 #int
y = 2.0 #float
z = "3" #str

print("Before:")
print(x)
print(y)
print(z)

y = int(y)
z = int(z)

print("To Int:")
print(x)
print(y)
print(z)

x = float(x)
y = float(y)
z = float(z)

print("To Float:")
print(x)
print(y)
print(z)