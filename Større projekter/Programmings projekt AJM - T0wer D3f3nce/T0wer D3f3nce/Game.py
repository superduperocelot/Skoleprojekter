import pygame
import Draw
import SpawnEnemy
import Classes
import Towers
import PublicVariables as pv
import EveryGroup as eg



def main():

    waves = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]]

    eg.towers.add(Towers.ArcherTower(1100, 50, 1100, 50))
    eg.towers.add(Towers.ArcherTower(1200, 50, 1200, 50))
    eg.towers.add(Towers.ArcherTower(1300, 50, 1300, 50))
    eg.towers.add(Towers.IceTower(1150, 150, 1150, 150))
    eg.towers.add(Towers.IceTower(1250, 150, 1250, 150))
    eg.towers.add(Towers.FireTower(1150, 250, 1150, 250))
    eg.towers.add(Towers.FireTower(1250, 250, 1250, 250))
    eg.towers.add(Towers.BunnyTower(1150, 350, 1150, 350))
    eg.towers.add(Towers.BunnyTower(1250, 350, 1250, 350))
    playButton = Classes.PlayButton()

     
    pygame.init()

    screen = pygame.display.set_mode((1400,700))
    screen.fill((76, 187, 23))
    Draw.DrawScreen(screen)
    
    pygame.display.flip()
    
    textFont = pygame.font.SysFont("Comic Sans", 24, bold = True)
    largeFont = pygame.font.SysFont("Comic Sans", 58, bold = True)
    smallFont = pygame.font.SysFont("Comic Sans", 18, bold = True)


    def DrawText(text, textCol, x, y, screen):
        textSurface = textFont.render(text, True, textCol)
        textRect = textSurface.get_rect(center = (x, y))
        screen.blit(textSurface, textRect)

    def LargeText(text, textCol, x , y, screen):
        textSurface = largeFont.render(text, True, textCol)
        textRect = textSurface.get_rect(center = (x, y))
        screen.blit(textSurface, textRect)
    
    def SmallText(text, textCol, x , y, screen):
        textSurface = smallFont.render(text, True, textCol)
        textRect = textSurface.get_rect(center = (x, y))
        screen.blit(textSurface, textRect)
     
    dragging = False
    running = True

    # main loop
    while running:
        currentTime = pygame.time.get_ticks()
        SpawnEnemy.Spawn(pv.currentRound, waves, eg.enemies)
        #Flytter fjender
        for enemy in eg.enemies:
            enemy.totalDistance += enemy.moveSpeed
            enemy.Move()
        
        mouseX, mouseY = pygame.mouse.get_pos()
        eg.enemies.update()

        #Fjerner fjender der skal fjernes
        for enemy in eg.enemies:
            if enemy.health <= 0:
                pv.money += enemy.moneydrop
                eg.enemies.remove(enemy)
            if enemy.totalDistance > 4280:
                eg.enemies.remove(enemy)
                pv.health -= enemy.damage
        eg.towers.update()

        #Tegner alt der skal tegnes
        Draw.DrawScreen(screen)
        eg.enemies.draw(screen)
        for enemy in eg.enemies:
            enemy.DrawHealth(screen)
        eg.towers.draw(screen)
        screen.blit(playButton.image, playButton.rect)
        DrawText(str(pv.health) + " <3", "gray100", 1050, 650, screen)
        DrawText(str(pv.money) + " $", "gray100", 1050, 680, screen)
        SmallText("100$", (255,255,255), 1040, 50, screen)
        SmallText("200$", (255,255,255), 1040, 150, screen)
        SmallText("300$", (255,255,255), 1040, 250, screen)
        SmallText("400$", (255,255,255), 1040, 350, screen)

        #Tjekker efter, og skyder på mål for alle placerede tårne
        for tower in eg.towers:
            if tower.placed == True and currentTime - tower.lastshot >= tower.speed:
                tower.Shoot()
                tower.lastshot = currentTime
        
        #Taber hvis liv er 0
        if pv.health <= 0:
            screen.fill((0, 0, 0))
            LargeText(str("Game Over"), (200, 0, 0), screen.get_width()/2, screen.get_height()/2, screen)

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Hvis der klikkes på et tårn, skal der tages fat i tårnet
                for tower in eg.towers:
                    if tower.rect.collidepoint(event.pos) and tower.placed == False and pv.money >= tower.cost and dragging == False:
                        pv.money -= tower.cost
                        dragging = True
                        chosenTower = tower
                
                if playButton.rect.collidepoint(event.pos) and pv.roundRunning == False and pv.currentRound < len(waves) - 1:
                    pv.currentRound += 1
                    pv.currentEnemySpawn = 0

            if event.type == pygame.MOUSEBUTTONUP and dragging:
                #Tjekker om det valgte tårn rører ved vej eller andre tårne.
                touchingSomething = False
                towersTouched = -1
                for roadSegment in Draw.roadSegments:
                    if chosenTower.rect.colliderect(roadSegment):
                        touchingSomething = True
                for tower in eg.towers:
                    if chosenTower.rect.colliderect(tower):
                        towersTouched += 1
                if towersTouched > 0:
                    touchingSomething = True
                if touchingSomething == False:
                    if mouseX <= 980 and not chosenTower.placed:
                        dragging = False
                        chosenTower.placed = True
                    else:
                        #Tilbage til standardposition
                        chosenTower.rect.topleft = (chosenTower.default_x, chosenTower.default_y)
                        pv.money += chosenTower.cost
                        dragging = False
                else:
                    #Tilbage til standardposition
                    chosenTower.rect.topleft = (chosenTower.default_x, chosenTower.default_y)
                    pv.money += chosenTower.cost
                    dragging = False
                    
        if dragging:
            #Valgte tårn følger musen
            chosenTower.rect.center = pygame.mouse.get_pos()
            chosenTower.DrawRange(screen)

        eg.towers.update()
        pygame.display.flip()
        pygame.display.set_caption("T0wer D3f3nce")
        pygame.time.Clock().tick(60)
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    main()