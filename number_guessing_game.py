#!/usr/bin/env python3
#Emma Ryan

#number guessing game

import sys#for clean exit
#i was gonna do the time sleep module too, but it would take too long and I don't care that much.

number_list = [i for i in range(101)] #all possible valid numbers (0-100)
#i included 0 becuase i need it to be a valid option for the quit code
print('''
+---------------------------+
|Secret Number Guessing Game|
+---------------------------+
''')

player1 = str(input("Enter Player 1 Name: ")) #Enter names for player 1 and player 2
player2 = str(input("Enter Player 2 Name: "))
player1 = player1.upper()
player2 = player2.upper()

print()
print("Welcome, ",player1," and ",player2,". Let's begin!",sep = "")
print()
print("AT ANY POINT, TYPE '0' (zero) TO END GAME EARLY")
print()
print("PLEASE ONLY LOOK AT THE SCREEN WHEN ITS YOUR TURN, NO CHEATING!!")
print()

print('''
+---------------+
|  ~ROUND ONE~  |
+---------------+ ''')
print()
print("+--------------->")
print("|  ~"+player1+"~  ")
print("+--------------->")
print()

while True:
    print("Enter a number 1-100 for",player2,"to try and guess:")
    print("(or '0' to end game early):")
    try: #incase they input a string or float, i dont want an actual error
        secret_number = int(input())
    except ValueError: #instead of the normal error crash, it will print this
        print("Not a valid number. Please try again.")
        continue
    if secret_number not in number_list: #if not 1-100
        print("Not a valid number. Please try again.")
        continue
    elif secret_number == 0: #quit number
        while True:
            end_game = input("Are you sure you want to quit?(Y/N): ")
            if end_game.upper() == "Y" or end_game == "YES":
                sys.exit()
            elif end_game.upper() == "N" or end_game == "NO":
                break
            else:
                continue     
    else:
        print("The secret number is now ", secret_number, ". SHHHHH, DON'T TELL!", sep = "")
        break

while True: #i didn't want it to move on to the other players turn without warning player 1, so this way they control when it switches.
    switch = input("Press Enter to End Turn and Start " + player2 + "'s Turn: ")
    if switch == "":
        break
    elif switch == 0:
        while True:
            end_game = input("Are you sure you want to quit?(Y/N): ")
            if end_game.upper() == "Y" or end_game == "YES":
                sys.exit()
            elif end_game.upper() == "N" or end_game == "NO":
                break
            else:
                continue
    else:
        continue
#this is just a spacefiller so that player 2 cant see the secret number while guessing
print("""
+---------------------------------------------+
|                                             |
|        ,/|         _.--''^``-...___.._.,;   |
|       /, \\'.     _-'          ,--,,,--'''   |
|      { \\    `_-''       '    /}             | 
|       `;;'            ;   ; ;               |
|   ._.--''     ._,,, _..'  .;.'              |
|    (,_....----'''     (,..--''              |
|                                             |
|                             _               |
|                            | |              |
|                            | |              |
|                            | |              |
|       |\\                   | |              |
|      /, ~\\                / /               |
|     X     `-.....-------./ /                |
|      ~-. ~  ~              |                |
|         \\             /    |                |
|          \\  /_     ___\\   /                 |
|          | /\\ ~~~~~   \\ |                   |
|          | | \\        || |                  |
|         (_/ (_/      ((_/                   |
|                                             |
|                                             |
|               ____                          |
|              />    >                        | 
|              | _  _|                        |
|             /\\ = x /                        |
|            /      |                         |
|            / \\    /                         |
|          _|   | | |                         |
|        / __|   | | |                        |
|       | (_ \\___\\_)_)                        |
|        \\__)                                 |
|                                             |
+---------------------------------------------+
        """)

print()
print("+--------------->")
print("|  ~"+player2+"~  ")
print("+--------------->")
print()

guesses_count2 = 0 #baseline number for number of guesses for player2

while True:
    print()
    print("Try to Guess the Secret Number!")

    try:
        guess = int(input("Enter a number from 1-100\n")) #they have to type in an integer
    except ValueError:
        print("Not a valid number. Please try again.") #
        continue
    
    if guess == secret_number and guesses_count2 == 0: #if they guess secret number on first try
        print("You guessed the secret number correct on the first try!")
        print("...")
        print("Wait")
        print("...")
        while True:
            print("Did you cheat? Be honest (Y/N):") #ask user if they cheated (they probably did)
            cheater_check = input()
            cheater_check = cheater_check.upper()
            if cheater_check == "Y" or cheater_check == "YES":
                guesses_count2 += 999 #if they cheated, their guesses count goes to 999, so basically they lose
                print("You loser, cheatings against the rules :(")
                break
            elif cheater_check == "N" or cheater_check == "NO":
                guesses_count2 += 1 #add one to their guess count (final number for their round)
                print("Congratulations! You ACTUALLY found the secret number on your first try!!")
                break
            else: #if they input something other than yes or no, go back and ask them again.
                print("Give me a real answer.")
                continue
        break
    
    elif guess == secret_number and guesses_count2 != 0: #if they guess the secret number, not on their first guess.
        guesses_count2 += 1
        print("Congratulations! You found the secret number after",guesses_count2,"guesses!")
        break
    elif guess > secret_number and guess in number_list: #if the guess is greater than the secret number, but not greater than 100
        guesses_count2 += 1 
        print("The Secret Number is LOWER than ",guess,"... Try Again!", sep = "")
        continue
    elif guess == 0: #if the guess is zero (exit number)
        while True:
            end_game = input("Are you sure you want to quit?(Y/N): ") #prompt to ask if user is sure they want to quit
            if end_game.upper() == "Y" or end_game == "YES":
                sys.exit() #if they say yes, quit game early
            elif end_game.upper() == "N" or end_game == "NO":
                break #if they say no, break and go back to loop of entering guess
            else:
                continue
    elif guess < secret_number: #if their guess is less than the secret number
        guesses_count2 += 1
        print("The Secret Number is HIGHER than ",guess,"... Try Again!", sep = "")
        continue
    else:
        print("Not a valid number. Please try again.") #if they type a number outside the range of 0-100
        continue

print()
print("Round 1 Complete! I hope you got a good score,",player2, end = ".")
print()
print()
print('''
+---------------+
|  ~ROUND TWO~  |
+---------------+ ''')
print()

while True:
    print("Enter a number 1-100 for",player1,"to try and guess:")
    print("(or '0' to end game early):")
    try:
        secret_number = int(input())
    except ValueError:
        print("Not a valid number. Please try again.")
        continue
    if secret_number not in number_list:
        print("Not a valid number. Please try again.")
        continue
    elif secret_number == 0:
        while True:
            end_game = input("Are you sure you want to quit?(Y/N): ")
            if end_game.upper() == "Y" or end_game == "YES":
                sys.exit()
            elif end_game.upper() == "N" or end_game == "NO":
                break
            else:
                continue 
    else:
        print("The secret number is now ",secret_number,". SHHHHH, DON'T TELL!",sep = "")
        break
      
while True:
    switch = input("Press Enter to End Turn and Start " + player1 + "'s Turn: ")
    if switch == "":
        break
    elif switch == 0:
        while True:
            end_game = input("Are you sure you want to quit?(Y/N): ")
            if end_game.upper() == "Y" or end_game == "YES":
                sys.exit()
            elif end_game.upper() == "N" or end_game == "NO":
                break
            else:
                continue    
    else:
        continue

print("""
+---------------------------------------------+
|                                             |
|        ,/|         _.--''^``-...___.._.,;   |
|       /, \\'.     _-'          ,--,,,--'''   |
|      { \\    `_-''       '    /}             | 
|       `;;'            ;   ; ;               |
|   ._.--''     ._,,, _..'  .;.'              |
|    (,_....----'''     (,..--''              |
|                                             |
|                             _               |
|                            | |              |
|                            | |              |
|                            | |              |
|       |\\                   | |              |
|      /, ~\\                / /               |
|     X     `-.....-------./ /                |
|      ~-. ~  ~              |                |
|         \\             /    |                |
|          \\  /_     ___\\   /                 |
|          | /\\ ~~~~~   \\ |                   |
|          | | \\        || |                  |
|         (_/ (_/      ((_/                   |
|                                             |
|                                             |
|               ____                          |
|              />    >                        | 
|              | _  _|                        |
|             /\\ = x /                        |
|            /      |                         |
|            / \\    /                         |
|          _|   | | |                         |
|        / __|   | | |                        |
|       | (_ \\___\\_)_)                        |
|        \\__)                                 |
|                                             |
+---------------------------------------------+
        """)
print()
print("+--------------->")
print("|  ~"+player1+"~  ")
print("+--------------->")
print()

guesses_count1 = 0

print()
while True:
    print()
    print("Try to Guess the Secret Number!") #round 2

    try:
        guess = int(input("Enter a number from 1-100\n")) #they have to type in an integer
    except ValueError:
        print("Not a valid number. Please try again.") #
        continue
    
    if guess == secret_number and guesses_count1 == 0: #if they guess secret number on first try
        print("You guessed the secret number correct on the first try!")
        print("...")
        print("Wait")
        print("...")
        while True:
            print("Did you cheat? Be honest (Y/N):") #ask user if they cheated (they probably did)
            cheater_check = input()
            cheater_check = cheater_check.upper()
            if cheater_check == "Y" or cheater_check == "YES":
                guesses_count1 += 999 #if they cheated, their guesses count goes to 999, so basically they lose
                print("You loser, cheatings against the rules :(")
                break
            elif cheater_check == "N" or cheater_check == "NO":
                guesses_count1 += 1 #add one to their guess count (final number for their round)
                print("Congratulations! You ACTUALLY found the secret number on your first try!!")
                break
            else: #if they input something other than yes or no, go back and ask them again.
                print("Give me a real answer.")
                continue
        break
    
    elif guess == secret_number and guesses_count1 != 0: #if they guess the secret number, not on their first guess.
        guesses_count1 += 1
        print("Congratulations! You found the secret number after",guesses_count1,"guesses!")
        break
    elif guess > secret_number and guess in number_list: #if the guess is greater than the secret number, but not greater than 100
        guesses_count1 += 1 
        print("The Secret Number is LOWER than ",guess,"... Try Again!", sep = "")
        continue
    elif guess == 0: #if the guess is zero (exit number)
        while True:
            end_game = input("Are you sure you want to quit?(Y/N): ") #prompt to ask if user is sure they want to quit
            if end_game.upper() == "Y" or end_game == "YES":
                sys.exit() #if they say yes, quit game early
            elif end_game.upper() == "N" or end_game == "NO":
                break #if they say no, break and go back to loop of entering guess
            else:
                continue
    elif guess < secret_number: #if their guess is less than the secret number
        guesses_count1 += 1
        print("The Secret Number is HIGHER than ",guess,"... Try Again!", sep = "")
        continue
    else:
        print("Not a valid number. Please try again.") #if they type a number outside the range of 0-100
        continue
print()
print("Round 2 Complete! I hope you got a good score,",player2, end = ".")
print()
print("Now, let's compare how many guesses it took you both and see who won!")
print()
print(player2,"'s Number of Guesses: ",guesses_count2, sep = "") #prints both players guess counts
print(player1,"'s Number of Guesses: ",guesses_count1, sep = "")
print()
#players can tie, or lowest score wins
if guesses_count2 == guesses_count1:
    print("It's a Tie! Well Played Everyone!!")
elif guesses_count2 > guesses_count1:
    print("The Winner is...",player1, end = "!")
elif guesses_count2 < guesses_count1:
    print("The Winner is...",player2, end = "!")

print()
while True:
    the_end = input("Press Enter to End Game: ")
    if the_end == "":
        break
    elif the_end == 0:
        while True:
            end_game = input("Are you sure you want to quit?(Y/N): ")
            if end_game.upper() == "Y" or end_game == "YES":
                sys.exit()
            elif end_game.upper() == "N" or end_game == "NO":
                break
            else:
                continue    
    else:
        continue
print("Goodbye.")
sys.exit()
