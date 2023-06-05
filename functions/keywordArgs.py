# keyword argument = an argument preceded by an identified when passed to a function
#                    The order of the arguments doesn't matter, unlike positional arguments
#                    Python knows the names of the arguments that our function receives

# Positional arguments example

def hello(first, middle, last):
    print("Hello "+first+" "+middle+" "+last)


hello("Quandale", "Pringle", "Dingle")
hello("Pringle", "Quandale", "Dingle") # the order matters in positional arguments
# Keyword Argument example

hello(last="Dingle", first="Quandale", middle="Dingle") # Here, the order doesn't matter
# The identifiers such as first, last, middle are the parameters that were defined in the function declaration
