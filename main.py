from tkinter import *
from PIL import Image, ImageTk

# Hauptfenster
root = Tk()
root.title("Labyrinth-Spiel")
root.geometry("600x600")

# Canvas für das Spiel
canvas = Canvas(root, width=600, height=600)
canvas.pack()

# Labyrinth-Bild laden
lab_img = PhotoImage(file="labyrinth-photo.png")  # PNG im assets-Ordner
canvas.create_image(0, 0, anchor=NW, image=lab_img)

# Hauptloop starten
root.mainloop()
root.mainloop()