# nested function calls = function calls inside of other function calls
#                         inner function calls are resolved first
#                         returned value is used as argument for the next outer function

# num = input("Enter a whole positive number")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a positive number "))))) # This single line of code does what the lines above do
# It's a faster  and smaller way of writing, but it can get messy fast

# 1, we get the input (innermost layer)
# 2, we convert that input to a float
# 3, we get the absolute value of that float
# 4, we round the number to the nearest whole
# 5, we print the result