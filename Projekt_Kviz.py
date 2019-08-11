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
clock = pygame.time.Clock

def zacetni_meni():
    prikaz = True
    while prikaz:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        zaslon.fill((0, 255, 0))
        pygame.display.update()

def igra():
    
    tocke = 0
    odgovorjenih = 0
    while odgovorjenih < 3:
        prikazi_vprasanje("Koliko je ura?")
        odgovorjenih += 1
        tocke += 1
    rezultat(tocke)

def rezultat(tocke):
        prikazi_vprasanje("Čestitamo! Dosegli ste {} točk".format(tocke))

def besedilo_povrsina_kvadrat_vprasanja(tekst, pisava):
    povrsina_besedila = pisava.render(tekst, True, (0,255,127))
    return povrsina_besedila, povrsina_besedila.get_rect()

def prikazi_vprasanje(vprasanja):
    pisava = pygame.font.Font('freesansbold.ttf', 30)
    besedilo_povrsina, besedilo_kvadrat = besedilo_povrsina_kvadrat_vprasanja(vprasanja, pisava)
    besedilo_kvadrat.center = ((sirina / 2), (visina / 3))
    zaslon.blit(besedilo_povrsina, besedilo_kvadrat)
    pygame.display.update()

    pygame.time.delay(5000)
    
    zaslon.fill((255, 255, 255))
    











def preveri_odgovor():
    pass
    #preveri ogovor, zabelezi score in zabelezi vprasanje



def besedilo_povrsina_kvadrat_pozdrav(tekst, pisava):
    povrsina_besedila = pisava.render(tekst, True, (255,255,255))
    return povrsina_besedila, povrsina_besedila.get_rect()


def zacetni_pozdrav(tekst):
    pisava = pygame.font.Font('freesansbold.ttf', 30)
    besedilo_povrsina, besedilo_kvadrat = besedilo_povrsina_kvadrat_pozdrav(tekst, pisava)
    besedilo_kvadrat.center = ((sirina / 2), (visina / 3))
    zaslon.blit(besedilo_povrsina, besedilo_kvadrat)
    pygame.display.update()
    
    pygame.time.delay(5000)

    zaslon.fill((255, 255, 255))
    


def prazno_okno():
    zaslon.fill((0,0,0))



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
        zacetni_pozdrav("Juhu")
        igra()
        
        
        

        

main()

