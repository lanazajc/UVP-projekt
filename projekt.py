# SNAKE GAME
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class Cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass
    
    def move(self, dirnx, dirny):
        pass

    def draw(self, surface):
        pass

class Snake(object):
    body = []
    turns = {} # slovar, dodamo mu trenutno pozicijo glave, kjer mora telo obrnit
    
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos) # glava kače je kvadrat v dani poziciji
        self.body.append(self.head) # telesu dodamo glavo (body je seznam, glava na začetku)
        self.dirnx = 0
        self.dirny = 1 

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()  # ne zapre se
                pygame.quit() # ne zapre okenca 

            keys = pygame.key.get_pressed() # seznam vseh tipk z True Ali False (ali je bilo kliknjeno)

            for key in keys:# čez keys preletimo kater od 4 tipk se je pritisnila (je TRUE)
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0 
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] # slovarju dodamo ključ trenutna poz glave, vrednst je pozicija

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]


        for i, c in enumerate(self.body): # indeks, cube v body
            p = c.pos[:] # p je pozicija za vsak cube 
            if p in self.turns: # pogledamo če je p v slovarju obratov, če je:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1: # če smo na zadnji cube, bomo odstranili pravilo za obrat 
                    self.turns.pop(p)

            else: 
                if c.dirnx == -1 and c.pos[0] <= 0:  # premikamo se levo, pozicija je <=0
                    c.pos = (c.rows - 1, c.pos[1]) # spremenimo pozicijo. gremo na desno stran  , y ostane isti
                                                   # c.rows -1 : če mamo 20 stolpcev nas postavi na 19indeks tj. na prvi okenček esno pri istem y ( v isti vrstici)
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1: # premikamo se desno, poz. je (x, y), pos[0] = x če je več kot "19" 
                    c.pos = (0, c.pos[1])  # prestavimo na (0, y isti (vrstica ista))

                elif c.dirny == 1 and c.pos[1] >= c.rows - 1: # premikamo se dol, če y pozicija večja ali enaka "19"
                    c.pos = (c.pos[0], 0) # nas premakne gor na vrh ekrana ( očitno številči od zgoraj na vzdol)

                elif c.dirny == -1 and c.pos[1] <= 0: # premikamo se gor, če je y pozicija manjša ali enaka nič
                    c.pos = (c.pos[0], c.rows -1) # prestavi nas na dno igralne plošče, x ostaja isti 
                
                else:  # če se ne zgoodi nič od tega naj cube nadaljuje svojo pot v isti smeri
                    c.move(c.dirnx, c.dirny)
            


    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0: # prvi index je glava kače 
                c.draw(surface, True) # true doda oči kači?
            else: 
                c.draw(surface)

def draw_grid(w, rows, surface):
    size_between = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + size_between
        y = y + size_between

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w)) # navpične črte # barva, začetna točka, končna točka 
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y)) # vodoravne črte


def redraw_window(surface):
    global rows, width
    surface.fill((0, 0, 0))
    draw_grid(width, rows, surface)
    pygame.display.update()

def random_snack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width)) #naredi začetno okence
    s = snake((255, 0, 0), (10,10))
    flag = True

    clock = pygame.time.Clock()
    while flag: 
        pygame.time.delay(50) #upočasni program, manjša številka hitreje gre
        clock.tick(10) # manjša številka, počasneje gre
        redraw_window(win)

main()
pygame.quit() # tut ne pomaga