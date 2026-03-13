from tkinter import *
import pygame
from labyrinth import Labyrinth
from player import Player

# Musik starten
pygame.mixer.init()
pygame.mixer.music.load("hintergrundmusik.mp3")
pygame.mixer.music.play(-1)

# Fenster
root = Tk()
root.title("Labyrinth-Spiel")
root.geometry("600x600")
canvas = Canvas(root, width=600, height=600)
canvas.pack()

# Labyrinth und Spieler
labyrinth = Labyrinth(canvas)
labyrinth.draw()
player = Player(canvas, labyrinth)

# Bewegung
def move_player(event):
    if event.keysym == "Up":
        player.move(0, -5)
    elif event.keysym == "Down":
        player.move(0, 5)
    elif event.keysym == "Left":
        player.move(-5, 0)
    elif event.keysym == "Right":
        player.move(5, 0)

root.bind("<Key>", move_player)
root.mainloop()