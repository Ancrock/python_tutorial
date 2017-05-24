x = 1
y = 2

if x < y:
    print "X is less than y"
    d = int(raw_input("What do you want to do? \n 1. Increment \n2. Decrement \n >"))
    if d == 1:
        x += 1
        print "The new value of x now is %d" %x
    else:
        x -= 1
        print "The new value of x is now %d" %x