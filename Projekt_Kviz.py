#Projekt 2
#Kviz
#Matematičnih 10

import pygame 

pygame.init()
sirina = 800
visina = 600
zaslon = pygame.display.set_mode((sirina, visina))

aktivno = True
while aktivno:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            aktivno = False


