import pygame
import sys
from boardButton import BoardButton
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
                 name=0,
                 fontName="",
                 fontSize=16,
                 textColor=BLACK,
                 buttonColor=WHITE,
                 backgroundColor=GREY,
                 buttonSize=(80, 30),
                 active=True,
                 boardButton = False,
                 boardButtObj = 0):
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
        self.name = name
        # Color and size of button
        self.buttonColor = buttonColor #the current button color
        self.color = buttonColor #the normal button color
        self.mouseoverColor = backgroundColor #the color displayed upon mouseover
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
        self.active = active
        if(boardButton == True):
            self.boardButton = boardButtObj

    """
    BUTTON: Checks if a button is hit on mouse click and activates the relevant 
    button action.
    """
    def getBoardButton(self):
        return(self.boardButton.getTileNum())
    def mouseButtonDown(self, buttons):
        pos = pygame.mouse.get_pos()
        for button in buttons:
            if button.rect.collidepoint(pos):
                buttonColor = self.mouseoverColor
                self.setButtonColor(buttonColor)
                button.callBack()
                
        return self.buttonColor
                

    """
    Calls the mouseover function, then updates the button surface with 
    color and text and blits to screen.
    """
    def draw(self, screen):
        self.mouseover()

        if self.active:
            if len(self.buttonColor) == 4:
                self.surface.set_alpha(self.buttonColor[3])
            else:
                self.surface.set_alpha(None)
            self.surface.fill(self.buttonColor)
            self.surface.blit(self.txtSurf, self.txtRect)
            screen.blit(self.surface, self.rect)


    def draw2(self, screen, color):
        self.mouseover()

        if self.active:
            if len(self.buttonColor) == 4:
                self.surface.set_alpha(self.buttonColor[3])
            else:
                self.surface.set_alpha(None)
            self.surface.fill(color)
            self.surface.blit(self.txtSurf, self.txtRect)
            screen.blit(self.surface, self.rect)

    """
    Changes the button color temporarily if the mouse is hovering 
    over the button
    """

<<<<<<< HEAD
    def setButtonColor(self, color):
        self.buttonColor = color
=======
    def setButtonColor(self,screen, color):
        self.buttonColor = color
        self.surface.fill(color)
        self.surface.blit(self.txtSurf, self.txtRect)
        screen.blit(self.surface, self.rect)
>>>>>>> e6ef48a0099688202a198d9aded97f7693e2c972

    def getButtonColor(self):
        return self.buttonColor
        
    def mouseover(self):
        self.buttonColor = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.buttonColor = self.mouseoverColor     #changes button color upon mouseover

    def callBack(self):
        if self.active:
            if self.actionArgs == []:
                self.call_back_()
            else:
                self.call_back_(*self.actionArgs)

    def mouseButtonDown(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            buttonColor = self.mouseoverColor
<<<<<<< HEAD
            self.setButtonColor(buttonColor)
=======
            #self.setButtonColor(WHITE)
>>>>>>> e6ef48a0099688202a198d9aded97f7693e2c972
            self.callBack()
