# Add
def add(x, y):
    return x + y


# Subtraction
def sub(x, y):
    return x - y


# Multiplication
def multiply(x, y):
    return x * y


# division
def divide(x, y):
    return x / y


# Square root
def square_root(x):
    return x ** 0.5


# Cube root
def cube_root(x):
    return x ** 0.3333333333333333333333333333333333333333333333333333


print("The performable operations for complex operations are listed below:")
print("1. For Square root..Use 'sqrt'")
print("2. For Cube root..Use 'cbrt'")
# Input from User
fn = input("Input the above symbols as per your use -->")
if fn == 'sqrt':
    input_1 = int(input("Enter the number-->"))
    print("The square root of the entered number is", square_root(input_1))
if fn == '+':
    input_2 = int(input("Enter the first number here-->"))
    input_3 = int(input("Enter the second number here-->"))
    print(input_2, "+", input_3, "=", add(input_2, input_3))
if fn == "-":
    input_4 = int(input("Enter the first number here-->"))
    input_5 = int(input("Enter the second number here-->"))
    print(input_4, "-", input_5, "=", sub(input_4, input_5))
if fn == "*":
    input_6 = int(input("Enter the first number here-->"))
    input_7 = int(input("Enter the second number here-->"))
    print(input_6, "*", input_7, "=", multiply(input_6, input_7))
if fn == "/":
    input_8 = int(input("Enter the first number here-->"))
    input_9 = int(input("Enter the second number here-->"))
    print(input_8, "/", input_9, "=", divide(input_8, input_9))
if fn == "cbrt":
    input_10 = int(input("Enter the number-->"))
    print("The cube root of the entered number is", cube_root(input_10))
else:
    print("Something is wrong in the input")
