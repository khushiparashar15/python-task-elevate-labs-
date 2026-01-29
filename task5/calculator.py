# Addition function
def add(a, b=0):
    """Returns the sum of two numbers."""
    return a + b

# Subtraction function
def subtract(a, b=0):
    """Returns the difference of two numbers."""
    return a - b

# Multiplication function
def multiply(a, b=1):
    """Returns the product of two numbers."""
    return a * b

# Division function
def divide(a, b=1):
    """Returns the division of two numbers."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# Main program
def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1-4): ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    else:
        print("Invalid choice")
#run the program 
main()        