# 423
import pygame, math
WHITE = (255,255,255)
BLACK = (0,0,0)
screen_width = 700
screen_height = 400

class Block(pygame.sprite.Sprite):
    """docstring for Block"""
    def __init__(self, color, width, height, ini_x, ini_y):
        super(Block, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.radius = 100
        self.angel = 0
        self.speed = 1
        self.ini_x = ini_x
        self.ini_y = ini_y
    def update(self):
        deg_rad = math.radians(self.angel)
        cter_x = self.ini_x + self.radius
        cter_y = self.ini_y
        self.rect.x = cter_x - (self.radius * round(math.cos(deg_rad),5))
        self.rect.y = cter_y - self.radius * round(math.sin(deg_rad), 5)
        self.angel += self.speed
        print self.rect.x


sprite_all = pygame.sprite.Group()

block1 = Block(BLACK,20,15,250, 250)
sprite_all.add(block1)


surface = pygame.display.set_mode([screen_width, screen_height])
done = False
clock = pygame.time.Clock()
pygame.init()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    sprite_all.update()
    surface.fill(WHITE)
    sprite_all.draw(surface)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

