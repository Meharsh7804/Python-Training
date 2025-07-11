# r+ mode is used to open the file for both reading and writing. The file pointer is placed at the beginning of the file.
# If the file does not exist, it raises an error.

# w+ mode is used to open the file for both writing and reading. If the file does not exist, it creates a new file.
# If the file exists, it truncates the file to zero length before writing.

# a+ mode is used to open the file for both appending and reading. The file pointer is placed at the end of the file.
# If the file does not exist, it creates a new file.