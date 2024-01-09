# Nathan Chan, channath@usc.edu
# ITP 115, Spring 2021
# Assignment 1
# Description: This program tells you a little bit about myself and a sneaky little lie about myself.
# Answers are expressed by these data types: strings, booleans, and integers

# Variables are created here

first = str("Nathan")
last = str("Chan")
statement1 = str("Squash is my favorite sport")
statement2 = str("I enjoy playing video games")
statement3 = str("I can speak 5 languages")
truth1 = bool(True)
truth2 = bool(True)
truth3 = bool(False)
pets = int(1)
siblings = int(2)

# I learned about f-string while searching for ways to help with formatting Lab 1.
# I liked it and decided to implement it for the assignment.
# This is the output to the user

print(f"Full name: {first} {last} \n")
print(f"Number of pets: {pets} \n"
      f"Number of siblings: {siblings} \n")
print(f"Statement 1: {statement1} \n"
      f"Statement 2: {statement2} \n"
      f"Statement 3: {statement3} \n")
print(f"Statement 1 is {truth1} \n"
      f"Statement 2 is {truth2} \n"
      f"Statement 3 is {truth3}")
