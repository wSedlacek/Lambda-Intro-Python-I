"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open('./src/foo.txt') as f:
    print(f.read())
    f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open('./src/bar.txt', 'w+') as f:
    line1 = input("Line 1:")
    line2 = input("Line 2:")
    line3 = input("Line 3:")
    f.write(f'{line1}\n{line2}\n{line3}\n')
    f.close()

with open('./src/bar.txt') as f:
    print(f.read())
    f.close()
