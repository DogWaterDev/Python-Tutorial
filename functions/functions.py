# function = a block of code that is executed only when it is called on. can be used multiple times while only being written once


# FUNCTIONS ARE NOT LIMITED TO ONE LINE. IT'S AN ENTIRE BLOCK OF CODE

def ageDetector():
    age = int(input("How old are you?: ")) # asks how old the user is
    print(age)

# i can call this function as many times as I want to

ageDetector()
print("Here we go again! \n") #\n adds a newline
ageDetector()

def helloWorld(x): # this is the declaration for a function. def functionName(parameters):
    print("Hello World! " * x)
    # your code in the function needs to be indented

helloWorld(3) # to call a function, write the name of the function and the parentheses.
# if the function has any parameters, they will be written down in the parentheses for declaration and when called on
# In this example, 3 will replace x, so the code inside the function will be equivalent to this:
# print("Hello World!" * 3)


# Like normal input, you can also just send variables as a parameter

def iTakeVariableInputs(name):
    print("Hi there, " + name)

myName = "Joe Mama"

iTakeVariableInputs(myName)
# you can have more than one value (parameter) in a function

def twoValues(first_name, last_name):
    print("Hello, " + first_name)
    print("Is your last name " + last_name + "?")

# You can only give as many parameters as the function supports
# this wouldn't work:

#iTakeVariableInputs("cheese", "Hi")
# this function call would give an error because it gives two parameters when only one is supported,
# the parameters aren't matching
