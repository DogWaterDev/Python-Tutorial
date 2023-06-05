
try:  # You should probably use a try block incase the file does not exist so your program doesn't crash
    with open('fileTesting.txt') as file:  # opens fileTesting.txt and calls the opened file "file" within the scope of the with block
        # The file is automatically closed after the code block
        print(file.read())  # prints the contents of the file

except FileNotFoundError:
    print("Sorry, something went wrong.")
