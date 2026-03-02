from tkinter import *
from PIL import Image, ImageTk


class LevelManager:
    def __init__(self, canvas):
        self.canvas = canvas
        self.current_level = 0

        # Hier definierst du deine Level (Bild + Startposition etc.)
        self.levels = [
            {
                "image": "labyrinth1.png",
                "player_start": (50, 50)
            },
            {
                "image": "labyrinth2.png",
                "player_start": (100, 100)
            }
        ]

        self.lab_image_obj = None
        self.player = None

        self.load_level(self.current_level)

    def load_level(self, level_index):
        self.canvas.delete("all")

        level_data = self.levels[level_index]

        # Labyrinth Bild laden
        img = Image.open(level_data["image"])
        img = img.resize((600, 600))
        self.lab_image_obj = ImageTk.PhotoImage(img)

        self.canvas.create_image(0, 0, anchor=NW, image=self.lab_image_obj)

        # Spieler zeichnen
        x, y = level_data["player_start"]
        self.player = self.canvas.create_oval(
            x, y, x + 20, y + 20, fill="red"
        )

    def next_level(self):
        self.current_level += 1
        if self.current_level >= len(self.levels):
            print("Spiel beendet!")
            self.current_level = 0

        self.load_level(self.current_level)


# ------------------------
# Hauptprogramm
# ------------------------

root = Tk()
root.title("Labyrinth-Spiel")
root.geometry("600x600")

canvas = Canvas(root, width=600, height=600)
canvas.pack()

level_manager = LevelManager(canvas)

# Taste "n" für nächstes Level
root.bind("n", lambda event: level_manager.next_level())

root.mainloop()