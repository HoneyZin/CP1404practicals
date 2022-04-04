"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError occurs when a user gives an invalid value to a function but is of a valid argument.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when the numerator is divided by 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Adding a while loop which will ask the user until he/she puts the valid value would avoid the problem.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
