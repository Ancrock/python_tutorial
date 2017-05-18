from sys import argv
from os.path import exists

script, file1 = argv
open_file = open(file1)
file_content = open_file.read()
print """Your file contains the following: 
%s""" %(file_content)
write_file = raw_input("Enter the file name that you want to write to: ")
print "writing contents to the file... "
file2 = open(write_file, "w+")
file2.write(file_content)
print "Successfully copied the contents to %s" %write_file
open_file.close()
file2.close()