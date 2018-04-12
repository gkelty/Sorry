from Button import Button
from TextInputBox import TextInputBox
import pygame
import pygame.locals as pl
import sys
import os.path
pygame.init()
pygame.font.init()

displayWidth = 600

displayHeight = 600

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
smallText = pygame.font.Font('freesansbold.ttf', 20)



def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


# Display an intro page that gives user the option to sign in or register 
def intro():
    intro = True
    introGameDisplay = pygame.display.set_mode((displayWidth,displayHeight))

    # create the two buttons 
    signInButton = Button("Sign In", (300,400),signedIn)
    registerButton = Button("Register",(300,450),register)


    buttons = [signInButton, registerButton]

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Button.mousebuttondown(buttons)
                
        introGameDisplay.fill(WHITE)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Sorry!", largeText)
        TextRect.center = ((displayWidth/2),(displayHeight/2))
        introGameDisplay.blit(TextSurf, TextRect)
        

        for button in buttons:
            button.draw()
        
        pygame.display.update()
        



def signedIn():
    signIn = True
    signInGameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
    clock = pygame.time.Clock()
    signInGameDisplay.fill(WHITE)
    clock = pygame.time.Clock()

    signInButton = Button("Sign In", (400,300),nextPage)

    buttons = [signInButton]

 #Create TextInput-object
    userNameInput = TextInputBox(250, 229, 140, 22)
    passwordInput = TextInputBox(250, 190, 140, 22)
    clock = pygame.time.Clock()

    while signIn:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Button.mousebuttondown(buttons)

        # Feed it with events every frame
        userNameInput.update(events)
        passwordInput.update(events)


        # Blit its surface onto the screen
        userNameInput.draw(signInGameDisplay)
        passwordInput.draw(signInGameDisplay)

        pygame.display.flip()
        clock.tick(30)

        userSurf, userRect = text_objects("Username: ", smallText)
        passSurf, passRect = text_objects("Password: ", smallText)
        userRect.center = ((displayWidth/3),(displayHeight/3))
        passRect.center = ((displayWidth/3),(displayHeight/3 + 40))
        signInGameDisplay.blit(userSurf, userRect)
        signInGameDisplay.blit(passSurf, passRect)
        signInButton.draw()
        
    print(userNameInput.get_text())
    print(passwordInput.get_text())
    
def nextPage():
    print("next page")


    
##    while signIn:
##        event = pygame.event.get()
##        for event in events:
##            if event.type == pygame.QUIT:
##                pygame.quit()
##                sys.exit()
##                
##        userSurf, userRect = text_objects("Username: ", smallText)
##        passSurf, passRect = text_objects("Password: ", smallText)
##        userRect.center = ((displayWidth/3),(displayHeight/3))
##        passRect.center = ((displayWidth/3),(displayHeight/3 + 40))
##
##        userNameInput.draw(signInGameDisplay)
##
##        
##        signInGameDisplay.blit(userSurf, userRect)
##        signInGameDisplay.blit(passSurf, passRect)
##
####        pygame.display.update()
##        pygame.display.flip()
##        clock.tick(30)

def register():
    print("Thanks for registering")


intro()
