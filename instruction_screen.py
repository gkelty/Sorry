import pygame
import sys
import fileinput

pygame.init()
pygame.font.init()


WHITE = (240, 248, 255)
PURPLE = (153, 102, 204)
SCREENSIZE = [1280, 720]

screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption('Instructions test')

clock = pygame.time.Clock()
tickspeed = 60
running = True

font = pygame.font.Font(None, 36)


f=open("instructions.txt")
for line in f:

    text = font.render(line, True, WHITE)

    screen.blit(text, text.get_rect())

    print(line)




# while running:
#     screen.fill(WHITE)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit('Program stopped')
#
#
#     draw_instructions()
#     pygame.display.update()


