#Projekt 2
#Kviz
#Matematičnih 10

import pygame 
import tkinter as tkinter
import menu
from tkinter import messagebox

def zacetni_meni():
    prikaz = True
    while prikaz:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        zaslon.fill((0, 255, 0))
        pygame.display.update()

def prvo_obvestilo(naslov, vsebina):
    okence = tkinter.Tk()
    okence.withdraw()
    messagebox.showinfo("Pozdravljeni!", "Kviz se začenja!")
    okence.mainloop()




class Kviz(object):
    def __init__(self):
        pass
        
        
def zacni_igro():
    pass
    #po tem ko zapres prvo okence

def nastavi_vprasanje():
    pass
    #vedno znova 

def preveri_odgovor():
    pass
    #preveri ogovor, zabelezi score in zabelezi vprasanje



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
        prvo_obvestilo("ns", "ls")
        zacni_igro
        

main()

