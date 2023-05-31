# if statement = a block of code that will execute if a given condition is true

age = int(input("How old are you?: "))

"""
>= greater than or equal to
<= less than or equal to
== equal to
< less than
> greater than
"""

# ORDER OF YOUR IF STATEMENTS MATTERS
# if they are 18 or over 18
if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0: # this will run if the above if statement is false and this condition is true
    print("You haven't been born yet!")

else: # this will execute if the above if statement is false
    print("You are a child!")