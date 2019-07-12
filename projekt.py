# SNAKE GAME
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1 # da se kača začne takoj premikati
        self.dirny = 0
        self.color = color
    
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        distance = self.w // self.rows
        i = self.pos[0] # vrstica 
        j = self.pos[1] # stolpec

        pygame.draw.rect(surface, self.color, (i * distance + 1, j * distance + 1, distance -2, distance -2))
        # +1, -2 je zato, da kvadrat ne pokrije črt belih igralne plošče oz. da ostane znotrj polja

        # Ne nujna koda ta oči kače:
        if eyes:
            centre = distance // 2
            radius = 3
            circle_middle = (i * distance + centre - radius, j * distance + 8)
            circle_middle2 = (i * distance + distance - radius * 2, j * distance + 8)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius) # surface, barva (črna), pozicija, radij
            pygame.draw.circle(surface, (0, 0 ,0), circle_middle2, radius)
            
        

class snake(object):
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
                pygame.quit() # program ne deluje pravilno

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
        self.head = cube(pos)
        self.body = []
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def add_cube(self):   # dodajanje nove kocke kači, najprej moramo ugotovit kje se nahaja zadnji cube kače, da dodamo na konec kače
        tail = self.body[-1] 
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0: #če se premikamo desno
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1]))) # dodamo cube v isto vrstico v en stolpec pred zadnjim cubom kače
        elif dx == -1 and dy == 0: # če se premikamo levo 
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1]))) # dodamo en stolpec desno od zadnjega cuba
        elif dx == 0 and dy == 1: # če se premikamo dol
            self.body.append((cube(tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1: # če se pomikamo gor 
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0: # prvi index je glava kače 
                c.draw(surface, True) # true doda oči kači?
            else: 
                c.draw(surface) # ostale cube nariše normalno

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
    global rows, width, s, snack
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()

def random_snack(rows, items):
    positions = items.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0: #prepirčamo se da pozicija snacka ni na kači
            continue #če se random pozicija snacka ujema s pozicijo telesa kače, potem išči nov (x, y)
        else: #sicer vrni (x, y)
            break
    
    return (x, y)


def message_box(subject, content):
    root = tk.Tk() # novo okence
    root.attributes("-topmost", True) # Okence bo vedno na vrhu vseh okencev
    root.withdraw()
    messagebox.showinfo(subject, content)
    try: 
        root.destroy()
    except:
        pass


def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width)) #naredi začetno okence
    s = snake((255, 0, 0), (10,10))
    snack = cube(random_snack(rows, s), color=(0, 255, 0))
    flag = True

    clock = pygame.time.Clock()
    while flag: 
        pygame.time.delay(50) #upočasni program, manjša številka hitreje gre
        clock.tick(10) # manjša številka, počasneje gre
        s.move()
        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack = cube(random_snack(rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):
                print ('Score: ', len(s.body))
                message_box('You Lost!', 'Play Again')
                message_box()
                s.reset((10, 10))
                break

        redraw_window(win)
        

main()