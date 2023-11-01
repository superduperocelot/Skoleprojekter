grid = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]

def PrintGrid():
    for y in range(3):
        if(y == 0):
            print("A", end="")
        elif(y == 1):
            print("B", end="")
        elif(y == 2):
            print("C", end="")

        for x in range(3):
            print(grid[y][x], end="")
        print("")
    print(" 123")

def CheckForWin():
    return CheckHorizontal(0) or CheckHorizontal(1) or CheckHorizontal(2) or CheckVertical(0) or CheckVertical(1) or CheckVertical(2) or CheckDiagonal()

def CheckHorizontal(y):
    return grid[y][0] == grid[y][1] and grid[y][0] == grid[y][2] and grid[y][0] != "-"

def CheckVertical(x):
    return grid[0][x] == grid[1][x] and grid[0][x] == grid[2][x] and grid[0][x] != "-"

def CheckDiagonal():
    return grid[0][0] == grid[1][1] and grid[2][2] == grid[1][1] and grid[1][1] != "-" or grid[0][2] == grid[1][1] and grid[2][0] == grid[1][1] and grid[1][1] != "-"

running = True
turn = 0
while running:
    PrintGrid()
    if turn % 2 == 0:
        pos = input("Player 1: ")
    else:
        pos = input("Player 2: ")
    if pos[0] == "A":
        y = 0
    elif pos[0] == "B":
        y = 1
    elif pos[0] == "C":
        y = 2
    x = int(pos[1]) - 1

    if grid[y][x] == "-":
        if turn % 2 == 0:
            grid[y][x] = "X"
        else:
            grid[y][x] = "O"
    else:
        print("Du har valgt et optaget felt, og din hjerne fungerer ikke optimalt. Prøv igen\n")
        turn -= 1
    
    if CheckForWin():
        print("Player " + (turn % 2) + 1 + " wins!")
        running = False
    turn += 1

