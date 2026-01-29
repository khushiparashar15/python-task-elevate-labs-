# Different data types
a = 10          # int
b = 2.5         # float
c = "Hello"     # string
d = True        # boolean

# Print type of each
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Arithmetic operations
print("Sum:", a + b)
print("Product:", a * b)

# Type casting with error handling
try:
    num = input("Enter a number: ")
    n1 = int(num)
    n2 = float(num)
    print("Int:", n1)
    print("Float:", n2)
except:
    print("Invalid input")

# String + number
age = 20
print("My age is", age)

# Dynamic typing
x = 5
print(x, type(x))
x = "Python"
print(x, type(x))