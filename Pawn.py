import Image
#Pawn class
class Pawn:
    #Possible colors with there corresponding images
    colors = ['yellow', 'green', 'red', 'blue']
    pawnImages = {'yellow': Image.getImage('images\sorryPawnYellow.png'),
                  'green': Image.getImage('images\sorryPawnGreen.png'),
                  'red': Image.getImage('images\sorryPawnRed.png'),
                  'blue': Image.getImage('images\sorryPawnBlue.png')}
    #Creates a pawn with a name, color, player tile name and image
    def __init__(self, name, color, player, tileName):
        self.name = name
        self.color = color
        self.player = player
        self.tileName = tileName    # This is tiles dictionary key to look up tile attributes (found in board class)
        self.image = Pawn.pawnImages[color]

    #Returns the pawn image
    def getPawnImage(self):
        return self.image
    #Displays the pawn image to pygame
    def displayPawn(self, screen, location):
        screen.blit(self.image, location)
