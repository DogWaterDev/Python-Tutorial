# module = a file containing python code. May contain functions, classes, etc.
# used in modular programming, which is separating a program into parts.
# Example of module: os, shutil, time, math, etc.
# These are modules made by other people. The ones above are in the standard library, so they come with python
# Other modules you have to install

# Any file that you make can be imported into another program. That's also a module

import myModule as m # You can give a module an alias. I am calling myModule m to make it faster to write

# Access a module by writing the name or alias, then a dot, and the class/function/something else you want to access
# I'm going to say hi to "John Pork"
name = "John Pork"
m.hello(name)

# You can also import modules another way, only importing some things from a module

from anotherModule import anotherOne
anotherOne()
# This lets you access a function or class like it was defined in this file, whilst actually being in a different module

# Instead of specifically naming the part of the module you want, you can use * and Python will automatically convert
# that asterisk into the part(s) of the module you use. So it, specifically gives only what you need

# However, due to organization and overview issues, this is not recommended. Also, you may run into naming issues
# if you use this method in large programs. For small programs, it probably won't be much of an issue

# If you need help or a list of modules, write help("modules")

help("modules")

# This will generate a list of modules and more info on how to get help

# you can also just go the python documentation