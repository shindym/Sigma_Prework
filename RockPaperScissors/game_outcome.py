# imports
import random

class Game():
    """This class holds the mechanism of the game Rock, Paper, Scissors"""
    @staticmethod
    def outcome(computer_action, user_action,):
        """ function takes in the inputs - user and computer and works out the game outcome"""
        # Outcomes
        #  0 - Draw
        # 1 - User wins
        # 2 - Computer wins
        game_outcome = 0

        if computer_action == user_action:  # Same action from both parties
            print("Draw")
            game_outcome = 0

        if computer_action == 0:  # Rock
            if user_action == 1:  # Paper
                print("User Wins")  #  Paper covers Rock
                game_outcome = 1
                

            elif user_action == 2:  # Scissors
                print("Computer Wins")  # Rock crushes Scissors
                game_outcome = 2
     

        if computer_action == 1:  # Paper
            if user_action == 0:  # Rock
                print("Computer Wins")  # Paper covers Rock
                game_outcome = 2


            elif user_action == 2:  # Scissors
                print("User Wins")  # Scissors cut paper
                game_outcome = 1
   

        if computer_action == 2:  # Scissors
            if user_action == 0:  #  Rock
                print("User Wins")  # Rock crushes Scissors
                game_outcome = 1
 

            elif user_action == 1:  # Paper
                print("Computer Wins")  # Scissors cut Paper
                game_outcome = 2


        return game_outcome

    @staticmethod
    def game_score(outcome, user_score, computer_score):
        """ Function responsible for changing the scoreboard depending on the game outcome"""
        if outcome == 1:
            user_score += 1

        elif outcome == 2:
            computer_score += 1
        return user_score, computer_score
             