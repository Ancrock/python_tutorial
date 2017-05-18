from sys import argv

script, file_name = argv
file = open(file_name, 'rb+')
print """The file has following contents:
%s """ %(file.read())
print "Please enter the text that you want to enter in the file: "
line1 = raw_input();
print "Please enter another lined that you want to enter in the file: "
line2 = raw_input();
print "Please enter another that you want to enter in the file: "
line3 = raw_input();
file.truncate()
file.write(line1)
file.write("\n")
file.write(line2)
file.write("\n")
file.write(line3)
print "Your file has been successfully overwritten."
file.close()

