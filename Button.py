import pygame
import sys
pygame.init()

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((120, 100))

#Modified from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/
#Python programming tutorial, Buttons and Sliders in Pygame, posted Feb. 19, 2017 by user DK3250
class Button():
    def __init__(self, txt, location, action, bg = WHITE, fg = BLACK, size = (80, 30), font_name = "Segoe Print", font_size = 16):
        self = self
        self.color = bg #the static (normal) color
        self.bg = bg #the actual background color, can change on mouseover
        self.fg = fg #text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center = [s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center = location)

        self.call_back_ = action

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GREY #mouseover color



    def call_back(self):
        self.call_back_()

        
    def mousebuttondown(buttons):
        pos = pygame.mouse.get_pos()
        for button in buttons:
            if button.rect.collidepoint(pos):
                button.call_back()   



