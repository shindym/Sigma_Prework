# Example file showing a basic pygame "game loop"
import pygame
import button as button
import random
import game_outcome
import os

# pygame setup

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Rock,Paper,Scissors")
image_filepath = f"{os. getcwd()}/Images/"
icon = pygame.image.load(f"{image_filepath}rock_paper_scissors_icon.png")
pygame.display.set_icon(icon)
background_colour = 250,243,221

# functions

# scales image up or down
def transform_image(image,scale):
    width = image.get_width()
    height = image.get_height()
    return pygame.transform.scale(image, ((width*scale), (height*scale)))

#changes the message viewed on the screen based on games outcome
def change_message(outcome):
    if outcome == 0:
        message = messages[0]
    elif outcome == 1:
        message = messages[1]
    else:
        message = messages[2]
    return message

# not my code - sourced from https://www.pygame.org/pcr/hollow_outline/index.php
def textHollow(font, message, fontcolor):
    notcolor = [c^0xFF for c in fontcolor]
    base = font.render(message, 0, fontcolor, notcolor)
    size = base.get_width() + 2, base.get_height() + 2
    img = pygame.Surface(size, 16)
    img.fill(notcolor)
    base.set_colorkey(0)
    img.blit(base, (0, 0))
    img.blit(base, (2, 0))
    img.blit(base, (0, 2))
    img.blit(base, (2, 2))
    base.set_colorkey(0)
    base.set_palette_at(1, notcolor)
    img.blit(base, (1, 1))
    img.set_colorkey(notcolor)
    return img

# not my code - sourced from https://www.pygame.org/pcr/hollow_outline/index.php
def textOutline(font, message, fontcolor, outlinecolor):
    base = font.render(message, 0, fontcolor)
    outline = textHollow(font, message, outlinecolor)
    img = pygame.Surface(outline.get_size(), 16)
    img.blit(base, (1, 1))
    img.blit(outline, (0, 0))
    img.set_colorkey(0)
    return img

# image imports

title = pygame.image.load(f"{image_filepath}title.png").convert_alpha()
score_label = pygame.image.load(f"{image_filepath}score.png").convert_alpha()
restart_label = pygame.image.load(f"{image_filepath}restart_label.png").convert_alpha()
vs_icon_img = pygame.image.load(f"{image_filepath}vs_icon.png").convert_alpha()

# game messages
win_label = pygame.image.load(f"{image_filepath}win_label.png").convert_alpha()
lose_label = pygame.image.load(f"{image_filepath}lose_label.png").convert_alpha()
draw_label = pygame.image.load(f"{image_filepath}draw_label.png").convert_alpha()
choose_label = pygame.image.load(f"{image_filepath}choose_label.png").convert_alpha()

# rock, paper, scissors picture imports & x,y positions

rock_img = pygame.image.load(f"{image_filepath}rock_icon.png").convert_alpha()

rockX = 100
rockY = 300

paper_img = pygame.image.load(f"{image_filepath}paper_icon.png").convert_alpha()

paperX = 500
paperY = 300

scissors_img = pygame.image.load(f"{image_filepath}scissors_icon.png").convert_alpha()

scissorsX = 900
scissorsY = 300

#clock = pygame.time.Clock()

# variables
computer_pick = None
reset_key = False
running = True
moves = ["Rock","Paper","Scissors"]
move_images = [rock_img,paper_img,scissors_img]
messages = [draw_label,win_label,lose_label,choose_label]

# creation of buttons
rock_button = button.Button(rock_img,rockX,rockY,0.5,screen)
paper_button = button.Button(paper_img,paperX,paperY,0.5,screen)
scissors_button = button.Button(scissors_img,scissorsX,scissorsY,0.5,screen)
restart_label_button = button.Button(restart_label,1050,0,1,screen)


# assigning values to X and Y variable
X = 600
Y = 50

# message which is initially shown
message = messages[3]

# score board 
font = pygame.font.SysFont("Arial", 36)
white = 255, 255, 255
outline = 96, 18, 75
bigfont = pygame.font.Font(None, 60)
user_score = 0
computer_score = 0

while running:

    score = f"{user_score} : {computer_score} "
    
    score_message = textOutline(bigfont,score, outlinecolor=outline, fontcolor=white)
   
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    # set up 
    screen.fill((background_colour))
    screen.blit(title,(350,50))
    screen.blit(message,(500,600))
    screen.blit(score_label,(0,0))
    screen.blit(score_message,(75,40))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: # checking if user is pressing "r" key - used to reset game
            if event.key == pygame.K_r:
                reset_key = True
    
    # drawing buttons on screen
    rock_button.draw_button(rock_img)
    paper_button.draw_button(paper_img)
    scissors_button.draw_button(scissors_img)
    restart_label_button.draw_button(restart_label)
    

    # checking if any buttons have been pressed
    # Rock 
    if rock_button.check_if_button_pressed() == True:
        if computer_pick is None:
            # computer picks a move if it has not chosen one already
            computer_pick = random.choice(moves)
            computer_pick_img = move_images[(moves.index(computer_pick))]
            # changes other buttons to show the outcome 
            paper_button.update_button_image(vs_icon_img,2)
            scissors_button.update_button_image(computer_pick_img,scale =0.5)
            # calcutes the outcome, updates the score and changes message
            outcome = game_outcome.Game.outcome(computer_action=moves.index(computer_pick),user_action= 0)
            user_score,computer_score = game_outcome.Game.game_score(outcome=outcome,user_score=user_score,computer_score=computer_score)
            message = change_message(outcome)

   # Paper
    elif paper_button.check_if_button_pressed() == True:
        # computer picks a move if it has not chosen one already
        if computer_pick is None:
            computer_pick = random.choice(moves)
            computer_pick_img = move_images[(moves.index(computer_pick))]
            # changes other buttons to show the outcome 
            rock_button.update_button_image(paper_img,0.5)
            paper_button.update_button_image(vs_icon_img,2)
            scissors_button.update_button_image(computer_pick_img,0.5)
            # calcutes the outcome, updates the score and changes message
            outcome = game_outcome.Game.outcome(computer_action=moves.index(computer_pick), user_action= 1)
            user_score,computer_score = game_outcome.Game.game_score(outcome=outcome,user_score=user_score,computer_score=computer_score)
            message = change_message(outcome)


    elif scissors_button.check_if_button_pressed() == True:
        # computer picks a move if it has not chosen one already
        if computer_pick is None:
            computer_pick = random.choice(moves)
            computer_pick_img = move_images[(moves.index(computer_pick))]
            # changes other buttons to show the outcome 
            rock_button.update_button_image(scissors_img,0.5)
            paper_button.update_button_image(vs_icon_img,2)
            scissors_button.update_button_image(computer_pick_img,0.5)
            # calcutes the outcome, updates the score and changes message
            outcome = game_outcome.Game.outcome(computer_action=moves.index(computer_pick), user_action= 2)
            user_score,computer_score = game_outcome.Game.game_score(outcome=outcome,user_score=user_score,computer_score=computer_score)
            message = change_message(outcome)

    # reset button
    elif restart_label_button.check_if_button_pressed() == True or reset_key==True: # reset is triggered by button being pressed by mouse or user pressing 'r' key 
        #resets variables to initial values
        computer_pick = None
        reset_key =False
        rock_button.update_button_image(rock_img,0.5)
        paper_button.update_button_image(paper_img,0.5)
        scissors_button.update_button_image(scissors_img,0.5)
        message = messages[3]

    pygame.display.update()
    pygame.display.flip()

pygame.quit()