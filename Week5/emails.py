"""Email to name dictionary"""


def main():
    """Store email and names in a dictionary."""
    emails_to_names = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        checking = input(f"Is your name {name}? (Y/n) ")
        if checking.lower() != "y" and checking != "":
            name = input("Name: ")
        emails_to_names[email] = name
        email = input("Email: ")

    # Print all names and email addresses.
    print()
    for key, value in emails_to_names.items():
        print(f"{value}: {key}")

    print("\nThank you.")


def extract_name(email):
    """Extract name from email address."""
    no_at_name = email.split('@')[0]  # Eg: ['honey.zin']
    no_dot_name = no_at_name.split('.')  # Eg: ['honey', 'zin']
    name = " ".join(no_dot_name).title()  # Eg: "Honey Zin"
    return name


if __name__ == "__main__":
    main()
