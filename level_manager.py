class LevelManager:

    def __init__(self):
        self.current_level = 1

    def next_level(self):
        self.current_level += 1
        print("Level:", self.current_level)

    def reset_levels(self):
        self.current_level = 1