"""Password Checker"""

min_length = 5


def main():
    """Check if password has minimum length and print valid password"""
    password = get_password(min_length)
    print_asterisks(password)


def get_password(min_length):
    """Get user password and check the minimum length"""
    password = input("Please enter your password: ")
    while len(password) < min_length:
        print(f"Your password must have at least {min_length} characters.")
        password = input("Enter password: ")
    return password


def print_asterisks(word):
    """print string in asterisks"""
    for char in word:  # print('*' * len(word))
        print("*", end="")


main()
