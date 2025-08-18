import math

print("=== Advanced Calculator ===")
print("Available operations:")
print("Addition: +")
print("Subtraction: -")
print("Multiplication: *")
print("Division: /")
print("Power: ^")
print("Square Root: sqrt")
print("Greatest Common Divisor (GCD): gcd")
print("Least Common Multiple (LCM): lcm")

operation = input("Choose an operation (+, -, *, /, ^, sqrt, gcd, lcm): ")

# Square root requires only one number
if operation == "sqrt":
    num = float(input("Enter a number: "))
    if num < 0:
        print("Error: Cannot calculate square root of a negative number!")
    else:
        print("Result:", math.sqrt(num))

# GCD and LCM require integers only
elif operation in ["gcd", "lcm"]:
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    if operation == "gcd":
        print("Result (GCD):", math.gcd(num1, num2))
    elif operation == "lcm":
        # math.lcm is available in Python 3.9+
        try:
            print("Result (LCM):", math.lcm(num1, num2))
        except AttributeError:
            # Manual formula for LCM
            print("Result (LCM):", abs(num1 * num2) // math.gcd(num1, num2))

# Other operations require two numbers
else:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)
    elif operation == "^":
        print("Result:", num1 ** num2)
    elif operation == "%":
        print("Result:", num1 % num2)
    else:
        print("Invalid operation")

input("Press Enter to exit...")
