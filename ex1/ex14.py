from sys import argv

script, name = argv
prompt = "> "
print "What is your age ?"
age = raw_input(prompt)
print "And how do you like your chicken? "
chicken = raw_input(prompt)
print """Okay %s, So your age is %s
and you like your chicken %s""" %(name, age, chicken)
