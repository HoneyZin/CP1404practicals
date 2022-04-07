numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] - 3
# numbers[-1] - 2
# numbers[3] - 1
# numbers[:-1] - [3, 1, 4, 1, 5, 9]
# numbers[3:4] - [1]
# 5 in numbers - True
# 7 in numbers - False
# "3" in numbers - False
# numbers + [6, 5, 3] - [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


# 1.
numbers[0] = "ten"
print("1= ", numbers)

# 2.
numbers[-1] = 1
print("2= ", numbers)

# 3.
three = numbers[2:]
print("3= ", three)

# 4.
print("4= ",9 in numbers)
