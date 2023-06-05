# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept varying amount of arguments

def add(*args): # The asterisk (*) is more important than then 'args' part. Technically, you can name it anything, as long as it has that *
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# you can cast the args

def add2(*args): # they do the same thing, one is unchangeable tuple, other is changeable list
    sum = 0
    stuff = list(args)
    stuff[0] = 0
    for i in args:
        sum += i
    return sum

print(add2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))