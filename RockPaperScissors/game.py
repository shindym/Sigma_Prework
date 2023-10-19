import random

# Ascii art sourced online (https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe)


class Action():

  ROCK = 0
  PAPER = 1
  SCISSORS = 2
  ALL = [ROCK, PAPER, SCISSORS]

  def __init__(self, ):
    self.action = None

  def __eq__(self, action: int) -> bool:
    return self.action == action

  def __int__(self) -> int:
    return self.action

  def set_action(self, action: int):
    self.action = action

  def get_action(self):
    return self.action

  def translate_action(self, player):
    if self.action == 0:

      print(f"{player} chose Rock\n")
      print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

    elif self.action == 1:
      print(f"{player} chose Paper\n")
      print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

    else:
      print(f"{player} chose Scissors\n")
      print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


def outcome(
    computer_action,
    user_action,
):

  # Outcomes
  # 0 - Draw
  # 1 - User wins
  # 2 - Computer wins

  game_outcome = 0

  if computer_action == user_action:  # Same action from both parties
    print("Draw")
    game_outcome = 0

  if computer_action == 0:  # Rock
    if user_action == 1:  # Paper
      print("User Wins")  # Paper covers Rock
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
    if user_action == 0:  # Rock
      print("User Wins")  # Rock crushes Scissors
      game_outcome = 1

    elif user_action == 1:  # Paper
      print("Computer Wins")  # Scissors cut Paper
      game_outcome = 2

  return game_outcome


def end_of_game_message(computer_score, user_score):
  # Prints final message to User
  print("----------------------------------------")
  score_text = "\nFinal Score\nComputer: {} User: {}".format(
      computer_score, user_score)
  print(score_text)
  print("")

  if user_score > computer_score:
    print("   .-'''''-.")
    print("  /   O O   \\")
    print(" |     ∆     |")
    print(" |   \___/   |")
    print("  \\         /")
    print("   `'-----'")
    print("You Win !")

  elif user_score < computer_score:
    print("   .-'''''-.")
    print("  /   O O   \\")
    print(" |     ∆     |")
    print(" |   ____    |")
    print("  \\         /")
    print("   `'-----'")

    print("You Lose :(")

  else:

    print("   .-'''''-.")
    print("  /   O O   \\")
    print(" |     ∆     |")
    print(" |     O     |")
    print("  \\         /")
    print("   `'-----'")
    print("It's a Draw :0")


def game():
  print("Welcome to Rock,Paper,Scissors!")
  print("----------------------------------------")

  end_game_flag = False  # Flag to tell when the last game has finished
  # Scoreboard
  computer_score = 0
  user_score = 0
  game_count = 0
  # Initiates action class for User and Computer
  user = Action()
  computer = Action()
  possible_actions = user.ALL.copy()  # Copies possible actions

  num_games = int(
      input("How many games would you like to play? "
            ))  # Input from user on how many games they would like to play

  while end_game_flag == False:
    # User
    user_choice = int(
        input("Enter a choice \nrock:0 \npaper:1 \nscissors:2\n"))
    user.set_action(user_choice)
    user.translate_action(player="User")

    # Computer
    computer.set_action(random.choice(possible_actions))
    computer.translate_action(player="Computer")
    # Outcome of actions chosen
    action_outcome = outcome(computer.get_action(), user.get_action())
    # Increasing score of player who won
    if action_outcome == 1:
      user_score += 1
    elif action_outcome == 2:
      computer_score += 1
    game_count += 1

    # Prints score to console so user can keep track
    score_text = "\n Score\nComputer: {} User: {}".format(
        computer_score, user_score)
    print(score_text)
    print("")

    # All games ended
    if game_count == num_games:
      end_game_flag = True

  end_of_game_message(computer_score, user_score)


game()
