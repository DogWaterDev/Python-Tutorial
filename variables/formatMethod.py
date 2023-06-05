# str.format() = an optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the " + item + "\n")

print("The {} jumped over the {}\n".format(animal, item)) # The curly braces are format fields (placeholders)
# the order matters
# First format field to first value given to the format() function

print("The {0} jumped over the {1}\n".format(animal, item)) # positional argument
#                                          indx 0  indx 1
print("The {1} jumped over the {1}\n".format(animal, item))

print("The {animal} jumped over the {item}\n".format(animal="cow", item="moon")) # keyword argument

print("The {animal} jumped over the {animal}\n".format(animal="cow"))


text = "The {} jumped over the {}\n"

print(text.format(animal, item))

# You can add padding to the text
name = "Carmen"
print("Hello, my name is {:10}. Nice to meet you.".format(name)) # 10 spaces of padding from right side
print("Hello, my name is {:<10}. Nice to meet you.".format(name)) # Left align with padding
print("Hello, my name is {:>10}. Nice to meet you.".format(name))  # Right align with padding
print("Hello, my name is {:^10}. Nice to meet you.".format(name))  # Center align with padding
print("Hello, my name is {name:10}. Nice to meet you, {title}.".format(name=name,title="sir"))
# that's how you add padding and align text

pi = 3.14159
n = 3200
print("Pi is approximately {:.2f}".format(n)) # f is for floating point number. This will display only 2 digits after decimal point
# It will also round your number, so you should keep that in mind for precision
print("The number is {:,}".format(n)) # This will add a comma to all thousandths places
print("The number is {:b} in binary".format(n)) # This will display a binary representation of your number, but only for ints
print("The number is {:o} in octal".format(n)) # You can make octal numbers
print("The number is {:X} in hex".format(n)) # Hexadecimal, too!
print("The number is {:e}".format(n)) # Lastly, you can use scientific notation