#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import sys
#
# for av in sys.argv:
# 	infile = open(av,"r")
# 	for line in infile:
# 		print line
# 	infile.close()

from Tkinter import *
import random

def rain():
    """ Dessine un cercle de centre (x,y) et de rayon r """
    # x = random.randint(0,Largeur)
    # y = random.randint(0,Hauteur)
    # r = 10
	#
    # # on dessine un cercle dans la zone graphique
    # item = Canevas.create_oval(x-r, y-r, x+r, y+r, outline='black', fill='black')
	#
    # print("Création du cercle (item" , item ,")")
    # # affichage de tous les items de Canevas
    # print(Canevas.find_all())

def wave():
    """ Efface le dernier cercle"""
    # if len(Canevas.find_all()) > 1:
    #     item = Canevas.find_all()[-1]
    #     # on efface le cercle
    #     Canevas.delete(item)
	#
    #     print("Suppression du cercle (item" , item ,")")
    #     # affichage de tous les items de Canevas
    #     print(Canevas.find_all())

def flood():
    """ Efface tous les cercles"""
    # while len(Canevas.find_all()) > 1:
    #     Undo()


# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('mod1')

# Image de fond
# photo = PhotoImage(file="black.jpg")

# Création d'un widget Canvas (zone graphique)
Largeur = 1000
Hauteur = 1000
Canevas = Canvas(Mafenetre,width=Largeur, height=Hauteur)
# item = Canevas.create_image(0,0,anchor=NW, image=photo)
item = Canevas.create_rectangle(0,0,1000,1000,width=2,fill='black')
poly = Canevas.create_polygon([160,45,175,20,190,45,175,70 ], width =2, fill = 'blue')
print("Image de fond (item",item,")")
print(poly)
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
