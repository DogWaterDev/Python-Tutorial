import time
# a module, like time, is imported into a script. it's something that has been written by somebody else and you can
# use the functions of this module, like math has math.ceil() to round up. ceil() is function from math
# that you can import to use in this script.


# for loop =    a statement that will execute it's block of code a given amount of times
# while loop = unlimited
# for loop = limited

for i  in range(10): # this will execute for every number in a range from 0 to 10 (integers, exclusive), so it will repeat
    print(i)
    # ten times

for i in range(10): # this will count from 1 to 10
    print(i+1)

for i in "Bro Code": # this will spell out every index (character) of Bro Code
    print(i)


for seconds in range(10, 0, -1): # this will start at 10, end at 0, and go down by 1 each step
    print(seconds)
    time.sleep(1) # this will make the code pause for 1 second.
print("Happy New Year!")