import pygame

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 40
        self.height = 40
        self.totalDistance = 0
        pygame.draw.rect(self.image, (200, 200, 200), pygame.Rect(0, 50, self.width, self.height))
        self.rect = self.image.get_rect()


    def Move(self):
     
        if self.totalDistance >= 0 and self.totalDistance < 400:
            self.rect.y = 50 - self.height/2
            self.rect.x = self.totalDistance - self.width/2

        if self.totalDistance >= 400 and self.totalDistance < 500:
            self.rect.y = self.totalDistance - 400 + 50 - self.height/2
            self.rect.x = 400 - self.width/2

        if self.totalDistance >= 500 and self.totalDistance < 600:
            self.rect.y = 150 - self.height/2
            self.rect.x = self.totalDistance - 500 + 400 - self.width/2
        
        if self.totalDistance >= 600 and self.totalDistance < 700:
            self.rect.y = -self.totalDistance + 600 + 150 - self.height/2
            self.rect.x = 500 - self.width/2

        if self.totalDistance >= 700 and self.totalDistance < 1150:
            self.rect.y = 50 - self.height/2
            self.rect.x = self.totalDistance - 700 + 500 - self.width/2

        if self.totalDistance >= 1150 and self.totalDistance < 1650:
            self.rect.y = self.totalDistance - 1150 + 50 - self.height/2
            self.rect.x = 950 - self.width/2

        if self.totalDistance >= 1650 and self.totalDistance < 1750:
            self.rect.y = 550 - self.height/2
            self.rect.x = -self.totalDistance + 1650 + 950 - self.width/2

        if self.totalDistance >= 1750 and self.totalDistance < 2150:
            self.rect.y = -self.totalDistance + 1750 + 550 - self.height/2
            self.rect.x = 850 - self.width/2

        if self.totalDistance >= 2150 and self.totalDistance < 2250:
            self.rect.y = 150 - self.height/2
            self.rect.x = -self.totalDistance + 2150 + 850 - self.width/2

        if self.totalDistance >= 2250 and self.totalDistance < 2550:
            self.rect.y = self.totalDistance - 2250 + 150 - self.height/2
            self.rect.x = 750 - self.width/2

        if self.totalDistance >= 2550 and self.totalDistance < 3200:
            self.rect.y = 450 - self.height/2
            self.rect.x = -self.totalDistance + 2550 + 750 - self.width/2

        if self.totalDistance >= 3200 and self.totalDistance < 3400:
            self.rect.y = self.totalDistance - 3200 + 450 - self.height/2
            self.rect.x = 100 - self.width/2
        
        if self.totalDistance >= 3400 and self.totalDistance < 4300:
            self.rect.y = 650 - self.height/2
            self.rect.x = self.totalDistance - 3400 + 100 - self.width/2
        

    def DrawHealth(self, screen):
        self.healthSurface = pygame.Surface((40, 10), pygame.SRCALPHA)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.rect.x, self.rect.y - 20, 40, 10))
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.rect.x, self.rect.y - 20, 40 - 40 * (self.health/self.maxhealth), 10))


class BasicEnemy(enemy):
    def __init__(self):
        self.image = pygame.image.load("Sprites/BasicEnemy.png")
        self.maxhealth = 3
        self.health = self.maxhealth
        self.moveSpeed = 3
        self.moneydrop = 10
        super().__init__()
        self.rect.x = 0
        self.rect.y = 50
        self.damage = 15


class StrongerEnemy(enemy):
    def __init__(self):
        self.image = pygame.image.load("Sprites/StrongerEnemy.png")
        self.maxhealth = 5
        self.health = self.maxhealth
        self.moveSpeed = 4
        self.moneydrop = 20
        super().__init__()
        self.rect.x = 0
        self.rect.y = 50
        self.damage = 25
        
class PlayButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Sprites/PlayButton.png")
        self.rect = self.image.get_rect()
        self.rect.center = (1200, 660)
        #pygame.draw.rect(self.image, (0, 0, 0), pygame.Rect(400, 400, 80, 60))