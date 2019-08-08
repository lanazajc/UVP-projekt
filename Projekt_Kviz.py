#Projekt 2
#Kviz
#Matematičnih 10

import pygame 
import tkinter as tkinter
import menu
from tkinter import messagebox
import time

sirina = 800
visina = 600

    
zaslon = pygame.display.set_mode((sirina, visina))
pygame.display.set_caption("Kviz Matematičnih 10")
    
    


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






def igra():
    tocke = 0
    odgovorjenih = 0
    while odgovorjenih < 7:
        for vprasanje iz random uprasanje: 
            prikazi_vprasanje(vprasanja)
            for event in mousedown bla bla:
                ce gumb zadane okno 
                odgovorjenih += 1
                preveri_odgovor()
                if odgovor je true:
                        tocke += 1
    rezultat()

def rezultat():
        zacetni_pozdrav("Čestitamo! Dosegli ste {} točk".format(tocke))




    #po tem ko zapres prvo okence

    def prikazi_vprasanje(vprasanja):
        pisava = pygame.font.Font('freesansbold.ttf', 30)
        besedilo_povrsina, besedilo_kvadrat = besedilo_povrsina_kvadrat(tekst, pisava)
        besedilo_kvadrat.center = ((sirina / 2), (visina / 3))
        zaslon.blit(besedilo_povrsina, besedilo_kvadrat)
        pygame.display.update()
    

def preveri_odgovor():
    pass
    #preveri ogovor, zabelezi score in zabelezi vprasanje


def besedilo_povrsina_kvadrat(tekst, pisava):
    povrsina_besedila = pisava.render(tekst, True, (255,255,255))
    return povrsina_besedila, povrsina_besedila.get_rect()


def zacetni_pozdrav(tekst):
    pisava = pygame.font.Font('freesansbold.ttf', 30)
    besedilo_povrsina, besedilo_kvadrat = besedilo_povrsina_kvadrat(tekst, pisava)
    besedilo_kvadrat.center = ((sirina / 2), (visina / 3))
    zaslon.blit(besedilo_povrsina, besedilo_kvadrat)
    pygame.display.update()
    time.sleep(7)
    igra()


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
        zacetni_pozdrav("Pripravljeni...")
        igra()

        

main()

