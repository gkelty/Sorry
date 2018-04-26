from Button import Button
from TextInputBox import TextInputBox
from dbConnection import dbConnection
from gameLoop import main
import pygame
import pygame.locals as pl
import sys
import os.path
pygame.init()
##pygame.font.init()

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

# create text object
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


# Display an intro page that gives user the option to sign in or register 
def intro(isNewUser, username):
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
            
        # if a user is creating a new account add creteUser and cancel buttons
        # depending on which is hit, perform some action
        if isNewUser == True:
            createUser = Button("Create new user", (300,400),dbConnection.addPlayer, actionArgs=[dbConnection.connectDB(),username], buttonSize=(100,30), buttonColor=DARKGREY)
            cancel = Button("Cancel",(300,450),intro, actionArgs=[False, None], buttonSize=(100,30), buttonColor=RED)
            buttons = [createUser, cancel]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        Button.mouseButtonDown(button)
                for button in buttons:
                    button.draw(screen)

            TextSurf, TextRect = text_objects(username, smallText)
            TextRect.topleft = ((255),(303))
            screen.blit(TextSurf, TextRect)
                    
                
        pygame.display.update()
        clock.tick(30)       
        
# creates display when the user decides to sign in. 
def startPage(username):


    screen = pygame.display.set_mode((displayWidth,displayHeight))
    screen.fill(SCREEN)

    newGameButton = Button("New Game", (300,200), newGame1, actionArgs=[username, True], buttonColor = FORESTGREEN, buttonSize=(200,30))
    resumeGameButton = Button("Resume Game", (300,250), resumeGame, buttonSize=(200,30),buttonColor = BLUE)
    instructionsButton = Button("Instructions", (300,300), instructions, actionArgs=[username], buttonSize=(200,30),buttonColor = DARKGREY)
    statsButton = Button("Game Statistics", (300,350), statsDisplay,actionArgs=[username], buttonSize=(200,30),buttonColor = BANANA)
    exitButton = Button("Exit", (300,400), exitGame, buttonSize=(200,30),buttonColor = RED)
    backButton = Button("Back to Sign In", (300,500), intro, actionArgs=[False, None], buttonColor = SCREEN, buttonSize=(200,30))


    buttons = [backButton,newGameButton, resumeGameButton, instructionsButton, statsButton, exitButton]

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

# creates display for the stats page
def statsDisplay(username):
    screen = pygame.display.set_mode((displayWidth,displayHeight))
    screen.fill(SCREEN)

    # create db connection
    dbConnect = dbConnection.connectDB()

    # grab stats from db
    stats = dbConnection.getStats(dbConnect, username)

    # create strings that will get drawn to screen and add to array
    gamesPlayed = ("Games Played: " + str(stats[0]))
    gamesInProgress = ("Games In Progress: " + str(stats[1]))
    totalWins = ("Total Wins: " + str(stats[2]))
    totalLosses = ("Total Losses: " + str(stats[3]))
    totalKOs = ("Total KOs: " + str(stats[4]))

    statistics = [gamesPlayed, gamesInProgress, totalWins, totalLosses, totalKOs]

    # create back button object
    backButton = Button("Main Menu", (300,500), startPage, actionArgs=[username], buttonColor = FORESTGREEN, buttonSize=(200,30))
    buttons = [backButton]
    
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
        for button in buttons:
            button.draw(screen)
        
        pygame.display.update()
        clock.tick(30)

# creates the first game setup page where numOfComps, user color, and pvp/pvc is set
def newGame1(username, valid):
    
    screen = pygame.display.set_mode((displayWidth,displayHeight))
    screen.fill(SCREEN)

    userColor = TextInputBox(250, 350, 140, 22)
    numOfComps = TextInputBox(250, 235, 140, 22)
    mode = TextInputBox(250, 435,140, 22)


    txtBoxes = [userColor, numOfComps, mode]

    colorButton = Button("continue..", (300,500), newGame2, actionArgs=[username, numOfComps,userColor, True, mode], buttonSize=(200,30),buttonColor = BLUE)
##    backButton = Button("Main Menu", (300,550), startPage, actionArgs=[username], buttonSize=(200,30), buttonColor = FORESTGREEN)
    
    buttons = [colorButton]

    clock = pygame.time.Clock()
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    Button.mouseButtonDown(button)                    
                    for txt in txtBoxes:
                        txt.updateEvent(event)

            else:
                for txt in txtBoxes:
                    txt.updateEvent(event)


        
        screen.fill(SCREEN)

        # create text that will display on screen
        TextSurf, TextRect = text_objects(("New Game Setup"), mediumText)
        TextRect.center = ((displayWidth/2),(displayHeight/7))
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(("Enter number of opponents (1-3): "), smallText)
        TextRect.topleft = ((20),(displayHeight/3))
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(("Choose your color (Red, Green, Blue, Yellow):  "), smallText)
        TextRect.topleft = ((20),(displayHeight/3 + 100))
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(("Player VS (Player,Computer): "), smallText)
        TextRect.topleft = ((20),(displayHeight/3 + 200))
        screen.blit(TextSurf, TextRect)

        for txt in txtBoxes:
            txt.updateDisplay()
            txt.draw(screen)

        for button in buttons:
            color = button.getButtonColor()
            button.draw2(screen,color)

        if valid == False:
            myfont = pygame.font.SysFont('segoe UI', 28)
            validation = "Please enter correct values"
            textsurface = myfont.render(validation, False, RED)
            screen.blit(textsurface, (200, 150))
            
        pygame.display.update()
        clock.tick(30)

# creates second game setup page where computer intelligence/behavior is set
def newGame2(username,numOfComps,userColor, valid, mode):
    
    # validate user input from newGame1
    colors = ["red", "blue", "green", "yellow"]
    if not isinstance(userColor, str):
        userColor = userColor.getText().lower()
    if not isinstance(numOfComps, int):
        numOfComps = numOfComps.getText()
    if isinstance(userColor, str):
        if userColor.isalpha() == False:
            newGame1(username, False)
        elif userColor not in colors:
            newGame1(username, False)
    if isinstance(numOfComps, str): 
        if numOfComps.isalpha():
            newGame1(username, False)

    numOfComps = int(numOfComps)
        
    if numOfComps < 1 or numOfComps > 3:
        newGame1(username, False)
                
    # create textbox objects
    textObjects = []
    height = displayHeight/3 + 40

    
    for i in range(0,numOfComps):
        behavior = TextInputBox(140, height, 50, 22)
        intelligence = TextInputBox(370, height, 50, 22)
        height += 75
        textObjects.append(behavior)
        textObjects.append(intelligence)

        
    possibleModes = ["player", "computer"]
    if not isinstance(mode, str):
        mode = mode.getText().lower()

    if mode not in possibleModes:
        newGame1(username, False)
    elif mode == "player":
        mode = 2
##        main(textObjects, numOfComps, userColor, username, mode)        
    elif mode == "computer":
        mode = 1


    # create new screen
    screen = pygame.display.set_mode((displayWidth,displayHeight))
    screen.fill(SCREEN)

    clock = pygame.time.Clock()
    
    # hardcode names of computer
    names = [ "Computer 1", "Computer 2", "Computer3"]

        
    # create button object
    colorButton = Button("set", (300,530), main, actionArgs=[textObjects, numOfComps, userColor, username, mode], buttonSize=(200,30),buttonColor = BLUE)
    backButton = Button("back", (300,570), newGame1, actionArgs=[username, True], buttonColor = FORESTGREEN, buttonSize=(200,30))

    buttons = [colorButton,backButton]
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    Button.mouseButtonDown(button)
                    
                for txt in textObjects:
                    txt.updateEvent(event)

            else:
                for txt in textObjects:
                    txt.updateEvent(event)
        screen.fill(SCREEN)

        # create text for page
        TextSurf, TextRect = text_objects(("New Game Setup"), mediumText)
        TextRect.center = ((displayWidth/2),(displayHeight/7))
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(("Set the Behavior and Intelligence of opponents"), instructionText)
        TextRect.center = ((displayWidth/2),(displayHeight/7 + 40))
        screen.blit(TextSurf, TextRect)   

        TextSurf, TextRect = text_objects(("Behavior"), smallText)
        TextRect.center = ((210),(190))
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(("(mean/nice)"), instructionText)
        TextRect.center = ((210),(215))
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(("Intelligence"), smallText)
        TextRect.center = ((460),(190))
        screen.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects(("(smart/dumb)"), instructionText)
        TextRect.center = ((460),(215))
        screen.blit(TextSurf, TextRect)

        # depending on number of computer opponents the user pics, display the names
        height = displayHeight/3 + 50
        for name in range(0,numOfComps):
            TextSurf, TextRect = text_objects((names[name] + ":"), smallText)
            TextRect.center = ((displayWidth/6 - 35),(height))
            screen.blit(TextSurf, TextRect)
            height += 75

        # draw the textboxes
        for i in range(0,(numOfComps)*2):
            textObjects[i].updateDisplay()
            textObjects[i].draw(screen)


        # draw the buttons
        for button in buttons:
            color = button.getButtonColor()
            button.draw2(screen,color)

        if valid == False:
            myfont = pygame.font.SysFont('segoe UI', 28)
            validation = "Please enter correct values"
            textsurface = myfont.render(validation, False, RED)
            screen.blit(textsurface, (200,450))

        pygame.display.update()
        clock.tick(30)

# eventually would be used for resume game
def resumeGame():
    print("resume game")


# creates page for when a user view instructions 
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
            instructions.append(line.strip('\n'))

        height = (displayHeight/2 - 100)
        for instruction in instructions:
                Surf, Rect = text_objects((instruction), instructionText)
                Rect.topleft = ((20),(height))
                screen.blit(Surf, Rect)
                height += 25

        backButton.draw(screen)
        pygame.display.update()

# exits game
def exitGame():
    print("Game Quit")
    pygame.quit()
    sys.exit()



