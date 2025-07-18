print("Welcome to the Simple Calculator!")
print("What is your name?")
name = input("Enter your name: ")
print("Hello", name + "!")

print("Please enter your symbol (+, -, *, /):")
symbol = input("Enter your symbol: ")

if symbol == "+":
    print("You have selected addition")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a + b)
elif symbol == "-":
    print("You have selected subtraction")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a - b)
elif symbol == "*":
    print("You have selected multiplication")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a * b)
elif symbol == "/":
    print("You have selected division")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b == 0:
        print("Error: Division by zero is not allowed")
    else:
        print("Result:", a / b)
else:
    print("You have not entered a valid operation symbol")
