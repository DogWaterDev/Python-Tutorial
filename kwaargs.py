# **kwaargs = oarameter that will pack all argument into a dictionary
        #    useful so that a function can accept a varying amount of keyword arguments

# identical to args but instead of accepting positional args and packing them into a tuple
# it accepts keyword args and packs them into a dictionary

# def hello(first, last):
#     print("Hello " + first + " " + last)
#
# hello(first="Bro", last="Dude", middle="G")

# This would return an error because there are more keyword args than the function supports

def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last']) # access the arguments with the key (parameter name)\
    # It's just a dictionary, which if you need more info on has already been uploaded to the repo


hello(first="Bro", last="Dude", middle="G") # This will work even though there is an extra argument that we don't need

def hello2(**kwargs):
    print("Hello,", end=" ") # This will stop the print from creating a newline after printing the text
    for key,value in kwargs.items():
        print(value,end=" ")


hello2(title="Archduke", first="Franz", last="Ferdinand", middle="Karl Ludwig Joseph Maria")
# Franz Ferdinand sure has a long name

# Like *args, you can rename **kwargs

def new(**cheeseburger):
     for key,value in cheeseburger.items():
       print(value, end=" ")

new(first="Nein")