"""
CP1404/CP5632 - Practical - Suggested Solution
Fixed program to determine score status
"""

user_score = float(input("Enter score: "))
if user_score < 0 or user_score > 100:
    print("Invalid score. Please enter score between 0 and 100.")
elif user_score >= 90:
    print("Excellent!")
elif user_score >= 50:
    print("Pass.")
else:
    print("Bad :(")
