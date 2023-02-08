import tkinter as tk

def button_click(i, j):
    print(str(i) + str(j))

root = tk.Tk()

def grid(hauteur,largeur):
    for i in range(hauteur):
        for j in range(largeur):
            b = tk.Button(root, text="Button " + str(i) + str(j), width=10, height=5, command=lambda i=i, j=j: button_click(i, j))
            b.grid(row=i, column=j)

    root.mainloop()
    
grid(9,6)