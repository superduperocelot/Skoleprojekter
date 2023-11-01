from Food import food
import random
class pistol(food):
    def __init__(self, x, y, grid):
        food.__init__(self, x, y, grid)
        self.value = 1



