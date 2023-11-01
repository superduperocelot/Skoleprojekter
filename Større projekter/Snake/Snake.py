import pygame
import sys
class snake:
    def __init__(self):
        self.snake_x = 3
        self.snake_y = 7
        
        self.direction_right = True
        self.direction_left = False
        self.direction_down = False
        self.direction_up = False
        self.snake_length = 2

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
    
                
    def update(self):
        if self.direction_up == True:
            self.snake_y -= 1
        elif self.direction_down == True:
            self.snake_y += 1
        elif self.direction_right == True:
            self.snake_x += 1
        elif self.direction_left == True:
            self.snake_x -= 1
