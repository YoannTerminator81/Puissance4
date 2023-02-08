import tkinter as tk

def grid(hauteur,largeur):
    root = tk.Tk()

    for i in range(hauteur):
        for j in range(largeur):
            b = tk.Button(root, text="Button " + str(i) + str(j), width=10, height=5)
            b.grid(row=i, column=j)

    root.mainloop()

grid(7,10)
    