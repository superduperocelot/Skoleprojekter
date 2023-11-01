import pygame
import EveryGroup as eg

class Tower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.cost = 100
        self.damage = 0
        self.placed = False
        self.speed = 0
        self.lastshot = 0
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(x, y))

    def Shoot(self):
        self.furthestDistance = 0
        self.target = None
        for enemy in eg.enemies:
            if ((enemy.rect.x - enemy.width/2) - (self.rect.x - self.image.get_width()/2))**2 + ((enemy.rect.y - enemy.width/2) - (self.rect.y - self.image.get_height()/2))**2 <= self.range**2 and enemy.totalDistance > self.furthestDistance:
                self.furthestDistance = enemy.totalDistance
                self.target = enemy
        if self.target != None:
            self.target.health -= self.damage
    
    def DrawRange(self, screen):
        transparency = 128  # Adjust alpha value for desired transparency (0 to 255)
        circle_surface = pygame.Surface((self.range * 2, self.range * 2), pygame.SRCALPHA)
        pygame.draw.circle(circle_surface, (100, 100, 100, transparency), (self.range, self.range), self.range)
        screen.blit(circle_surface, (self.rect.x - self.range + self.image.get_width()/2, self.rect.y - self.range + self.image.get_height()/2))


class ArcherTower(Tower):
    def __init__(self, x, y, default_x, default_y):
        self.image = pygame.image.load(r"Sprites/ArcherTower.png")
        super().__init__(x, y)
        self.damage = 1
        self.range = 150
        self.cost = 100
        self.speed = 1200
        self.default_x = default_x - self.image.get_width()/2
        self.default_y = default_y - self.image.get_height()/2
    


class IceTower(Tower):
    def __init__(self, x, y, default_x, default_y):
        self.image = pygame.image.load(r"Sprites/IceTower.png")
        super().__init__(x, y)
        self.damage = 2
        self.range = 120
        self.cost = 200
        self.speed = 1400
        self.default_x = default_x - self.image.get_width()/2
        self.default_y = default_y - self.image.get_height()/2
    
    def Shoot(self):
        super().Shoot()
        if self.target != None:
            self.target.moveSpeed *= 0.9


class FireTower(Tower):
    def __init__(self, x, y, default_x, default_y):
        self.image = pygame.image.load(r"Sprites/FlameTower.png")
        super().__init__(x, y)
        self.damage = 4
        self.range = 90
        self.cost = 300
        self.speed = 2000
        self.default_x = default_x - self.image.get_width()/2
        self.default_y = default_y - self.image.get_height()/2


class BunnyTower(Tower):
    def __init__(self, x, y, default_x, default_y):
        self.image = pygame.image.load(r"Sprites/BunnyTower.png")
        super().__init__(x, y)
        self.damage = 0.5
        self.range = 250
        self.cost = 400
        self.speed = 400
        self.default_x = default_x - self.image.get_width()/2
        self.default_y = default_y - self.image.get_height()/2
        
