# expection = events detected during execution that will interup the flow of a program (such as an error)

# n = int(input("Enter a number to divide: "))
# d = int(input("Enter a number to divide by: "))
# result = n/d
# print(result)

# Basic exception handling: Surround the "dangerous" code in a try block

try:
    n = int(input("Enter a number to divide: "))
    d = int(input("Enter a number to divide by: "))
    result = n / d
except ZeroDivisionError: # this will handle the error when someone  tries to divide by 0. Instead of crashing
    # it will execute what happens in this block
    print("Du kannst nicht durch Null teilen, Junge!")
except ValueError as e: # It is standard to define the exception as e to be used in the program
    print(e) # this will print the error
    print("Please only enter numbers.")
except Exception: # It is not good practice to have a single except block to handle all exceptions
    # Standard practice is to have multiple of these blocks to handle specific exceptions and then one big exception block to handle the rest
    print("Something went wrong. Please try again")
else: # If no exception occurs, we print the result
    print(result)
finally: # No matter if there is an error or not, we always execute this code
    print("This will always execute")
