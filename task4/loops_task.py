# 1. For loop: print numbers 1 to 100
print("Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")

print("\n\nCountdown using while loop:")

# 2. While loop: countdown timer
count = 10
while count > 0:
    print(count)
    count -= 1
print("Go!\n")

# 3. break and continue
print("Break and Continue Demo:")
for i in range(1, 11):
    if i == 5:
        continue   # skip 5
    if i == 9:
        break      # stop at 9
    print(i)

print("\nString character iteration:")
# 4. Iterate over string
word = "Python"
for ch in word:
    print(ch)

print("\nMultiplication Table of 5:")
# 5. Multiplication table
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

print("\nRange with step of 2:")
# 6. Range with step
for i in range(2, 21, 2):
    print(i, end=" ")

print("\n\nEven numbers between 1 to 20:")
# 7. Loop + condition
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")