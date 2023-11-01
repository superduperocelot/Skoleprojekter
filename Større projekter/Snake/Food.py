import random
class food: 
    def __init__(self,x,y, grid):
        self.spawned = False
        self.value = 2
        self.x = x
        self.y = y
        self.try_x = 0
        self.try_y = 0
        self.grid = grid
        
    def eaten(self):
        self.spawned = False
        while not self.spawned:
            self.try_y = random.randint(0,14)
            self.try_x = random.randint(0,16)

            if self.grid[self.try_y][self.try_x] == 0:
                self.x = self.try_x
                self.y = self.try_y
                self.spawned = True
            
       


        


