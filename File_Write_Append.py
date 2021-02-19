# no need to close a file after reading

with open('File_Data.txt') as my_file:
    print(my_file.readlines())

# Mode='w' will create a new text file (if not exist) and write text to it
with open('New_File.txt', mode='w') as my_file:
    text = my_file.write('hello there!!')

# mode='a' Append writes in the end of the file
with open('New_File.txt', mode='a') as my_file:
    text = my_file.write("Welcome")


with open('New_File.txt', mode='r') as my_file:
    print(my_file.readlines())
