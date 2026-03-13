from tkinter import *

CELL = 30  # Größe einer Zelle im Raster

class Labyrinth:

    def __init__(self, canvas):
        self.canvas = canvas

        # ASCII-Labyrinth (20x20 Zellen)
        self.map = [
            "####################",
            "#..................#",
            "#.######.#.#######.#",
            "#.#....#.#.....#.#.#",
            "#.#.##.#######.#.#.#",
            "#.#.#..#.....#.#.#.#",
            "#.#.#.######.#.#.#.#",
            "#...#........#...#..",
            "#####.###########.#.",
            "#.....#.........#.#.",
            "#.###.#.#######.#.#.",
            "#.#...#.....#...#.#.",
            "#.#.#######.#.###.#.",
            "#.#.........#.....#.",
            "#.###############.#.",
            "#.................#.",
            "#.###############.#.",
            "#.......#.........#.",
            "#.###############.#.",
            "####################"
        ]

        self.walls = []
        self.end_area = (17 * CELL, 17 * CELL, 19 * CELL, 19 * CELL)

        self._generate_walls()

    def _generate_walls(self):
        for row, line in enumerate(self.map):
            for col, char in enumerate(line):
                if char == "#":
                    x1 = col * CELL
                    y1 = row * CELL
                    x2 = x1 + CELL
                    y2 = y1 + CELL
                    self.walls.append((x1, y1, x2, y2))

    def draw(self):
        for wall in self.walls:
            x1, y1, x2, y2 = wall
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")

        # Zielbereich
        x1, y1, x2, y2 = self.end_area
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")

    def is_collision(self, x, y, width, height):
        for wx1, wy1, wx2, wy2 in self.walls:
            if x < wx2 and x + width > wx1 and y < wy2 and y + height > wy1:
                return True
        return False

    def reached_end(self, x, y, width, height):
        x1, y1, x2, y2 = self.end_area
        return x + width > x1 and x < x2 and y + height > y1 and y < y2