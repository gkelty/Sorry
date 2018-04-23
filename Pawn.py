import Image

class Pawn:
    colors = ['yellow', 'green', 'red', 'blue']
    pawnImages = {'yellow': Image.getImage('images\sorryPawnYellow.png'),
                  'green': Image.getImage('images\sorryPawnGreen.png'),
                  'red': Image.getImage('images\sorryPawnRed.png'),
                  'blue': Image.getImage('images\sorryPawnBlue.png')}

    def __init__(self, name, color, player, tileName):
        self.name = name
        self.color = color
        self.player = player
        self.tileName = tileName    # This is tiles dictionary key to look up tile attributes (found in board class)
        self.image = Pawn.pawnImages[color]


    def getPawnImage(self):
        return self.image

    def displayPawn(self, screen, location):
        screen.blit(self.image, location)
