#Projekt 2
#Kviz
#Matematičnih 10

import pygame 
import tkinter as tkinter
import menu
from tkinter import messagebox
import time
import random

pygame.init()
sirina = 800
visina = 600

zaslon = pygame.display.set_mode((sirina, visina))
pygame.display.set_caption("Kviz Matematičnih 10")

clock = pygame.time.Clock()

odgovori = tuple()

def igra():
    zaslon.fill((255, 255, 255))
    naslednje_vprasanje()
    
def prvo_vpr():
        zaslon.fill((255, 255, 255))
        vpr = random.choice(list(vpr_odg.keys()))
        prikazi_vprasanje(vpr)


def dodaj_DA():
        global odgovori
        odgovori = odgovori + ("DA", )
        if len(odgovori) < 5:
            naslednje_vprasanje()
            print(odgovori)
        
        
def dodaj_NE():
        global odgovori
        odgovori = odgovori + ("NE", )
        if len(odgovori) < 5: 
             naslednje_vprasanje()
             print(odgovori)

def naslednje_vprasanje():
        zaslon.fill((255, 255, 255))
        vpr = random.choice(list(vpr_odg.keys()))
        prikazi_vprasanje(vpr)

        

def rezultat(tocke):
        prikazi_vprasanje("Čestitamo! Dosegli ste {} točk".format(tocke))

def besedilo_povrsina_kvadrat_vprasanja(tekst, pisava):
    povrsina_besedila = pisava.render(tekst, True, (0,255,127))
    return povrsina_besedila, povrsina_besedila.get_rect()

def prikazi_vprasanje(vprasanja=""):
    zaslon.fill((255, 255, 255))
    pisava = pygame.font.Font('freesansbold.ttf', 30)
    besedilo_povrsina, besedilo_kvadrat = besedilo_povrsina_kvadrat_vprasanja(vprasanja, pisava)
    besedilo_kvadrat.center = ((sirina / 2), (visina / 3))
    zaslon.blit(besedilo_povrsina, besedilo_kvadrat)

    tipke("DA", 250, 400, 100, 50, (142, 142, 142), dodaj_DA )
    tipke("NE", 500, 400, 100, 50, (142, 142, 142), dodaj_NE )

    pygame.display.update()
    pygame.time.delay(30)
    clock.tick(15)
    

def preveri_odgovor():
    pass
    #preveri ogovor, zabelezi score in zabelezi vprasanje

def tipke(tekst, x, y, sirina_tipke, visina_tipke, barva, dogodek=None):
    clicked = False
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
    pozicija_miske = pygame.mouse.get_pos()
    #klik = pygame.mouse.get_pressed()
    #print(klik)
    pygame.draw.rect(zaslon, barva, (x, y, sirina_tipke, visina_tipke))
    pisava_za_tipke = pygame.font.Font('freesansbold.ttf', 20)
    besedilo_povrsina, besedilo_kvadrat = besedilo_povrsina_kvadrat_tipke(tekst, pisava_za_tipke)
    besedilo_kvadrat.center = ((x + (sirina_tipke / 2)), (y + (visina_tipke/ 2)))
    zaslon.blit(besedilo_povrsina, besedilo_kvadrat)
    if x < pozicija_miske[0] < x + sirina_tipke and y < pozicija_miske[1] < y + visina_tipke:
        if clicked and dogodek != None:
            dogodek()

def besedilo_povrsina_kvadrat_tipke(tekst, pisava):
        povrsina_besedila = pisava.render(tekst, True, (40,40,40))
        return povrsina_besedila, povrsina_besedila.get_rect()

def izhod():
        pygame.quit()
        #quit()

def besedilo_povrsina_kvadrat_pozdrav(tekst, pisava):
    povrsina_besedila = pisava.render(tekst, True, (255,255,255))
    return povrsina_besedila, povrsina_besedila.get_rect()

def zacetni_pozdrav(tekst):
    pisava = pygame.font.Font('freesansbold.ttf', 30)
    besedilo_povrsina, besedilo_kvadrat = besedilo_povrsina_kvadrat_pozdrav(tekst, pisava)
    besedilo_kvadrat.center = ((sirina / 2), (visina / 2))
    zaslon.blit(besedilo_povrsina, besedilo_kvadrat)

    #tipke("Začni!", 250, 270, 100, 50, (142, 142, 142), igra)
    #tipke("Izhod", 400, 270, 100, 50, (142, 142, 142), izhod)

    pygame.display.update()
    pygame.time.delay(2000)
    clock.tick(15)

    #prikazi_vprasanje("lala")



    
    

vpr_odg = {"Glavno mesto Slovenije je Ljubljana.": "DA", "1 + 1 = 2": "DA", "15 / 3 = 5": "DA", "Jabolka so modra.": "NE"}

def zacetni_meni():
    prikaz = True
    while prikaz:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        zacetni_pozdrav("Pripravljeni...")
        prikazi_vprasanje("lala")
        

        

zacetni_meni()
pygame.quit()
quit()

