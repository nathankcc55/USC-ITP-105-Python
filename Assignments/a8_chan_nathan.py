# Nathan Chan, channath@usc.edu
# ITP 115, Spring 2021
# Assignment 8
# Description:
# This program simulates a two player Tic Tac Toe game

# Same parent directory
import TicTacToeHelper


# Checks to see if a spot is taken or not and returns true or false
def isValidMove(boardList, spot):
    if 0 <= spot <= 8:
        if boardList[spot] == "x" or boardList[spot] == "o":
            return False
        else:
            return True


# The player
def updateBoard(boardList, spot, playerLetter):
    boardList[spot] = playerLetter


# Prints the tic tac toe board
def printPrettyBoard(boardList):
    print()
    counter = 0

    # 3 by 3
    for i in range(3):
        for j in range(3):

            # Every first and second element of a row will end with a vertical line
            if j == 0 or j == 1:
                print(boardList[counter], end=" | ")
                counter += 1

            # The list will go up by one count every time
            else:
                print(boardList[counter])
                counter += 1

        # First two rows will print a horizontal line
        if i == 0 or i == 1:
            print("---------")


# Function to actually interact with the game
def playGame():
    numberList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    # Use numberList elements to make the 3x3 board
    printPrettyBoard(numberList)

    # Count moves between two players
    moves = 0

    # Determine who's turn it is, and it starts with x
    turn = "x"

    # Game is ended is false
    end_game = False

    # While game is not ended, players get to pick their spots
    while not end_game:

        # Used later to check if the move the player made was valid or not
        valid_move = False

        # When not valid, player gets to pick a spot
        while not valid_move:
            spot = int(input("Player " + turn + ", pick a spot: "))

            # Call isValidMove function using the numberList list and the spot from user input
            valid_move = isValidMove(numberList, spot)

            #
            if valid_move:
                updateBoard(numberList, spot, turn)
                moves += 1
                if turn == "x":
                    turn = "o"
                elif turn == "o":
                    turn = "x"
                printPrettyBoard(numberList)
            else:
                print("Invalid move, please try again.")

        winner = TicTacToeHelper.checkForWinner(numberList, moves)
        if winner == "x" or winner == "o" or winner == "s":
            end_game = True
            print("\nGame over!")
            if winner == "x" or winner == "o":
                print("Player " + winner + " is the winner!")
            else:
                print("Stalemate reached!")


def main():
    setup_game = True
    print("Welcome to Tic Tac Toe!")
    while setup_game:
        playGame()
        new_game = False
        while new_game != "y" and new_game != "n":
            new_game = input("Would you like to play another round? (y/n): ")
            if new_game.lower() == "y":
                pass
            elif new_game.lower() == "n":
                setup_game = False
            else:
                print("Invalid choice. Please select 'y' or 'n'")
    print("Goodbye!")


main()
