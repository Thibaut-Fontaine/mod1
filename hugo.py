#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Tkinter import *
import random

def ft_atoi(astr):
    num = 0
    for c in astr:
        if '0' <= c <= '9':
            num  = num * 10 + ord(c) - ord('0')
    return num

def printPixel(x, y, color, Canevas):
        Canevas.create_rectangle(x, y, x + 2, y + 2, fill=color)

env = []
if (len(sys.argv) == 1):
	raise SystemExit
infile = open(sys.argv[1],"r")
for line in infile:
	new = []
	for char in line:
		if (char != ' ' and char != '\n' and char < '0' or char > '9'):
			raise SystemExit
		new.append(ft_atoi(char))
	env.append(new)
infile.close()
# print env

def rain():
    """ Dessine un cercle de centre (x,y) et de rayon r """

def wave():
    """ Efface le dernier cercle"""

def flood():
    """ Efface tous les cercles"""

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('mod1')

envmin = 2000000000
envmax = 0
# Création d'un widget Canvas (zone graphique)
width = 1200
height = 1200
Canevas = Canvas(Mafenetre,width=width, height=height)
item = Canevas.create_rectangle(0,0,width,height,width=2,fill='black')
pts = [(0, height/2), (width/2, height-(height/3)), (width, height/2), (width/2, (height/3))]
poly = Canevas.create_polygon(pts, width=3, fill='green')
print(item, poly)
# Canevas.create_line(150, 150, 300, 300, fill='red')
for envx in env:
	for envy in envx:
		if envy < envmin:
			envmin = envy
		if envy > envmax:
			envmax = envy
scale = envmax - envmin
idx = -10
for envx in env:
	idx += 10
	idy = -10
	for envy in envx:
		idy += 10
		if envy > scale/3:
			color = 'blue'
		elif envy > (scale/3)*2:
			color = 'cyan'
		else:
			color = 'yellow'
		# Canevas.create_line(idx+490, idy+490, idx+500, idy+500, fill=color)
                # Canevas.create_rectangle(100, 100, 102, 102, fill="red")
		printPixel(50, 60, "blue", Canevas)
                # if idx > 0 and idy > 0:
		# 	Canevas.create_line(idx2+500, idy2+500, idx+500, idy+500, fill=color)

Canevas.pack()

# Création d'un widget Button
BoutonGo = Button(Mafenetre, text ='Pluie', command = rain)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

# Création d'un widget Button
BoutonEffacer = Button(Mafenetre, text ='Vague', command = wave)
BoutonEffacer.pack(side = LEFT, padx = 10, pady = 10)

# Création d'un widget Button
BoutonEffacerTout = Button(Mafenetre, text ='Inondation', command = flood)
BoutonEffacerTout.pack(side = LEFT, padx = 10, pady = 10)

# Création d'un widget Button (bouton Quitter)
BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 10, pady = 10)

Mafenetre.mainloop()
