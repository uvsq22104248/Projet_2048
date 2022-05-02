#Projet_2048#

import tkinter as tk
import random as rd

HAUTEUR = 700
LARGEUR = 700

racine = tk.Tk()
canvas = tk.Canvas(racine, bg = "grey", height = HAUTEUR, width = LARGEUR)

button_play = tk.Button(racine, text = "Play", bg = "orange", height = 2, width = 10)
button_play.grid(row = 0, column = 0)

for i in range(0,4) :
    canvas.create_line((i*175, 0), (i*175, HAUTEUR), fill="black", width=5)
    canvas.create_line((0, i*175), (LARGEUR, i*175), fill="black", width=5)


canvas.grid()
racine.mainloop()