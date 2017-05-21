def custom_print(arg1):
    print """ So this is a custom print _______
    =====> %s <=====""" % arg1
    
def unlim_args(*args):
    print(args)
    
def print_nothin():
    print "______________________ I GOT NOTHIN ELSE!!_______________________"
    
def add(a, b):
    print a+b
    
custom_print("MY NAME IS AMIT")
custom_print("This looks cool")
unlim_args("Cat", "Dog", "Horse")
unlim_args("Bull")
add(2, 5)
print_nothin()