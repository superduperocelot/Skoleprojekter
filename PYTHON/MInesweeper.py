import random
grid_x = 8
grid_y = 8
grid = []
topgrid = []
mineCount = 5

for y in range(grid_y):
    grid.append([])
    for x in range(grid_x):
        grid[y].append(0)

for y in range(grid_y):
    topgrid.append([])
    for x in range(grid_x):
        topgrid[y].append('#')




def PlaceMines(not_x, not_y):
    for i in range(mineCount):
        done = False
        while not done:
            x = random.randint(0, grid_x - 1)
            y = random.randint(0, grid_y - 1)
            if grid[y][x] == 0 and (x != not_x or y != not_y):
                grid[y][x] = 9
                done = True
    for y in range(grid_y):
        for x in range(grid_x):
            if grid[y][x] == 0:
                grid[y][x] = CheckMines(x, y)

def CheckMines(tile_x, tile_y):
    mines = 0
    for y in range(tile_y - 1, tile_y + 2):
        for x in range(tile_x - 1, tile_x + 2):
            if 0 <= x < grid_x and 0 <= y < grid_y and grid[y][x] == 9:
                mines += 1
    return mines

def BlankScan():
    done = True
    for y in range(grid_y):
        for x in range(grid_x):
            if topgrid[y][x] == 0:
                for scan_y in range(y - 1, y + 2):
                    for scan_x in range(x - 1, x + 2):
                        if 0 <= scan_x < grid_x and 0 <= scan_y < grid_y and grid[scan_y][scan_x] != 9:
                            topgrid[scan_y][scan_x] = grid[scan_y][scan_x]
                            done = False
    return done

                
                

def MineScan():
    for y in topgrid:
        for x in y:
            if x == 9:
                return True

# Print the grid with row and column labels
def PrintGrid():
    print('  A B C D')
    for y in range(len(topgrid)):
        print(chr(65 + y), end=' ')
        for x in range(len(topgrid[y])):
            print(topgrid[y][x], end=' ')
        print()

PrintGrid()
inp = input('')
PlaceMines(ord(inp[0]) - 65, ord(inp[1]) - 65)
topgrid[ord(inp[0]) - 65][ord(inp[1]) - 65] = grid[ord(inp[0]) - 65][ord(inp[1]) - 65]
BlankScan()

running = True
while running:
    PrintGrid()
    inp = input('')
    if len(inp) == 2:
        topgrid[ord(inp[0]) - 65][ord(inp[1]) - 65] = grid[ord(inp[0]) - 65][ord(inp[1]) - 65]
    
    elif len(inp) == 3:
        if topgrid[ord(inp[0]) - 65][ord(inp[1]) - 65] == 'X':
            topgrid[ord(inp[0]) - 65][ord(inp[1]) - 65] = '#'
        
        elif topgrid[ord(inp[0]) - 65][ord(inp[1]) - 65] == '#':
            topgrid[ord(inp[0]) - 65][ord(inp[1]) - 65] = 'X'
    
    done = False
    while not done:
        done = BlankScan()
    if MineScan() == True:
        print(':(')
        running = False
