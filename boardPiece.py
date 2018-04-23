#Set up stuff
import pygame
import sys
pygame.init()
#Delete this later  in for testing right now
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((1300, 650))
#Board piece class, buttons that will numbered incrementally in gameboard class
class boardPiece():
    def __init__(self, txt = "Test", location = "0,0", action = "", bg = WHITE, fg = BLACK, size = (35, 35), font_name = "Segoe Print", font_size = 16):
        self.color = bg #the static (normal) color
        self.bg = bg #the actual background color, can change on mouseover
        self.fg = fg #text color
        self.size = size#Size
        #Font Stuff
        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        if(self.txt=="Base"):
            self.base = True
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

    #Def mad inefficient but good enough for time being
    def createBoard():
        #16 each side
        #5 up after 3 6th is home
        #5 in is base
        buttons = []
        #Start creating in bottom right corner
        startCordx = 1285
        startCordy = 630
        #Yellow squares on bottom
        for i in range(0,4):
            if (i==0):
                incrementValx = -40
                incrementBasey = -40
                incrementBasex = 0
                incrementValy = 0
            elif(i==1):
                incrementValx = 0
                incrementBasey = 0
                incrementBasex = 40
                incrementValy = -40
            elif(i==2):
                incrementValx = 40
                incrementBasey = 40
                incrementBasex = 0
                incrementValy = 0
            elif(i==3):
                incrementValx = 0
                incrementBasey = 0
                incrementBasex = -40
                incrementValy = 40
            for k in range(0,16):
                # CreateBase
                if (k == 2):
                    saveCordy = startCordy
                    saveCordx = startCordx
                    for k in range(0, 6):
                        saveCordy += incrementBasey
                        saveCordx += incrementBasex
                        buttonId = boardPiece("Base", (saveCordx, saveCordy), my_fantastic_function)
                        buttons.append(buttonId)

                # Start
                if (k == 4):
                    saveCordy = startCordy
                    saveCordx = startCordx
                    saveCordy += incrementBasey
                    saveCordx+=incrementBasex
                    buttonId = boardPiece("Start", (startCordx, saveCordy), my_fantastic_function)
                    buttons.append(buttonId)
                # Create normal pieces
                else:
                    startCordx += incrementValx
                    startCordy +=incrementValy
                    buttonId = boardPiece("Great!", (startCordx, startCordy), my_fantastic_function)
                    buttons.append(buttonId)
        #for i in range(0,16):
        displayBoard(buttons)
    def displayBoard(buttons):
        for button in buttons:
            button.draw()
#     button_01 = boardPiece("Great!",(60, 30),my_fantastic_function)
#     button_02 = boardPiece("Fantastic!", (220, 70), my_fantastic_function, bg=(50, 200, 20))
#     buttonMovementTest = boardPiece("Fantastic!", (200, 80),my_fantastic_function,bg=(50, 200, 20), size=(20, 20))
#     #buttons = createBoard()
#     #buttons.append(buttonMovementTest)
#     while True:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 print(event.pos)
#                 mousebuttondown(buttons)
#
#         for button in buttons:
#             button.draw()
#
#         pygame.display.flip()
#         pygame.time.wait(100)
#
# def main():
#     test()
# main()
