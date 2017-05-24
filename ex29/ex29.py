#Small Calculator app to try out if statements in python

def add(int1, int2):
    return int1 + int2

def subtract(int1, int2):
    return int1 - int2

def divide(int1, int2):
    return int1 / int2

def multiply(int1, int2):
    return int1 * int2

print """____________CALCULATOR_____________
Available Operations:
1> Addition
2> Subtraction
3> Division
4> Multiplication
Enter two numbers and select the appropriate number for the operation."""

a = float(raw_input("Enter the first number: "))
b = float(raw_input("Enter the second number: "))
operation = int(raw_input("Enter the operation number: "))

if operation == 1:
    print add(a,b)
    
if operation == 2:
    print subtract(a,b)

if operation == 3:
    print divide(a,b)

if operation == 4:
    print multiply(a, b)

