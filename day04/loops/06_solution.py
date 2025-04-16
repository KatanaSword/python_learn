# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

number = 10
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1

print(f"Factorial value of 10 is: {factorial}")