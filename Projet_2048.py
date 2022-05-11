#Projet_2048#

from re import L
import tkinter as tk
import random as rd

HAUTEUR1 = 700
LARGEUR1 = 1000

HAUTEUR2 = 700
LARGEUR2 = 700

racine = tk.Tk()
canvas = tk.Canvas(racine, bg = "orange", height = HAUTEUR1, width = LARGEUR1)
racine.title("2048")

canvas.create_rectangle((0, 0), (LARGEUR2, HAUTEUR2), fill="grey")
for i in range(1,4) :
    canvas.create_line((i*175, 0), (i*175, HAUTEUR2), fill="black", width=3)
    canvas.create_line((0, i*175), (LARGEUR2, i*175), fill="black", width=3)


matrice = [[0] * 4 for i in range(4)]

def start_game() :
    matrice = [[0] * 4 for i in range(4)]
    p = rd.randint(1, 10)
    pi = rd.randint(0,3)
    pj = rd.randint(0,3)
    
    for i in range(4) :
        for j in range(4) :
            
            if p == 1 :
                matrice[pi][pj] = 4
                r = canvas.create_rectangle((175*pi, 175*pj), (175*pi + 175, 175*pj + 175), fill="yellow")
                t = canvas.create_text(175*pi + 175/2, 175*pj + 175/2, fill="black", font="helvetica, 40", text="4")
                   
            else :
                matrice[pi][pj] = 2
                r = canvas.create_rectangle((175*pi, 175*pj), (175*pi + 175, 175*pj + 175), fill="yellow")
                t = canvas.create_text(175*pi + 175/2, 175*pj + 175/2, fill="black", font="helvetica, 40", text="2")
                
    print(matrice)
    


def tuiles_left() :
    for i in range(4) :
        for j in range(4) :
            if matrice[i][j] != 0 :
                l = matrice[i][0]
                matrice[i][0] = l
                matrice[i][j] = 0
    print(matrice)
    


def tuiles_right() :
    x = 2


def tuiles_up() :
    x = 2


def tuiles_down() :
    x = 2


def end_game() :
    x = 2


def save_game() :
    fic = open("fichier.txt","w")
    for i in range (4):
        for j in range(4):
            fic.write(str(matrice[i][j]))
    fic.close()


def load_game() :
    fic = open("fichier.tkt","r")
    print([fic])
    fic.close()

    
button_play = tk.Button(racine, text = "Play", bg = "yellow", height = 2, width = 10, command = start_game)
button_play.place(x=825, y=100)

button_left = tk.Button(racine, text = "Left", bg = "yellow", height = 2, width = 10, command = tuiles_left)
button_left.place(x=775, y=250)

button_right = tk.Button(racine, text = "Right", bg = "yellow", height = 2, width = 10, command = tuiles_right)
button_right.place(x=875, y=250)

button_up = tk.Button(racine, text = "Up", bg = "yellow", height = 2, width = 10, command = tuiles_up)
button_up.place(x=825, y=200)

button_down = tk.Button(racine, text = "Down", bg = "yellow", height = 2, width = 10, command = tuiles_down)
button_down.place(x=825, y=300)

button_exit = tk.Button(racine, text = "Exit", bg = "yellow", height = 2, width = 10, command = end_game)
button_exit.place(x=825, y=400)

button_save = tk.Button(racine, text = "Save", bg = "yellow", height = 2, width = 10, command = save_game)
button_save.place(x=775, y=500)

button_load = tk.Button(racine, text = "Load", bg = "yellow", height = 2, width = 10, command = load_game)
button_load.place(x=875, y=500)


start_game()
#tuiles_left()
#tuiles_right()
#tuiles_up()
#tuiles_down()
#end_game()
#save_game()
#load_game()
canvas.grid()
racine.mainloop()