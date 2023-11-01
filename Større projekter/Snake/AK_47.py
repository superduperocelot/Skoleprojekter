from Food import food

class ak_47(food):
    def __init__(self, x, y, grid):
        food.__init__(self, x, y, grid)
        self.value = 2