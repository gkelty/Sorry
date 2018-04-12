import pygame
import sys
import pygame.locals as pl
import os.path

pygame.font.init()

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
BLACK = (0, 0, 0)


# Modified from https://github.com/Nearoo/pygame-text-input/blob/master/pygame_textinput.py
# Github, pygame_textinput, posted Nov. 28, 2017, updated Feb. 8, 2018 by user Nearoo
# and from  https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame
# StackOverflow, How to Create a Text Input Box with Pygame, posted Sept. 24, 2017, edited Nov. 29, 2017
# by user skrx
class TextInputBox:
    """
    This class lets the user input a piece of text within a box at a blinking cursor.
    Position within the text can be moved using the arrow-keys. Delete, backspace, home and end work as well.
    """
    def __init__(self, x, y, w, h,
                 fontName="",
                 fontSize=25,
                 antialias=True,
                 textColor=BLACK,
                 cursorColor=BLACK):
        """
        Args:
            fontName: name or path of the font that should be used in text input box. Default is pygame-font
            fontSize: size of the font in the text input box
            antialias: (bool) determines if antialias is used on font
            textColor: color of the text in the text input box
            cursorColor: color of the cursor
        """

        # Box related vars:
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.active = False

        # Text related vars:
        self.antialias = antialias
        self.textColor = textColor
        self.fontSize = fontSize
        self.inputString = ""   # Inputted text
        if not os.path.isfile(fontName): fontName = pygame.font.match_font(fontName)
        self.fontObject = pygame.font.Font(fontName, fontSize)

        # Text-surface will be created during the first update call:
        self.surface = self.fontObject.render(self.inputString, True, self.color)
        self.surface.set_alpha(0)

        # Cursor vars:
        self.cursorSurface = pygame.Surface((int(self.fontSize / 20 + 1), self.fontSize))
        self.cursorSurface.fill(cursorColor)
        self.cursorPosition = 0  # Inside text
        self.cursorVisible = True  # Switches every self.cursorSwitchMs ms
        self.cursorSwitchMs = 800  # /|\
        self.cursorMsCounter = 0

        self.clock = pygame.time.Clock()

    """
    Blits the text input box to screen.
    """
    def draw(self, screen):
        # Blit the text.
        screen.blit(self.surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    """
    Updates whether the box is active, checks for a mouseclick in the box,
    and handles key events      
    """
    def updateEvent(self, event):
        self.clock.tick()
        # Change the current color of the input box.
        if self.active:
            self.color = COLOR_ACTIVE
            self.cursorVisible = True
        else:
            self.color = COLOR_INACTIVE
            self.cursorVisible = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False

        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pl.K_BACKSPACE:
                    self.inputString = self.inputString[:max(self.cursorPosition - 1, 0)] + \
                                        self.inputString[self.cursorPosition:]

                    # Subtract one from cursorPosition, but do not go below zero:
                    self.cursorPosition = max(self.cursorPosition - 1, 0)
                elif event.key == pl.K_DELETE:
                    self.inputString = self.inputString[:self.cursorPosition] + \
                                        self.inputString[self.cursorPosition + 1:]

                elif event.key == pl.K_RETURN:
                        self.active = False

                elif event.key == pl.K_RIGHT:
                    # Add one to cursorPosition, but do not exceed len(inputString)
                    self.cursorPosition = min(self.cursorPosition + 1, len(self.inputString))

                elif event.key == pl.K_LEFT:
                    # Subtract one from cursorPosition, but do not go below zero:
                    self.cursorPosition = max(self.cursorPosition - 1, 0)

                elif event.key == pl.K_END:
                    self.cursorPosition = len(self.inputString)

                elif event.key == pl.K_HOME:
                    self.cursorPosition = 0

                else:
                    # If no special key is pressed, add unicode of key to inputString
                    self.inputString = self.inputString[:self.cursorPosition] + \
                                        event.unicode + \
                                        self.inputString[self.cursorPosition:]
                    self.cursorPosition += len(event.unicode)

        return False

    def updateDisplay(self):
        # Resize the box if the text is too long.
        width = max(200, self.surface.get_width() + 10)
        self.rect.w = width

        # Rerender text surface:
        self.surface = self.fontObject.render(self.inputString, self.antialias, self.textColor)

        # Update self.cursorVisible
        if self.active:
            self.cursorMsCounter += self.clock.get_time()
            if self.cursorMsCounter >= self.cursorSwitchMs:
                self.cursorMsCounter %= self.cursorSwitchMs
                self.cursorVisible = not self.cursorVisible

        if self.cursorVisible:
            cursorYPos = self.fontObject.size(self.inputString[:self.cursorPosition])[0]
            # Without this, the cursor is invisible when self.cursorPosition > 0:
            if self.cursorPosition > 0:
                cursorYPos -= self.cursorSurface.get_width()
            self.surface.blit(self.cursorSurface, (cursorYPos, 0))


    def getSurface(self):
        return self.surface

    def getText(self):
        text = self.inputString
        return text

    def getCursorPosition(self):
        return self.cursorPosition

    def setTextColor(self, color):
        self.textColor = color

    def setCursorColor(self, color):
        self.cursorSurface.fill(color)

    def clearText(self):
        self.inputString = ""
