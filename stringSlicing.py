"""
 slicing = creating a substring by extracting elements from another string
start:stop:step
start is inclusive, stop is exclusive
counting starts at index 0
step is optional, how much you are increasing index from start to stop.
by default it is 1
"""

name = "Bro Code"
#       012345678

first_name = name[0:3]
print(first_name)
last_name = name[4:8]
print(last_name)
funky_name = name[0:8:3]
funky_name = name[::3] # python assumes that if the first two colons are empty,
#they are first and last
# in this case that means lines 17 and 18 are the same
print(funky_name)

# you can reverse a name like this
reversed_name = name[::-1]
print(reversed_name)
# ---------------------------------------------------------
# Slice Function
# ---------------------------------------------------------

print("""---------------------------------------------------------
Slice Function
---------------------------------------------------------""")

# slice function creates a slice object
website1 = "http://google.com"
website2 = "http://sony.com"
#positive indexes count forward from start, negative indexes count backwards from end
slice = slice(7, -4) # this will isolate website name from all URLs
print(website1[slice])
print(website2[slice])