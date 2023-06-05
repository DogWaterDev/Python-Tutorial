import os # allows us to access the operating system the user is using
# Included in standard python library

# In order to do this, you need to have a file. For convenience, I am placing this file on my desktop
# In the file path, "UserName" is the account/folder name

# Please note that this is the path on Windows. It will be different on MacOS, Linux, and probably every operating system

paths = ["C:\\Users\\UserName\\OneDrive\\Desktop\\fileTesting.txt", "C:\\Users\\UserName\\OneDrive\\Desktop\\testFolder"] # You will need to use double backslash because a single backslash
# is associated with other string manipulation stuff like \n, adding a newline

for path in paths: # cycles through the paths in the list and checks them
    print("Now checking " + path)
    if os.path.exists(path):
        print("That location exists!")
        if os.path.isfile(path):
            print("That is a file!") # Checks if the location is a file
        elif os.path.isdir(path):
            print("That is a directory!") # Checks if the location is a directory (folder)

    else:
        print("That location does not exist!")

