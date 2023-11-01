import pygame
from Snake import snake
import random
from Food import food 
from AK_47 import ak_47
from Bazooka import bazooka
from Pistol import pistol

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#17 * 15
block_size = 50
Snake = snake()
chance = random.randint(0,2)
if chance == 0:
    Food = pistol(10, 7, grid)
elif chance == 1:
    Food = ak_47(10, 7, grid)
else:
    Food = bazooka(10, 7, grid)

class Snake_sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width, x, y):
        super().__init__()
  
        self.image = pygame.image.load('Sprites/Correct Snake head smaller.png')
  
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()

class Food_sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width, x, y):
        super().__init__()
  
        self.image = pygame.image.load('Sprites/Correct Snake head smaller.png')
  
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()

def update_game():
    Snake.update()
    snake_parts.update()


    #læg 1 til alle tal
    for y in range(15):
        for x in range (17):
                if type(grid[y][x]) == int and grid[y][x] != 0:
                    grid[y][x] += 1

    #Fjerner enden
    for y in range(15):
        for x in range (17):
                if grid[y][x] == Snake.snake_length + 1:
                    grid[y][x] = 0
    
    hit_something()

    #Laver hovedet
    grid[Snake.snake_y][Snake.snake_x] = 1
    
    #laver mad
    grid[Food.y][Food.x] = 'a'


def hit_something():
    if Snake.snake_y < 0 or Snake.snake_y > 15 or Snake.snake_x < 0 or Snake.snake_x > 17 or grid[Snake.snake_y][Snake.snake_x] != 0 and type(grid[Snake.snake_y][Snake.snake_x]) == int:
        print(Snake.snake_length)
        ''/2
    elif grid[Snake.snake_y][Snake.snake_x] == 'a':
        global Food
        global chance
        Snake.snake_length += Food.value
        chance = random.randint(0,2)
        if chance == 0:
            Food = pistol(10, 7, grid)
        elif chance == 1:
            Food = ak_47(10, 7, grid)
        else:
            Food = bazooka(10, 7, grid)
        Food.eaten()

def check_event_right():
    if event.key == pygame.K_RIGHT and Snake.direction_left == False:
        Snake.direction_right = True
        Snake.direction_left = False
        Snake.direction_up = False
        Snake.direction_down = False

def check_event_down():
    if event.key == pygame.K_DOWN and Snake.direction_up == False:
        Snake.direction_right = False
        Snake.direction_left = False
        Snake.direction_up = False
        Snake.direction_down = True
        
def check_event_up():
    if event.key == pygame.K_UP and Snake.direction_down == False:
        Snake.direction_right = False
        Snake.direction_left = False
        Snake.direction_up = True
        Snake.direction_down = False
    
def check_event_left():
    if event.key == pygame.K_LEFT and Snake.direction_right == False:
        Snake.direction_right = False
        Snake.direction_left = True
        Snake.direction_up = False
        Snake.direction_down = False

def check_direction():
    check_event_down()
    check_event_left()
    check_event_right()
    check_event_up()

def make_blocks():
    snake_parts.empty()
    all_food.empty()
    for y in range(15):
        for x in range (17):
            if grid[y][x] == 'a':
                object_ = Food_sprite((0, 255, 0), block_size, block_size, x, y)
                object_.rect.x = (x) * block_size
                object_.rect.y = (y) * block_size
                all_food.add(object_)
            elif grid[y][x] != 0:
                object_ = Snake_sprite((255, 0, 0), block_size, block_size, x, y)
                object_.rect.x = (x) * block_size
                object_.rect.y = (y) * block_size
                snake_parts.add(object_)

pygame.init()
pygame.display.set_caption("Super cool snake game")

all_food = pygame.sprite.Group()
snake_parts = pygame.sprite.Group()

screen = pygame.display.set_mode((17 * block_size, 15 * block_size))

clock = pygame.time.Clock()

running = True
# main loop
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            check_direction()

    update_game()
    make_blocks()
    

    screen.fill((0, 0, 0))
    snake_parts.draw(screen)
    all_food.draw(screen)
    pygame.display.flip()
    clock.tick(3 + Snake.snake_length/4)