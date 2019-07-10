# SNAKE GAME
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass
    
    def move(self, dirnx, dirny):
        pass

    def draw(self, surface):
        pass

class snake(object):
    
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

def draw_grid(w, rows, surface):
    size_between = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + size_between
        y = y + size_between

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w)) # navpične črte 

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

