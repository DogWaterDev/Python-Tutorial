# scope = The region that a variable is recognized in
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Lester" # global scope (available inside & outside functions)

def display_name():
    name = "Chester" # this variable has a local scope (only available in this function)
    # if you try to access it outside the function, you will get a NameError
    print(name)

print(name)
display_name()
# You can have both a global and a local variable of the same name
# if this is the case, the local variable in the function will be used first
# if there is no local, it goes to global scope variable