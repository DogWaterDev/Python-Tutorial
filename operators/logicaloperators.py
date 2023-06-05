# logical operators (and,or,not) = used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside?: "))

if temp >= 10 and temp <= 30: # checks if the temperature is between 10 and 30 degrees (inclusive)
    print("It's pretty nice outside. Maybe you should go outside.")

elif temp <= 10 and temp >= 0: # checks if temperature is between 0 and 10 degrees, inclusive
    print("It's not too cold. Maybe wear a jacket, but you should still leave the house")
elif temp < 0 or temp > 30: # checks if temperature is less than 0 or greater than 30, exclusive
    print("The temperature is bad today. You should stay inside")

# That was and + or
# Now we have not, which behaves differently

if not(temp >= 0 and temp <= 30): # checks if the temperature is not between 0 and 30, inclusive
    print("Stay inside. The weather's bad.")
# this statement would work the same as:
elif temp < 0 or temp > 30:
    print("Stay inside. The weather's bad.")