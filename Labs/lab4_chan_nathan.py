# Nathan Chan, channath@usc.edu
# ITP 115, Spring 2021
# Lab 4

numSpaces = 18
numSymbols = 1

for i in range(0, 10, 1):
    print((" " * numSpaces) + ("^ " * numSymbols))
    numSpaces = numSpaces - 2
    numSymbols = numSymbols + 2