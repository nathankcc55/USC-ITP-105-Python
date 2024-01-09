# Nathan Chan, channath@usc.edu
# ITP 115, Spring 2021
# Lab 1

# Output to the user. Using lots of new line

print(" --\n"
      "|  |\n"
      "|  |\n"
      "|  |\n"
      " --")

print("You don't frighten us, English pig-dogs!\n"
      "Go and boil your bottoms, sons of a silly person!\n"
      "            -\"Monty Python and the Holy Grail\"")

# User input to help provide a value to our variables

day = input("Enter the day of the week:")
month = input("Enter the month:")
date = int(input("Enter the date:"))

# I just learned about f-string and it helped with formatting the final line, and I read that it is a relatively new feature.
# Odds 

print(f"Today is {day}, {month} {date}. Tomorrow will be {month} {date+1}.")

# This code will not work if the user inputs the date in float instead of an integer (e.g. twenty six instead of 26).
# It will compute an incorrect answer when counting from one month to the next (e.g. January 31 to January 32 instead of February 1).
# I'm not sure about the first problem, but the second problem might be solved by conditional statements (admittedly it does sound tedious to write a ton of if statements) and other methods that I hope to learn eventually.
