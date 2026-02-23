# Tkinter: Python-Bibliothek für grafische Oberflächen
from tkinter import *
from tkinter import colorchooser
import pygame

pygame.mixer.init()
pygame.mixer.music.load("hintergrundmusik.mp3")
pygame.mixer.music.play(-1)

# Hauptfenster erstellen
root = Tk()
root.title("Labyrinth-Spiel")
root.geometry("600x600")

farbe = colorchooser.askcolor(title="Wähle eine Hintergrundfarbe")[1] 
if farbe:  
    root.configure(bg=farbe)

def farbe_aendern():
    farbe = colorchooser.askcolor()[1]
    if farbe:
        root.configure(bg=farbe)

button = Button(root, text="Hintergrundfarbe ändern", command=farbe_aendern)
button.pack(pady=20)

root.mainloop()
