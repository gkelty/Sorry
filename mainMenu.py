from Button import Button
from TextInputBox import TextInputBox
from dbConnection import dbConnection
import pygame
import pygame.locals as pl
import sys
import os.path
pygame.init()
pygame.font.init()

# Height and Width of display screen
displayWidth = 600
displayHeight = 600

# colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (50, 200, 20)

#text sizes
smallText = pygame.font.Font('freesansbold.ttf', 20)



def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


# Display an intro page that gives user the option to sign in or register 
def intro():
    intro = True
    screen = pygame.display.set_mode((displayWidth,displayHeight))

    # create the two buttons 
    signInButton = Button("Sign In/Register", (300,400),signInDisplay)
    registerButton = Button("Register",(300,450),register)


    buttons = [signInButton, registerButton]

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Button.mouseButtonDown(buttons)
                
        screen.fill(GREY)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Sorry!", largeText)
        TextRect.center = ((displayWidth/2),(displayHeight/3))
        screen.blit(TextSurf, TextRect)

        

        for button in buttons:
            button.draw(screen)
        
        pygame.display.update()
        


# creates display when the user decides to sign in. 
def signInDisplay():
    signIn = True
    # create screen
    screen = pygame.display.set_mode((displayWidth,displayHeight))

    # create text box objects
    userNameInput = TextInputBox(250, 190, 140, 22)
    ##passwordInput = TextInputBox(250, 229, 140, 22)
    
    # create button to save username/password
    signInButton = Button("Sign In", (400,300), dbConnection.signIn, actionArgs=[userNameInput])
    
    backButton = Button("Back", (300,300), intro)

    buttons = [signInButton,backButton]



    # Creates a clock to track time for the text input box
    clock = pygame.time.Clock()

    while signIn:
        screen.fill(GREY)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Button.mouseButtonDown(buttons)
                userNameInput.updateEvent(event)
                ##passwordInput.updateEvent(event)
            else:
                userNameInput.updateEvent(event)
                ##passwordInput.updateEvent(event)
                
        
        userNameInput.updateDisplay()
        ##passwordInput.updateDisplay()

        userNameInput.draw(screen)
        ##passwordInput.draw(screen)

        userSurf, userRect = text_objects("Username: ", smallText)
        ##passSurf, passRect = text_objects("Password: ", smallText)
        
        userRect.center = ((displayWidth/3),(displayHeight/3))
        ##passRect.center = ((displayWidth/3),(displayHeight/3 + 40))
        
        screen.blit(userSurf, userRect)
        ##screen.blit(passSurf, passRect)
        
        for button in buttons:
            button.draw(screen)        

        pygame.display.update()
        clock.tick(30)


def register():
    print("Thanks for registering")



