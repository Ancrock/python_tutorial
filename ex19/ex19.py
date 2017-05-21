from sys import argv

script, file_name = argv
file = open(file_name)

def print_all(f):
    print f.read()

def print_one_line(f):
    print f.readline()

print "Okay, So the file you selected is %s" %file_name

print """So, the first line of the file contains this ::::>\n"""
print_one_line(file)
print "Now all the contents of the file are as follows ::::>\n"
print_all(file)
