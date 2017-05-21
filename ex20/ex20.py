def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def percentage(a, b):
    return (a / b) * 100

print "Hello there!! Please enter any two numbers and I will perform Mathematical operations on it =======> \n"
int1 = float(raw_input("> "))
print "Now enter the second number > \n"
int2 = float(raw_input("> "))

addition = add(int1, int2)
subtraction = subtract(int1, int2)
division = divide(int1, int2)
multiplication = multiply(int1, int2)
percentage = percentage(int1, int2)
print """Okay so lets begin:::
The addition is ==============> %f
The subtraction is ===========> %f
The division is ==============> %f
The multiplication is ========> %f
The percentage is ============> %f """ %(addition, subtraction, division, multiplication, percentage)