# copyfile() = copies contens of a file to a destination

# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file information such as creation and modification time)

import shutil # A module that has these functions and more for file manipulatian


shutil.copyfile('fileTesting.txt', 'fileStuff/copyofFileTesting.txt')  # src.dst ( destination)