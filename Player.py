import pygame
import random

#PLayer class, not really used fully any more

class Player:

    def __init__(self,id=0,color =0 , mean = False, smart = False,):

        self.color = color
        self.mean = mean
        self.smart = smart
        self.id = id
        self.pawns = []
    def getColor(self):
        return self.color
    def initialSetup(self,intel,behavior):

        self.smart = intel
        self.mean = behavior

    def getMean(self):
        return self.mean

    def getSmart(self):
        return self.smart

    def getId(self):
        return self.id

    def setMean(self,mean):
        self.mean = mean
    def setColor(self,color):
        self.color = color



