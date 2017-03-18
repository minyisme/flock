# Defines the calculator object and it's functions
class Calculator(object):

    # Like a simple calculator, decimal inputs are excluded
    def add(self, x, y):
        return x + y

    # Like a real calculator, the second number is subtracted from the first
    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    # Like a real calculator, decimal outputs from division are include
    def divide(self, x, y):
        if x:
            return float(x) / y
        else:
            return None



# Automatically tests code above with concrete examples: if time allowed, convert to unit testing
def test_add(x, y):
    calc = Calculator()
    return calc.add(x, y)

print test_add(2, 4)
print test_add(0, 4)
print test_add(2, -4)
# Expect 6, 4, -2

def test_subtract(x, y):
    calc = Calculator()
    return calc.subtract(x, y)

print test_subtract(2, 4)
print test_subtract(2, -4)
# Expect -2, 6

def test_multiply(x, y):
    calc = Calculator()
    return calc.multiply(x, y)

print test_multiply(2, 4)
print test_multiply(0, 4)
print test_multiply(2, -4)
# Expect 8 , 0  -8

def test_divide(x, y):
    calc = Calculator()
    return calc.divide(x, y)

print test_divide(2, 4)
print test_divide(0, 4)
print test_divide(4, 2)
# Expect 0.5, None, 2.0


# Allows user to use the calculator interactively in command line
print "Python Calculator"

start = raw_input("would you like to start calculating? Choose y/n.")

# Allows user to use calculator repeatedly
while start == "y":

    # Instantiates calculator object
    calc = Calculator()

    print "What would you like the calculator to do?"

    # Clarifies valid user inputs
    function = raw_input("Type 'add' for addition, 'sub' for subtraction, 'mult' for multiplication, 'div' for division.")

    # Addition function
    if function == "add":
        a = int(raw_input("What is the first number you would like to add?"))
        b = int(raw_input("What is the second number you would like to add?"))
        print a, "plus", b, "equals", calc.add(a, b)

    # Subtraction function
    if function == "sub":
        a = int(raw_input("What is the number you would like to subtract from?"))
        b = int(raw_input("What number you would like to subtract?"))
        print a, "plus", b, "equals", calc.subtract(a, b)

    # Multiplication function
    if function == "mult":
        a = int(raw_input("What is the first number you would like to multiply?"))
        b = int(raw_input("What is the second number you would like to multiply?"))
        print a, "plus", b, "equals", calc.multiply(a, b)

    # Division function
    if function == "div":
        a = int(raw_input("What is the number you would like to divide from?"))
        b = int(raw_input("What is the number you would like to divide by?"))
        print a, "plus", b, "equals", calc.divide(a, b)

    # Allows user to use calculator again
    start = raw_input("would you like to use the calculator again? Choose y/n.")

if start == "n":
    print "Goodbye"


