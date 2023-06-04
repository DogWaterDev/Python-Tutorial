# return statement = Functions send Python values/objects back to the claler.
#                    These values/objects are known as the function's return value

# a function can pass some value back to the caller

def multiply(x, y):
    result = x * y
    return result # this will give the result back to the caller

# a faster way to write this function would be

def multiply2(x,y):
    return x * y

# In order to store this result, do this:

answer = multiply(6, 3)
print(answer)
# You can also just use the result like this
print(multiply(12, 3))
