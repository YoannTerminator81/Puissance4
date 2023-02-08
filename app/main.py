'''
Jeu Puissance4
'''
import tkinter as tk

global hauteur
global largeur
hauteur = []
largeur = []

#Ajoute dans les tableaux les coordonnées du bouton cliqué
def verifier(i,j):
    
    try :
        hauteur[i]
        largeur[j]
    except :
        print("cette position va être créée")
        hauteur.append(i)
        largeur.append(j)

    print(i,j)

def button_click(i, j):
    print(str(i) + str(j))
    verifier(i,j)

root = tk.Tk()

#Création de l'UI
def grid(hauteur,largeur):
    for i in range(hauteur):
        for j in range(largeur):
            b = tk.Button(root, text="Button " + str(i) + str(j), width=10, height=5, command=lambda i=i, j=j: button_click(i, j))
            b.grid(row=i, column=j)

    root.mainloop()
    
grid(7,6)

        

