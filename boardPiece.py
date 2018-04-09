#Set up stuff
import pygame
import sys
pygame.init()
#Delete this later  in for testing right now
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((600, 500))
#Board piece class, buttons that will numbered incrementally in gameboard class
class boardPiece():
    def __init__(self, txt, location, action, bg = WHITE, fg = BLACK, size = (80, 30), font_name = "Segoe Print", font_size = 16):
        self.color = bg #the static (normal) color
        self.bg = bg #the actual background color, can change on mouseover
        self.fg = fg #text color
        self.size = size#Size
        #Font Stuff
        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center = [s//2 for s in self.size])
        #Setting the size and location
        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center = location)
        #Function button calls on click
        self.call_back_ = action
    #Set location class
    #ONLY IN FOR TESTING DELETE THIS
    def setLocation(self,loc):
        self.location = loc
        self.rect = self.surface.get_rect(center=self.location)
        screen.fill((0, 0, 0))
        pygame.display.update()
    #Drawing stuff
    def draw(self):
        self.mouseover()
        pygame.display.flip()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)
    #Highlighting on mouseover
    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GREY #mouseover color
    #Call back method
    def call_back(self):
        self.call_back_()
def test():
    def mousebuttondown(buttons):
        pos = pygame.mouse.get_pos()
        for button in buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

    def my_fantastic_function():
        print("Fantastic! " * 5)
        buttonMovementTest.setLocation(event.pos)

    button_01 = boardPiece("Great!",(60, 30),my_fantastic_function)
    button_02 = boardPiece("Fantastic!", (220, 70), my_fantastic_function, bg=(50, 200, 20))
    buttonMovementTest = boardPiece("Fantastic!", (200, 80),my_fantastic_function,bg=(50, 200, 20), size=(20, 20))
    buttons = [button_01, button_02, buttonMovementTest]
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                mousebuttondown(buttons)

        for button in buttons:
            button.draw()

        pygame.display.flip()
        pygame.time.wait(100)
def main():
    test()
main()