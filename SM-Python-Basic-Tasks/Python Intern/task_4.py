# Task 4

# Rock Paper Scissors

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game.

# Remember the rules:
#
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock


#######################################################################################################################################################################

from sys import exit

print("Rock Paper Scissors")

choices=["rock", "paper", "scissors"]

player_1_choice = input("Player 1 choose your choice rock/paper/scissors = " )
player_2_choice = input("Player 2 choose your choice rock/paper/scissors = " )
if player_1_choice not in choices or player_2_choice not in choices:
        print("Invalid input. Please give a valid input.")
        exit()
            
if (player_1_choice == "paper" and player_2_choice == "rock"
    or player_1_choice == "rock" and player_2_choice == "scissors"
    or player_1_choice == "scissors" and player_2_choice == "paper"):
    print("Congratulations !! Player 1 Wins.")
elif (player_1_choice ==  player_2_choice):
    print("Match is draw !!.")
else:
    print("Congratulations !! Player 2 Wins.")


