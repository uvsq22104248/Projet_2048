#Projet_2048#

import tkinter as tk
import random as rd

HAUTEUR1 = 700
LARGEUR1 = 1000

HAUTEUR2 = 700
LARGEUR2 = 700

racine = tk.Tk()
canvas = tk.Canvas(racine, bg = "orange", height = HAUTEUR1, width = LARGEUR1)
racine.title("2048")

#génère matrice 4*4#
matrice = [[0] * 4 for i in range(4)]

def start_game() :

    canvas.delete("all")

    #créé rectangle#
    canvas.create_rectangle((0, 0), (LARGEUR2, HAUTEUR2), fill="grey")

    #créé quadrillage avec 3 lignes verticales et horizontales#
    for i in range(1,4) :
        canvas.create_line((i*175, 0), (i*175, HAUTEUR2), fill="black", width=3)
        canvas.create_line((0, i*175), (LARGEUR2, i*175), fill="black", width=3)

    matrice = [[0] * 4 for i in range(4)]

    #génère 3 chiffres au hazard#
    #pour la probabilité d'un 2 ou un 4#
    p = rd.randint(1, 10)
    #pour la probabilité de placement de la tuile dans le quadrillage#
    pi = rd.randint(0,3)
    pj = rd.randint(0,3)
    
    for i in range(4) :
        for j in range(4) :
            
            if p == 1 :
                matrice[pi][pj] = 4
                canvas.create_rectangle((175*pi, 175*pj), (175*pi + 175, 175*pj + 175), fill="yellow")
                canvas.create_text(175*pi + 175/2, 175*pj + 175/2, fill="black", font="helvetica, 40", text="4")
                   
            else :
                matrice[pi][pj] = 2
                canvas.create_rectangle((175*pi, 175*pj), (175*pi + 175, 175*pj + 175), fill="yellow")
                canvas.create_text(175*pi + 175/2, 175*pj + 175/2, fill="black", font="helvetica, 40", text="2")
                
    print(matrice)
    


def tuiles_left() :
    for i in range(4) :
        for j in range(4) :
            #quand tuile pas égale à 0#
            if matrice[i][j] != 0 :
                #tuile se décale vers la gauche et s'ajoute à une tuile égale#
                if matrice[i][j] == matrice[i][j-1] :
                    matrice[i][j-1] += matrice[i][j]
                    matrice[i][j] = 0
                #tuile se décale vers la gauche#
                else :
                    matrice[i][j-1] = matrice[i][j]
                    matrice[i][j] = 0

                return
            
            else :
                matrice[i][j-1] = matrice[i][j]
                matrice[i][j] = 0

            return

    #génère 3 chiffres au hazard#
    #pour la probabilité d'un 2 ou un 4#
    p = rd.randint(1, 10)
    #pour la probabilité de placement de la tuile dans le quadrillage à droite#
    pi = rd.randint(0,3)
    pj = rd.randint(1,3)
    
    for i in range(4) :
        for j in range(4) :
            
            if p == 1 :
                matrice[pi][pj] = 4
                canvas.create_rectangle((175*pi, 175*pj), (175*pi + 175, 175*pj + 175), fill="yellow")
                canvas.create_text(175*pi + 175/2, 175*pj + 175/2, fill="black", font="helvetica, 40", text="4")
                   
            else :
                matrice[pi][pj] = 2
                canvas.create_rectangle((175*pi, 175*pj), (175*pi + 175, 175*pj + 175), fill="yellow")
                canvas.create_text(175*pi + 175/2, 175*pj + 175/2, fill="black", font="helvetica, 40", text="2")

    
    print(matrice)
    


def tuiles_right() :
    for i in range(4) :
        for j in range(4) :
            #quand tuile pas égale à 0#
            if matrice[i][j] != 0 :
                #tuile se décale vers la droite et s'ajoute à une tuile égale#
                if matrice[i][j] == matrice[i][j+1] :
                    matrice[i][j+1] += matrice[i][j]
                    matrice[i][j] = 0
                #tuile se décale vers la droite#
                else :
                    matrice[i][j+1] = matrice[i][j]
                    matrice[i][j] = 0

                return
            
            else :
                matrice[i][j+1] = matrice[i][j]
                matrice[i][j] = 0

            return

    #génère 3 chiffres au hazard#
    #pour la probabilité d'un 2 ou un 4#
    p = rd.randint(1, 10)
    #pour la probabilité de placement de la tuile dans le quadrillage à gauche#
    pi = rd.randint(0,3)
    pj = rd.randint(0,2)
    
    for i in range(4) :
        for j in range(4) :
            
            if p == 1 :
                matrice[pi][pj] = 4
                canvas.create_rectangle((175*pi, 175*pj), (175*pi + 175, 175*pj + 175), fill="yellow")
                canvas.create_text(175*pi + 175/2, 175*pj + 175/2, fill="black", font="helvetica, 40", text="4")
                   
            else :
                matrice[pi][pj] = 2
                canvas.create_rectangle((175*pi, 175*pj), (175*pi + 175, 175*pj + 175), fill="yellow")
                canvas.create_text(175*pi + 175/2, 175*pj + 175/2, fill="black", font="helvetica, 40", text="2")

    
    print(matrice)


def tuiles_up() :
    for i in range(4) :
        for j in range(4) :
            #quand tuile pas égale à 0#
            if matrice[i][j] != 0 :
                #tuile se décale vers le haut et s'ajoute à une tuile égale#
                if matrice[i][j] == matrice[i-1][j] :
                    matrice[i-1][j] += matrice[i][j]
                    matrice[i][j] = 0
                #tuile se décale vers le haut#
                else :
                    matrice[i-1][j] = matrice[i][j]
                    matrice[i][j] = 0

                return
            
            else :
                matrice[i-1][j] = matrice[i][j]
                matrice[i][j] = 0

            return

    #génère 3 chiffres au hazard#
    #pour la probabilité d'un 2 ou un 4#
    p = rd.randint(1, 10)
    #pour la probabilité de placement de la tuile dans le quadrillage en bas#
    pi = rd.randint(1,3)
    pj = rd.randint(0,3)
    
    for i in range(4) :
        for j in range(4) :
            
            if p == 1 :
                matrice[pi][pj] = 4
                canvas.create_rectangle((175*pi, 175*pj), (175*pi + 175, 175*pj + 175), fill="yellow")
                canvas.create_text(175*pi + 175/2, 175*pj + 175/2, fill="black", font="helvetica, 40", text="4")
                   
            else :
                matrice[pi][pj] = 2
                canvas.create_rectangle((175*pi, 175*pj), (175*pi + 175, 175*pj + 175), fill="yellow")
                canvas.create_text(175*pi + 175/2, 175*pj + 175/2, fill="black", font="helvetica, 40", text="2")

    
    print(matrice)


def tuiles_down() :
    for i in range(4) :
        for j in range(4) :
            #quand tuile pas égale à 0#
            if matrice[i][j] != 0 :
                #tuile se décale vers le bas et s'ajoute à une tuile égale#
                if matrice[i][j] == matrice[i+1][j] :
                    matrice[i+1][j] += matrice[i][j]
                    matrice[i][j] = 0
                #tuile se décale vers le bas#
                else :
                    matrice[i+1][j] = matrice[i][j]
                    matrice[i][j] = 0

                return
            
            else :
                matrice[i+1][j] = matrice[i][j]
                matrice[i][j] = 0

            return

    #génère 3 chiffres au hazard#
    #pour la probabilité d'un 2 ou un 4#
    p = rd.randint(1, 10)
    #pour la probabilité de placement de la tuile dans le quadrillage en haut#
    pi = rd.randint(0,2)
    pj = rd.randint(0,3)
    
    for i in range(4) :
        for j in range(4) :
            
            if p == 1 :
                matrice[pi][pj] = 4
                canvas.create_rectangle((175*pi, 175*pj), (175*pi + 175, 175*pj + 175), fill="yellow")
                canvas.create_text(175*pi + 175/2, 175*pj + 175/2, fill="black", font="helvetica, 40", text="4")
                   
            else :
                matrice[pi][pj] = 2
                canvas.create_rectangle((175*pi, 175*pj), (175*pi + 175, 175*pj + 175), fill="yellow")
                canvas.create_text(175*pi + 175/2, 175*pj + 175/2, fill="black", font="helvetica, 40", text="2")

    
    print(matrice)


def end_game() :
    #partie terminée,le score est donné#
    b = 0
    for i in range(16):
      b += int(input())
    print("le score est",b)



def save_game() :
    #ouvre un fichier et écrit dedans#
    fic = open("fichier.txt","w")
    for i in range (4):
        for j in range(4):
            fic.write(str(matrice[i][j]))
    fic.close()


def load_game() :
    #ouvre un fichier et le lit et écrit ce qu'il y a dedans#
    fic = open("fichier.tkt","r")
    print(str(fic))
    fic.close()

#création des boutons#
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