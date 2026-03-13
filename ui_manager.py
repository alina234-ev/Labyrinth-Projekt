from tkinter import *

class UIManager:

    def __init__(self, canvas):
        self.canvas = canvas

    def show_win_message(self):
        self.canvas.create_text(
            300,
            300,
            text="Du hast gewonnen!",
            font=("Arial", 30),
            fill="green"
        )