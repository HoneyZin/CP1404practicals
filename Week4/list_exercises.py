# 1.
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number: ", numbers[0])
print("The last number: ", numbers[-1])
print("The smallest number: ", min(numbers))
print("The largest number: ", max(numbers))
print("The average of the numbers: ", sum(numbers) / len(numbers))

# 2.
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter Username: ")

if username in usernames:
    print("Access granted!")
else:
    print("Access denied :(")
