from sys import argv

script, file_name = argv

file = open(file_name)
print file.read()

print("Now enter 2nd file name")
file_name2 = raw_input("> ")
file2 = open(file_name2)
print """Okay...This is your file:::
.
%s
""" %(file2.read())

