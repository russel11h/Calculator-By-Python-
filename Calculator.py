
print("What is your name?")
name = input("Enter your name: ")
print("Hello", name + "!")

print("Welcome to the Simple Calculator!")
print("Please enter your symbol (+, -, *, /):")
symbol = input("Enter your symbol: ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if symbol == "+":
    print("You have selected addition")
  
    print("Result:", a + b)
elif symbol == "-":
    print("You have selected subtraction")

    print("Result:", a - b)
elif symbol == "*":
    print("You have selected multiplication")

    print("Result:", a * b)
elif symbol == "/":
    print("You have selected division")

    if b == 0:
        print("Error: Division by zero is not allowed")
    else:
        print("Result:", a / b)
else:
    print("You have not entered a valid operation symbol")
