
text = "Hi! Did you know that if you write a file using this method that has the same name as another file, the file will be overwritten?"
with open('fileTestingTwo.txt', 'w') as file: # Opens a non-existing file in write mode. If you open it like how you would read it, you get an error
    file.write(text)
with open('fileTestingTwo.txt' 'a') as file: # opens the now existing file in append mode, adding whatever you write to the end
    file.write(" This text has been appended to the file after its creation.")

# You can use other parameters too. "r+" will allow you to read and write. It's useful

# For more info, search up "file open modes python3"