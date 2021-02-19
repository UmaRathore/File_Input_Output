# create a file object and open a file

my_file = open("File_Data.txt")

# Open has idea of cursor which moves at end after performing read()
# To read file from beginning each time read() is performed seek(0) is used

print(my_file.read())
my_file.seek(0)

# function returns a list of all lines in the file.
print(my_file.readlines())

my_file.close()
