import pygame
import sys
from Button import Button
from TextInputBox import TextInputBox

"""
BUTTON: The two functions below are for testing and demonstration of
button function and will be replaced with functions that do the action 
required upon button click (e.g., go to main menu, start game)
"""
def myGreatFunction():
    print("Great!  " *5)

def myFantasticFunction():
    print("Fantastic! " *5)

def getTextFromBox(textInput):
    input = textInput.getText()
    #print(input)
    return input

def main():
    # Create screen
    screen = pygame.display.set_mode((1000, 200))

    # Create TextInput-object
    textInput = TextInputBox(100, 100, 140, 22)

    # Creates a clock to track time for the text input box
    clock = pygame.time.Clock()

    # Define additional button colors (beyond white, grey, black)
    GREEN = (50, 200, 20)

    # Create buttons
    button1 = Button("Great!", (60, 30), myGreatFunction)
    button2 = Button("Fantastic!", (60, 70), myFantasticFunction, buttonColor=GREEN)
    button3 = Button("Save", (260, 150), getTextFromBox, actionArgs=[textInput])

    # Put buttons in a list for simpler game loop
    buttons = [button1, button2, button3]

    #Example game loop
    while True:
        screen.fill((225, 225, 225))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    button.mouseButtonDown()
                    textInput.updateEvent(event)
            else:
                textInput.updateEvent(event)
        textInput.updateDisplay()

        # Blit text input box surface onto the screen
        textInput.draw(screen)

        # Blit buttons on screen
        for button in buttons:
            button.draw(screen)

        pygame.display.update()
        clock.tick(30)

main()
