
import pygame
import sys
pygame.init()

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (50, 200, 20)

#Modified from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/
#Python programming tutorial, Buttons and Sliders in Pygame, posted Feb. 19, 2017 by user DK3250
class Button():
    """
    This class lets the user click on a button to perform an action.
    The color of the button can change upon mouseover.
    """
    def __init__(self, text, location, action, actionArgs=[],
                 fontName="",
                 fontSize=16,
                 textColor=BLACK,
                 buttonColor=WHITE,
                 buttonSize=(80, 30)):
        """
        Args:
            text: a string written to the button surface, may be empty
            location: position of button on screen
            action: function to be called upon button press
            actionArgs: list of arguments to be passed to the action callback
            fontName: font used for button text
            fontSize: size of font for button text
            textColor: color of button text
            buttonColor: color of button, may change upon mouseover
            buttonSize: size of button
        """
        # Color and size of button
        self.color = buttonColor #the normal button color
        self.buttonColor = buttonColor #the color displayed upon mouseover
        self.textColor = textColor
        self.buttonSize = buttonSize

        # Button text
        self.font = pygame.font.SysFont(fontName, fontSize)
        self.txt = text
        self.txtSurf = self.font.render(self.txt, 1, self.textColor)
        self.txtRect = self.txtSurf.get_rect(center = [s//2 for s in self.buttonSize])

        # Surface and rect of button
        self.surface = pygame.surface.Surface(buttonSize)
        self.rect = self.surface.get_rect(center = location)

        # Action of the button
        self.call_back_ = action
        self.actionArgs = actionArgs

    """
    Calls the mouseover function, then updates the button surface with 
    color and text and blits to screen.
    """
    def draw(self, screen):
        self.mouseover()

        self.surface.fill(self.buttonColor)
        self.surface.blit(self.txtSurf, self.txtRect)
        screen.blit(self.surface, self.rect)
    """
    Changes the button color temporarily if the mouse is hovering 
    over the button
    """
    def mouseover(self):
        self.buttonColor = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.buttonColor = GREEN     #changes button color upon mouseover

    def callBack(self):
        if self.actionArgs == []:
            self.call_back_()
        else:
            self.call_back_(*self.actionArgs)

            
    def mouseButtonDown(buttons):
        pos = pygame.mouse.get_pos()
        for button in buttons:
            if button.rect.collidepoint(pos):
                button.callBack()

    def getTextFromBox(textInput):
        input = textInput.getText()
        #print(input)
        return input


