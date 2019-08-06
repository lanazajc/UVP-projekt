#Projekt 2
#Kviz
#Matematičnih 10

import pygame 
import tkinter as tkinter



class Kviz(object):
    def __init__(self):
        self.vprašanje = {q, a}
        self.izbor = ""
        #Meni
        izbori = ("Osnovnosolska raven", "Srednjesolska raven", "Visokosolska raven")
        pass



def osnovnosolska(self):
    pass

def srednjesolska(self):
    pass

def visokosolska(self):
    pass


def main():

    pygame.init()
    sirina = 800
    visina = 600

    zaslon = pygame.display.set_mode((sirina, visina))
    pygame.display.set_caption("Kviz Matematičnih 10")

#da se okence takoj ne zapre oz koda ne izteče do konca
    aktivno = True
    while aktivno:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                aktivno = False

main()

