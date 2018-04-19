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
DARKGREY = (127,127,127)
FORESTGREEN = (34,139,34)
BANANA = (227,207,87)
RED = (238,0,0)
BLUE=(30,144,255)
SCREEN = (115, 235, 220)

#text sizes
instructionText = pygame.font.Font('freesansbold.ttf', 14)
smallText = pygame.font.Font('freesansbold.ttf', 20)
mediumText = pygame.font.Font('freesansbold.ttf', 50)
largeText = pygame.font.Font('freesansbold.ttf',115)

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


# Display an intro page that gives user the option to sign in or register 
def intro():
    screen = pygame.display.set_mode((displayWidth,displayHeight))
    # create text input box object
    userNameInput = TextInputBox(250, 300, 140, 22)

    # create the two buttons 
    signInButton = Button("Sign In/Register", (300,400),dbConnection.signIn, actionArgs=[userNameInput,screen], buttonSize=(100,30), buttonColor=DARKGREY)

    # create array of buttons
    buttons = [signInButton]

    # start clock
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    Button.mouseButtonDown(button)
                userNameInput.updateEvent(event)
            else:
                userNameInput.updateEvent(event)
                
                
        screen.fill(SCREEN)

        # Display text object
        TextSurf, TextRect = text_objects("Sorry!", largeText)
        TextRect.center = ((displayWidth/2),(displayHeight/3))
        screen.blit(TextSurf, TextRect)

        
        userNameInput.updateDisplay()
        userNameInput.draw(screen)

        # Display text object
        userSurf, userRect = text_objects("Username: ", smallText)
        userRect.center = ((displayWidth/3),(310))
        screen.blit(userSurf, userRect)
        
        for button in buttons:
            button.draw(screen)        

        pygame.display.update()
        clock.tick(30)       
        
# creates display when the user decides to sign in. 
def startPage(username):
    screen = pygame.display.set_mode((displayWidth,displayHeight))
    screen.fill(SCREEN)

    newGameButton = Button("New Game", (300,200), newGame, actionArgs=[username], buttonColor = FORESTGREEN, buttonSize=(200,30))
    resumeGameButton = Button("Resume Game", (300,250), resumeGame, buttonSize=(200,30),buttonColor = BLUE)
    instructionsButton = Button("Instructions", (300,300), instructions, actionArgs=[username], buttonSize=(200,30),buttonColor = DARKGREY)
    statsButton = Button("Game Statistics", (300,350), statsDisplay,actionArgs=[username], buttonSize=(200,30),buttonColor = BANANA)
    exitButton = Button("Exit", (300,400), exitGame, buttonSize=(200,30),buttonColor = RED)


    buttons = [newGameButton, resumeGameButton, instructionsButton, statsButton, exitButton]

    # start clock
    clock = pygame.time.Clock()
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                   Button.mouseButtonDown(button)

        for button in buttons:
            button.draw(screen)

        # Display text object
        TextSurf, TextRect = text_objects(("Welcome, " + username), mediumText)
        TextRect.center = ((displayWidth/2),(displayHeight/5))
        screen.blit(TextSurf, TextRect)


        pygame.display.update()
        clock.tick(30)

def statsDisplay(username):
    screen = pygame.display.set_mode((displayWidth,displayHeight))
    screen.fill(SCREEN)
    
    dbConnect = dbConnection.connectDB()
    stats = dbConnection.getStats(dbConnect, username)

    backButton = Button("Main Menu", (300,500), startPage, actionArgs=[username], buttonColor = FORESTGREEN, buttonSize=(200,30))
    buttons = [backButton]

    gamesPlayed = ("Games Played: " + str(stats[0]))
    gamesInProgress = ("Games In Progress: " + str(stats[1]))
    totalWins = ("Total Wins: " + str(stats[2]))
    totalLosses = ("Total Losses: " + str(stats[3]))
    totalKOs = ("Total KOs: " + str(stats[4]))

    statistics = [gamesPlayed, gamesInProgress, totalWins, totalLosses, totalKOs]
    
    clock = pygame.time.Clock()
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    Button.mouseButtonDown(button)

        # Display title text object
        titleSurf, titleRect = text_objects(("Stats for " + username), mediumText)
        titleRect.center = ((displayWidth/2),(displayHeight/5))
        screen.blit(titleSurf, titleRect)

        # initialize height 
        height = (displayHeight/2 - 100)
        
        # Display the rest of the stat text objects
        for stat in statistics:
            Surf, Rect = text_objects((stat), smallText)
            Rect.center = ((displayWidth/2),(height))
            screen.blit(Surf, Rect)
            height += 50
        
        # Draw button to screen
        backButton.draw(screen)
        
        pygame.display.update()
        clock.tick(30)

def setColor(color1,color2):
    print(color1.getText())
    print(color2.getText())

    
def newGame(username):

    screen = pygame.display.set_mode((displayWidth,displayHeight))
    screen.fill(SCREEN)

    clock = pygame.time.Clock()
    names = [username, "Computer 1", "Computer 2", "Computer3"]

    color1 = TextInputBox(250, 300, 140, 22)
    color2 = TextInputBox(350, 300, 140, 22)

    colorButton = Button("set color", (300,250), setColor, actionArgs=[color1,color2], buttonSize=(200,30),buttonColor = BLUE)
    print(colorButton.buttonColor)
    buttons = [colorButton]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    Button.mouseButtonDown(button)
                    print(button.getButtonColor())

                    color1.updateEvent(event)
                    color2.updateEvent(event)

            else:
                color1.updateEvent(event)
                color2.updateEvent(event)

        screen.fill(SCREEN)

        TextSurf, TextRect = text_objects(("New Game Setup"), mediumText)
        TextRect.center = ((displayWidth/2),(displayHeight/7))
        screen.blit(TextSurf, TextRect)

        height = displayHeight/3
        for name in names:
            TextSurf, TextRect = text_objects((name), smallText)
            TextRect.center = ((displayWidth/6),(height))
            screen.blit(TextSurf, TextRect)
            height += 100
            
        color1.updateDisplay()
        color1.draw(screen)
        color2.updateDisplay()
        color2.draw(screen)


        for button in buttons:
            color = button.getButtonColor()
            button.draw2(screen,color)
            print(color)
        pygame.display.update()
        clock.tick(30)

    
    print("start new game here")

    print(colorInput)
    
def resumeGame():
    print("resume game")

    
def instructions(username):
    screen = pygame.display.set_mode((displayWidth,displayHeight))
    screen.fill(SCREEN)

    backButton = Button("Main Menu", (300,500), startPage, actionArgs=[username], buttonColor = FORESTGREEN, buttonSize=(200,30))
    buttons = [backButton]
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    Button.mouseButtonDown(backButton)
                    
        # Display title text object
        titleSurf, titleRect = text_objects(("Instructions:"), mediumText)
        titleRect.center = ((displayWidth/2),(displayHeight/5))
        screen.blit(titleSurf, titleRect)
    
        infile = open("instructionText.txt", 'r')
        instructions = []
        for line in infile:
            instructions.append(line)

        height = (displayHeight/2 - 100)
        for instruction in instructions:
                Surf, Rect = text_objects((instruction), instructionText)
                Rect.topleft = ((20),(height))
                screen.blit(Surf, Rect)
                height += 25

        backButton.draw(screen)
        pygame.display.update()

def exitGame():
    print("Game Quit")
    pygame.quit()
    sys.exit()



