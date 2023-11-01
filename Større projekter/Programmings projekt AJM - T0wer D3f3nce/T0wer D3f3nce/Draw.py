import pygame
width = 50
roadColor = (78, 53, 36)
menuColor = (52, 47, 35)

roadSegments = [
    #Linjer
    pygame.Rect(0, 50 - width/2, 400, width),
    pygame.Rect(400 - width/2, 50, width, 100),
    pygame.Rect(400, 150 - width/2, 100, width),
    pygame.Rect(500 - width/2, 50, width, 100),
    pygame.Rect(500, 50 - width/2, 450, width),
    pygame.Rect(950 - width/2, 50, width, 500),
    pygame.Rect(850, 550 - width/2, 100, width),
    pygame.Rect(850 - width/2, 150, width, 400),
    pygame.Rect(750, 150 - width/2, 100, width),
    pygame.Rect(750 - width/2, 150, width, 300),
    pygame.Rect(100, 450 - width/2, 650, width),
    pygame.Rect(100 - width/2, 450, width, 200),
    pygame.Rect(100, 650 - width/2, 900, width),
    # Hjørner
    pygame.Rect(400 - width/2, 50 - width/2, width, width),
    pygame.Rect(400 - width/2, 150 - width/2, width, width),
    pygame.Rect(500 - width/2, 50 - width/2, width, width),
    pygame.Rect(500 - width/2, 150 - width/2, width, width),
    pygame.Rect(950 - width/2, 50 - width/2, width, width),
    pygame.Rect(950 - width/2, 550 - width/2, width, width),
    pygame.Rect(850 - width/2, 550 - width/2, width, width),
    pygame.Rect(850 - width/2, 150 - width/2, width, width),
    pygame.Rect(750 - width/2, 150 - width/2, width, width),
    pygame.Rect(750 - width/2, 450 - width/2, width, width),
    pygame.Rect(100 - width/2, 450 - width/2, width, width),
    pygame.Rect(100 - width/2, 650 - width/2, width, width),
    ]

def DrawScreen(screen):

    screen.fill((76, 187, 23))
    
    for roadSegment in roadSegments:
        pygame.draw.rect(screen, roadColor, roadSegment)

    #Menu
    pygame.draw.rect(screen, menuColor, pygame.Rect(1000, 0, 400, 700))
    