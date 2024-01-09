# Nathan Chan, channath@usc.edu
# ITP 115, Spring 2021
# Assignment 2
# Description: This program uses user input to create a Mad Libs story

# A mix of strings, integers, and float variables identified by user input
animal = input("Enter an animal (plural): ")
adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter a verb ending in 'ing': ")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))
decimal = float(input("Enter a number with a decimal: "))

# This is the Mad Libs story based on user input
# I used escape characters to help indicate the inputted words into the story
# This code will also make the subtraction of two numbers in integers, and then treat the calculation into a string
print("\n")
print("Our records indicate that the extinction of the \"" + animal + "\" occurred in \"" + str(num1) + "\" BC.\n"
      "They seem to be \"" + adj1 + "\" beings that thrive upon \"" + verb2 + "\".\n"
      "Funnily enough, \"" + animal + "\" typically require \"" + str(decimal) + "\" hours to \"" + verb1 + "\".\n"
      "The most peculiar thing about them is that the average male grows to \"" + str(num2) + "\" centimeters tall.\n"
      "Meanwhile, their female counterparts can grow to \"" + str(num3) + "\" centimeters tall.")

# I use the abs() function, which gives a positive value for any number in return. Good for calculating difference.
print("Thus, the difference in their height is a staggering \"" + str(abs(int(num2) - int(num3))) + "\" centimeters.\n"
      "Truly \"" + adj2 + "\" creatures they are!")
