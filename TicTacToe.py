#!/usr/bin/env python3
#Emma Ryan

#TicTacToe Final Project

# REQUIREMENTS:

# YES = Shebang line! Name!
# YES = Counts how many times you win/lose
# YES = Saves that to a file
# YES = Before starting, allows you to open your file and print your win/loss record
# YES = Exception handling needs to be evident
# YES = The computer should play the game using 'x's
# YES = The user should play the game using 'o's
# YES = The first move belongs to the computer - it always puts its first 'X' in the middle of the board
# YES = All the squares are numbered row by row starting with 1, Top-left should be "1", bottom-right "9"
# YES = The user inputs their move by entering the number of the square they choose - the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied
# YES = The program checks if the game is over - there are four possible verdicts: the game should continue ,the game ends with a tie, you win, or the computer wins
# YES = The computer responds with its move and the check is repeated
# YES = Don't implement any form of artificial intelligence - a random field choice made by the computer is good enough for the game.
# YES = Did not use any AI generated code - you typed everything

#imports:
import sys #for exit
import random #for computer's random turn

#function to check if winning conditions are met/game is over
def winner_check(move_counter, board_list): 
    winner = None

    for i in range(3):
        #checks for vertical wins
        if board_list[i] == board_list[i+3] == board_list[i+6]:
            winner = board_list[i]
            break
        #checks for horizontal wins
        elif board_list[i*3] == board_list[i*3+1] == board_list[i*3+2]:
            winner = board_list[i]
            break
    
    #checks for diagonal wins
    if board_list[0] == board_list[4] == board_list[8]:
        winner = board_list[i]

    elif board_list[2] == board_list[4] == board_list[6]:
        winner = board_list[i]
    
    #if there is no win, but 9 turns, its a tie
    elif move_counter == 9:
        winner = "tie"

    return winner

#game function
def game_function():
    #declaring variables
    winner = None
    move_counter = 1
    #computer starts in middle
    board_list = [1,2,3,4,"X",6,7,8,9]
    #print board
    print(f"""
    +---------+---------+---------+
    |         |         |         |
    |    {board_list[0]}    |    {board_list[1]}    |    {board_list[2]}    |
    |         |         |         |
    +---------+---------+---------+
    |         |         |         |
    |    {board_list[3]}    |    {board_list[4]}    |    {board_list[5]}    |
    |         |         |         |
    +---------+---------+---------+
    |         |         |         |
    |    {board_list[6]}    |    {board_list[7]}    |    {board_list[8]}    |
    |         |         |         |
    +---------+---------+---------+
    """)
    #loop will continue until there is winner (or tie)
    while winner == None:
        while True:
            try:   
                #player's turn
                player_move = int(input("Where would you like to place your token (1-9)?: "))
                #if there is not the base number in that slot (its already been chosen), repeat loop
                if board_list[player_move-1] != player_move:
                    print("That spot is already taken, try again.")
                    continue
                #else slot is free, mark that slot
                else:
                    board_list[player_move-1] = "O"
                    move_counter += 1
                    break
            except ValueError:
                print("That is not an integer. Please enter a valid input.")
            except:
                print("Unexpected Error")

        #check for winner
        winner = winner_check(move_counter, board_list)
        if winner != None:
            break

        while True:
            #computer's turn
            computer_move = random.randint(1,9)
            #if the random integer chosen is already filled, loop repeats
            if board_list[computer_move-1] != computer_move:
                continue
            #else slot is free, mark that slot
            else:
                board_list[computer_move-1] = "X"
                move_counter += 1
                #print the board
                print(f"""
    +---------+---------+---------+
    |         |         |         |
    |    {board_list[0]}    |    {board_list[1]}    |    {board_list[2]}    |
    |         |         |         |
    +---------+---------+---------+
    |         |         |         |
    |    {board_list[3]}    |    {board_list[4]}    |    {board_list[5]}    |
    |         |         |         |
    +---------+---------+---------+
    |         |         |         |
    |    {board_list[6]}    |    {board_list[7]}    |    {board_list[8]}    |
    |         |         |         |
    +---------+---------+---------+
    """)
                print(f"The computer played in spot {computer_move}.")
                break
            
        #checks for winner again after computer's turn
        winner = winner_check(move_counter, board_list)
        

    #once out of loop, because end condition is met, print results and return variable
    if winner == 'X':
        print("You Lose!")
    elif winner == "O":
        print("You Win!")
    elif winner == "tie":
        print("Its a Draw!")
    return winner

#declaring variables:
win_record = 0
loss_record = 0
tie_record = 0


#open file as read and record lines as variables
try:
    with open("WinLossRecord.txt", 'r') as file:
            #reads all the lines in file and saves it as a list, with \n after items
            score_record = file.readlines()
    #separates the list into 3 variable, gets rid of \n with .strip, and converts from string to int
    win_record = int((score_record[0]).strip())
    loss_record = int((score_record[1]).strip())
    tie_record = int((score_record[2]).strip())
#exception handling
except FileNotFoundError:
    print("(No Previous Game File Found)")

print()
print("---WELCOME TO TIC-TAC-TOE---")
print()

#infinite loop for menu, only way out is quit
while True:
    try:  
        menu_choice = int(input("\nPrint Record (1)\nStart Game (2)\nQuit Program (3)\nEnter Here: "))

        #printing the win record
        if menu_choice == 1: 
            print()
            print(f"Wins:   {win_record}")
            print(f"Losses: {loss_record}")
            print(f"Ties:   {tie_record}")
            continue
        
        #game start
        elif menu_choice == 2: 
            print()
            #calling game function
            winner = game_function()
            if winner == "O":
                win_record += 1
            elif winner == "X":
                loss_record += 1
            elif winner == "tie":
                tie_record += 1
            #opening file in write mode, or creating it if it doesnt exist
            with open("WinLossRecord.txt", 'w') as file:
                #copying down the new winlossrecord after every game
                file.write(f"{win_record}\n{loss_record}\n{tie_record}")
            continue
            
        #clean exit
        elif menu_choice == 3:
            print("Goodbye!")
            sys.exit()

        else:
            print("Not a valid input, try again.")
            continue
    except ValueError:
        print("That is not an integer. Please enter a valid input.")
        #i was going to also have a regular except, but apparently that catches the sys.exit, which i do not want. i cant think of any other specific exceptions 
        #that could happen with this input, so i think just the valueerror is good.

    #end of program :)