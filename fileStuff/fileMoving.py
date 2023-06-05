import os

source = "fileMovingDemo.txt"
destination = ".\\fileMovingDemo\\Demo.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there!") # prevents us from overwriting files
    else:
        os.replace(source, destination) # Switch these two around and disable the overwrite check to undo the file move
        print(source+" was moved successfully")
except FileNotFoundError:
    print(source+ " was not found")


