# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 22:02:30 2023

@author: DarkCoder
"""



import tkinter as tk
from tkinter import *
from tkinter import PhotoImage


#Dictionnaire de couleur
couleur = {"nero": "#252726",
           "purple":"#800080",
           "white": "#FFFFFF"}



#Paramétrage de la fenêtre 
app = tk.Tk()
app.title("WeAreCoder")
app.config(bg="gray30")
app.geometry("400x600")
app.iconbitmap("logo1.ico")


#Paramétrage switch
btnEtat = False

#Chargement image navbar
navIcon = PhotoImage(file='menu.png')
closeIcon = PhotoImage(file='close.png')
imgFond = PhotoImage(file='back_image3.png')


#Définir les fonctions switch
def switch():
    global btnEtat
    if btnEtat is True:
        #Creer une fermetture animée navbar
        for x in range(300):
            navLateral.place(x=-x, y=0)
            topFrame.update()
        #Reset couleur widgets
        bannerTexte.config(fg="purple")
        accueilText.config(bg=couleur["purple"])
        topFrame.config(bg=couleur["purple"])
        app.config(bg="gray30")
        btnEtat = False
    else:
        for x in range(-300, 0):
            navLateral.place(x=x, y=0)
            topFrame.update()
            btnEtat = True
            

#Créer une fermetture  animée navbar


#top bar ou nav top
topFrame = tk.Frame(app, bg=couleur["purple"])
topFrame.pack(side="top", fill=tk.X)

#Texte de top bar 
accueilText = tk.Label(topFrame, text="Java", 
                       font="ExtraCondensed 15", bg=couleur["nero"], 
                       fg="white", height=2, padx=20)
accueilText.pack(side="right")

#


#Banner texte et image de fond 
can = Canvas(app, width=400, height=600 )
can.create_image(0, 0, anchor=NW, 
                 image=imgFond)
bannerTexte = tk.Label(app, text="CODING", 
                      font="ExtraCondensed 25",
                      fg="purple")
bannerTexte.place(x=50,y=500)
can.pack()

#nav nar  Icone
navbarBtn = tk.Button(topFrame, image=navIcon, bg=couleur["purple"], padx=20,
                       bd=0, 
                       activebackground=couleur["purple"],
                       command=switch)
navbarBtn.place(x=10,y=10)

#Paramètre navbar latéral
navLateral = tk.Frame(app, bg="gray30", 
                      width=300, height=600)
navLateral.place(x=-300, y=0)
tk.Label(navLateral, font="ExtraCondensed 15", bg=couleur["purple"],
         fg="black", width=300, height=2, padx=20).place(x=0, y=0)
y = 80

# Les options dans la nav bar latérale
option = ["ACCUEIL", "PAGE", "PROFIL", "PARAETRES", "AIDE"]

#Positionnement des options dans la navbar

for i in range(5):
    tk.Button(navLateral, text=option[i], font="ExtraCondensed 10", 
              bg="gray30", fg=couleur["white"], 
              activebackground=couleur["purple"], 
              bd=0).place(x=25, y=y)
    y+=40



#Paramétrage du bouton de fermerture menu
fermeBtn = tk.Button(navLateral, image=closeIcon, bg=couleur["purple"],
                     activebackground=couleur["purple"], 
                     bd=0, command=switch)
fermeBtn.place(x=250, y=10)






app.mainloop()
