# import the pygame module, so you can use it
import pygame
import Draw
import SpawnEnemy
import Classes
import Towers
import PublicVariables as sv
import EveryGroup as eg
waves = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
spawnTimes = []

eg.towers.add(Towers.ArcherTower(1100, 50, 1100, 50))
eg.towers.add(Towers.ArcherTower(1200, 50, 1200, 50))
eg.towers.add(Towers.ArcherTower(1300, 50, 1300, 50))
eg.towers.add(Towers.IceTower(1150, 150, 1150, 150))
eg.towers.add(Towers.IceTower(1250, 150, 1250, 150))
eg.towers.add(Towers.FireTower(1150, 250, 1150, 250))
eg.towers.add(Towers.FireTower(1250, 250, 1250, 250))
eg.towers.add(Towers.BunnyTower(1150, 350, 1150, 350))
eg.towers.add(Towers.BunnyTower(1250, 350, 1250, 350))
playbutton = Classes.PlayButton()


# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    #pygame.display.set_caption("minimal program")
     
    text_font = pygame.font.SysFont("Comic Sans", 24, bold = True)
    Large_font = pygame.font.SysFont("Comic Sans", 58, bold = True)
    
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1400,700))
    screen.fill((76, 187, 23))
    Draw.draw_road(screen)
    
    pygame.display.flip()
    
    def draw_text(text, text_col, x, y, screen):
        text_surface = text_font.render(text, True, text_col)
        text_rect = text_surface.get_rect(center = (x, y))
        screen.blit(text_surface, text_rect)

    def large_text(text, text_col, x , y, screen):
        text_surface = Large_font.render(text, True, text_col)
        text_rect = text_surface.get_rect(center = (x, y))
        screen.blit(text_surface, text_rect)
    
    dragging = False
     
    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        current_time = pygame.time.get_ticks()
        SpawnEnemy.spawn(sv.currentRound, waves, eg.enemies)
        for enemy in eg.enemies:
            enemy.total_distance += enemy.movespeed
            enemy.move()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        eg.enemies.update()
        for enemy in eg.enemies:
            if enemy.health <= 0:
                sv.Money += enemy.moneydrop
                eg.enemies.remove(enemy)
            if enemy.total_distance > 4280:
                eg.enemies.remove(enemy)
                sv.Health -= enemy.damage
        eg.towers.update()
        Draw.draw_road(screen)
        eg.enemies.draw(screen)
        for enemy in eg.enemies:
            enemy.DrawHealth(screen)
        eg.towers.draw(screen)
        screen.blit(playbutton.image, playbutton.rect)
        draw_text(str(sv.Health) + " <3", "gray100", 1050, 650, screen)
        draw_text(str(sv.Money) + " $", "gray100", 1050, 680, screen)
        for tower in eg.towers:
            if tower.placed == True and current_time - tower.lastshot >= tower.speed:
                tower.shoot()
                tower.lastshot = current_time
        
        if sv.Health <= 0:
            screen.fill((0, 0, 0))
            large_text(str("Game Over"), (200, 0, 0), screen.get_width()/2, screen.get_height()/2, screen)

       # screen.blit(tower_icon, tower.rect)

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for tower in eg.towers:
                    if tower.rect.collidepoint(event.pos) and tower.placed == False and sv.Money >= tower.cost and dragging == False:
                        sv.Money -= tower.cost
                        dragging = True
                        chosen_tower = tower
                

                if playbutton.rect.collidepoint(event.pos) and sv.roundRunning == False and sv.currentRound < len(waves) - 1:
                    sv.currentRound += 1
                    sv.currentEnemySpawn = 0

            
            if event.type == pygame.MOUSEBUTTONUP and dragging:
                touching_something = False
                towers_touched = -1
                for road_segment in Draw.road_segments:
                    if chosen_tower.rect.colliderect(road_segment):
                        touching_something = True
                for tower in eg.towers:
                    if chosen_tower.rect.colliderect(tower):
                        towers_touched += 1
                if towers_touched > 0:
                    touching_something = True
                print(touching_something)
                if touching_something == False:
                    if mouse_x <= 980 and not chosen_tower.placed:
                        dragging = False
                        chosen_tower.placed = True
                    else:
                        chosen_tower.rect.topleft = (chosen_tower.default_x, chosen_tower.default_y)
                        sv.Money += chosen_tower.cost
                        dragging = False
                else:
                    chosen_tower.rect.topleft = (chosen_tower.default_x, chosen_tower.default_y)
                    sv.Money += chosen_tower.cost
                    dragging = False
                    
                    
        if dragging:
            chosen_tower.rect.center = pygame.mouse.get_pos()
            chosen_tower.draw_range(screen)

        eg.towers.update()
        pygame.display.flip()
        pygame.display.set_caption("T0wer D3f3nce")
        pygame.time.Clock().tick(60)
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()