# Love Calculator

# 💪 This is a Difficult Challenge 💪
# Instructions

# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

#     Take both people's names and check for the number of times the letters in the word TRUE occurs. 

#     Then check for the number of times the letters in the word LOVE occurs. 

#     Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."

# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"

# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."
# Example Input 1

# name1 = "Kanye West"
# name2 = "Kim Kardashian"

# Example Output 1

# Your score is 42, you are alright together.

# Example Input 2

# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"

# Example Output 2

# Your score is 73.

#solution

print("Welcome to the love calculator!")

name1 = input("What's your name? \n")
name2 = input("What is their name? \n")

#lowering the name
your_name = name1.lower()
her_or_his_name = name2.lower()

combined_name = your_name + her_or_his_name
#TRUE Count:
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

first_score = t+r+u+e

#LOVE Count:
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

second_score = l+o+v+e

love_score = int(str(first_score) + str(second_score))

if (love_score) < 10 or (love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score) <= 50 and (love_score) >= 40:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")