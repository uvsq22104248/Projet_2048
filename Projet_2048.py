#Projet_2048#

import tkinter as tk
import random as rd

HAUTEUR1 = 700
LARGEUR1 = 1000

HAUTEUR2 = 700
LARGEUR2 = 700

racine = tk.Tk()
canvas = tk.Canvas(racine, bg = "orange", height = HAUTEUR1, width = LARGEUR1)


button_play = tk.Button(racine, text = "Play", bg = "yellow", height = 2, width = 10)
button_play.place(x=825, y=100)

button_left = tk.Button(racine, text = "Left", bg = "yellow", height = 2, width = 10)
button_left.place(x=775, y=250)

button_right = tk.Button(racine, text = "Right", bg = "yellow", height = 2, width = 10)
button_right.place(x=875, y=250)

button_up = tk.Button(racine, text = "Up", bg = "yellow", height = 2, width = 10)
button_up.place(x=825, y=200)

button_down = tk.Button(racine, text = "Down", bg = "yellow", height = 2, width = 10)
button_down.place(x=825, y=300)

button_exit = tk.Button(racine, text = "Exit", bg = "yellow", height = 2, width = 10)
button_exit.place(x=825, y=400)

button_save = tk.Button(racine, text = "Save", bg = "yellow", height = 2, width = 10)
button_save.place(x=775, y=500)

button_load = tk.Button(racine, text = "Load", bg = "yellow", height = 2, width = 10)
button_load.place(x=875, y=500)

canvas.create_rectangle((0, 0), (LARGEUR2, HAUTEUR2), fill="grey")

for i in range(0,4) :
    canvas.create_line((i*175, 0), (i*175, HAUTEUR2), fill="black", width=3)
    canvas.create_line((0, i*175), (LARGEUR2, i*175), fill="black", width=3)


canvas.grid()
racine.mainloop()