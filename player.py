from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from labyrinth import CELL

class Player:

    def __init__(self, canvas, labyrinth):
        self.canvas = canvas
        self.labyrinth = labyrinth

        # Größe
        self.width = 15
        self.height = 30

        # Startpunkt (freie Zelle im Raster)
        self.x = 1 * CELL
        self.y = 1 * CELL

        # Spielerbild
        img = Image.open("player1.jpg")
        img = img.resize((self.width, self.height))
        self.player_img = ImageTk.PhotoImage(img)

        # Spieler auf Canvas
        self.player = self.canvas.create_image(self.x, self.y, image=self.player_img, anchor=NW)

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if not self.labyrinth.is_collision(new_x, new_y, self.width, self.height):
            self.x = new_x
            self.y = new_y
            self.canvas.move(self.player, dx, dy)

        if self.labyrinth.reached_end(self.x, self.y, self.width, self.height):
            messagebox.showinfo("Gewonnen!", "Du hast das Labyrinth geschafft!")