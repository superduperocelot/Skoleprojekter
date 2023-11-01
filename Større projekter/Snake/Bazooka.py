from Food import food

class bazooka(food):
    def __init__(self, x, y, grid):
        food.__init__(self, x, y, grid)
        self.value = 3


