# Simple Calculator
print("Addition: +")
print("Subtraction: -")
print("Multiplication: *")
print("Division: /")

num1 = float(input("Enter the first number: "))
operation = input("Choose an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    print("Result:", num1 / num2)
else:
    print("Invalid operation")

input("Press Enter to exit...")
