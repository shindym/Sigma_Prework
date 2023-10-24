import pygame

# Button class 
class Button():
    def __init__(self,image,x,y,scale,suface):

        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, ((width*scale), (height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.x = x
        self.y = y
        self.clicked = False
        self.surface = suface
    
    def update_button_image(self,image,scale): # updates the image the button is showing
        self.image = image
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, ((width*scale), (height*scale)))

    def draw_button(self,image): # drawing the button onto screen

        self.surface.blit(self.image,(self.rect.x,self.rect.y))
    
    def check_if_button_pressed(self): # checks for user input 
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # user presses mouse/click down
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0: # user releases mouse/click up
                self.clicked = False
        return action

