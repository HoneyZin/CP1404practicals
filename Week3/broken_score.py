"""
CP1404
Honey Zin
Fixed program to determine score status with function
"""


def main():
    """Get user input and print score"""
    user_score = float(input("Enter score: "))
    print(score_status(user_score))


def score_status(user_score):
    """Differentiate the user's input for scores"""
    if user_score < 0 or user_score > 100:
        print("Invalid score. Please enter score between 0 and 100.")
    elif user_score >= 90:
        print("Excellent!")
    elif user_score >= 50:
        print("Pass.")
    else:
        print("Bad :(")


if __name__ == '__main__':
    main()
