import pygame
import Classes
import random
import time
import PublicVariables as pv
def Spawn(round, roundList, enemiesList):
    #Er alle fjender allerede spawnet, og kører der allerede en runde?
    if pv.currentEnemySpawn < len(roundList[round]):
        pv.roundRunning = True

        #Finder ud af hvilken fjendetype der skal spawnes
        if roundList[round][pv.currentEnemySpawn] == 0:
            enemy = Classes.BasicEnemy()
        else: #round_list[round][currentSpawn] == 1:
            enemy = Classes.StrongerEnemy()
        
        
        currentTime = pygame.time.get_ticks()
        #Er der gået 1 sekund siden sidste spawn?
        if currentTime - pv.enemySpawnDelay > pv.lastEnemySpawnTime:
            pv.lastEnemySpawnTime = pygame.time.get_ticks()
            enemiesList.add(enemy)
            pv.currentEnemySpawn += 1
            if pv.currentEnemySpawn < len(roundList):

                #Spawn delay for hver enemy type
                if roundList[round][pv.currentEnemySpawn + 1] == 0:
                    pv.enemySpawnDelay = random.randint(700, 1300)
                elif roundList[round][pv.currentEnemySpawn + 1] == 1:
                    pv.enemySpawnDelay = random.randint(1100, 1900)
    else:
        pv.roundRunning = False

                



     


