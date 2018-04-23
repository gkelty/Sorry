import pygame
import random

# color
color = ["red","yellow","Green","Blue"]


class Player:

     def _init_(self, color, mean, smart,human):

         self.color = color
         self.mean = mean
         self.smart = smart
         self.human = human

     def getColor(self):
         return self.color

     def getMean(self):
         return self.mean

     def getSmart(self):
         return self.smart

     def getHuman(self):
         return self.human



