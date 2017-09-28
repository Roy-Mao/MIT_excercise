#6.24
import pygame
import random
#-----Some Constant Including: 1.Screen size  2.Color RGB  3.A screen surface-----
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BLOCK_SZ = 20
PLAYER_WIDTH = BLOCK_SZ * 2
PLAYER_HEIGHT = BLOCK_SZ
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])



def key_press_action(obj):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        obj.rect.x += obj.velocity
    if pressed[pygame.K_LEFT]:
        obj.rect.x -= obj.velocity
    if pressed[pygame.K_UP]:
        obj.rect.y -= obj.velocity
    if pressed[pygame.K_DOWN]:
        obj.rect.y += obj.velocity
    lunch_pos = (obj.rect.x, obj.rect.y)
    return lunch_pos



#-----Block Class----
# Instance attribute include a position(x, y coordinates) and color. The block image is a surface object
# Do not forget using the get_rect to get the rect coordinates of the surface object
# 
class Block(pygame.sprite.Sprite):
    def __init__(self, target_x, target_y, color):
        super(Block, self).__init__()
        self.color = color
        self.image = pygame.Surface([BLOCK_SZ, BLOCK_SZ])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = target_x
        self.rect.y = target_y
        self.velocity = 1

    def update(self):
        self.rect.x += self.velocity
        if self.rect.x == SCREEN_WIDTH - BLOCK_SZ:
            self.velocity = -1
        if self.rect.x == 0:
            self.velocity = 1


# Player is a subclass of Block. It inherits the same attribute from Block class, including surface object coordinates, color and size
# The unique feature of Player subclass is that it has a different update methods. That is the movement of Player object is different
# from the Block instance move pattern
class Player(Block):
    def __init__(self, target_x, target_y):
        super(Player, self).__init__(target_x, target_y, BLACK)
        self.image = pygame.Surface([PLAYER_WIDTH, BLOCK_SZ])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = target_x
        self.rect.y = target_y
        self.velocity = 3

    def update(self):
        current_pos = key_press_action(self)
        if self.rect.x > SCREEN_WIDTH - PLAYER_WIDTH:
            self.rect.x = SCREEN_WIDTH - PLAYER_WIDTH
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > SCREEN_HEIGHT - PLAYER_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT

class Bullet(Player):
    def __init__(self, target_x, target_y):
        super(Bullet, self).__init__(target_x, target_y)
        self.image = pygame.Surface([BULLET_WIDTH, BULLET_HEIGHT])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = target_x
        self.rect.y = target_y
        self.b_speed = 4
        self.should_lunch = False
    def update(self):
        if self.should_lunch == True:
            self.rect.y -= self.b_speed
            if self.rect.y < 0:
                self.kill()
                self.should_lunch = False
        else:
            current_pos = key_press_action(self)
            if self.rect.x > SCREEN_WIDTH - PLAYER_WIDTH // 2:
                self.rect.x = SCREEN_WIDTH - PLAYER_WIDTH // 2
            if self.rect.x < PLAYER_WIDTH // 2:
                self.rect.x = PLAYER_WIDTH // 2
            if self.rect.y > SCREEN_HEIGHT - PLAYER_HEIGHT:
                self.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT


#-----Game Class------
# I initialize many Instance attributes of Game instance, including: 
# 1.weather the game is over, default value is False
# 2.the initial score of the game should be 0
# 3.Initiate 4 sprites Group to group a.red_blocks b.gree_blocks c.all_blocks(exclude the player) d.all_sprites(include the player block)
# 4.create all blocks excluding the player block
# 5.add all_blocks into all_sprites group and add player_block too..NOTE: No assignment '=' instead use add method
class Game(object):
    def __init__(self):
        self.game_over = False
        self.scores = 0
        self.all_red_blocks = pygame.sprite.Group()
        self.all_green_blocks = pygame.sprite.Group()
        self.all_blocks = pygame.sprite.Group()
        self.all_bullets = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.OrderedUpdates()
        memo_pos = []
        go_on = True
        while go_on:
            found = False
            random_x = random.randrange(SCREEN_WIDTH - BLOCK_SZ)
            random_y = random.randrange(SCREEN_HEIGHT - BLOCK_SZ - 100)
            for element in memo_pos:
                if random_x > element[0] - BLOCK_SZ and random_x < element[0] + BLOCK_SZ and random_y > element[1] - BLOCK_SZ and random_y < element[1] + BLOCK_SZ:
                    found = True
                    break
            if not found:
                pos = (random_x, random_y)
                memo_pos.append(pos)
                if len(memo_pos) <= 10:
                    gblock = Block(random_x, random_y, GREEN)
                    self.all_green_blocks.add(gblock)
                    self.all_blocks.add(gblock)
                elif len(memo_pos) == 41:
                    go_on = False
                else:
                    rblock = Block(random_x, random_y, RED)
                    self.all_red_blocks.add(rblock)
                    self.all_blocks.add(rblock)
        self.all_sprites.add(self.all_blocks)

        self.mblock = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - BLOCK_SZ)
        self.all_sprites.add(self.mblock)
        self.init_bullet = Bullet(self.mblock.rect.x + PLAYER_WIDTH // 2, self.mblock.rect.y)
        self.all_bullets.add(self.init_bullet)
        self.all_sprites.add(self.init_bullet)

    def create_bullet(self):
        abullet = Bullet(self.mblock.rect.x + PLAYER_WIDTH // 2, self.mblock.rect.y)
        return abullet


    def process_events(self):
        done = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for sprite in self.all_sprites:
                        if type(sprite) == type(self.init_bullet):
                            sprite.should_lunch = True
                    abullet = self.create_bullet()
                    self.all_bullets.add(abullet)
                    self.all_sprites.add(abullet)
        return done
        


#Run the game.Firstly update the position of the player block(mblock)
# Then use the sprite.Group spritecollide method to check if mblock collides with any sprite in the all_blocks group
# self.scores add up 1 if there is any colliding sprite returned to the blocks_hit_list. In other words, if the len(blocks_hit_list) is 
# 1 then self.scores will add up 1
    def run_logic(self):
        self.all_sprites.update()
        for bullet in self.all_bullets:
            red_hit_list = pygame.sprite.spritecollide(bullet, self.all_red_blocks, True)
            for block in red_hit_list:
                self.scores += 1
                bullet.kill()

            green_hit_list = pygame.sprite.spritecollide(bullet, self.all_green_blocks, True)
            for block in green_hit_list:
                self.scores -= 1
                bullet.kill()

# Show the frame. Create text and blit it onto the screen.all so use the draw() method of the sprite Group to draw all sprites
    def display_frame(self):
        font = pygame.font.SysFont('serifs', 25)
        text_score = font.render('Scores: {0}'.format(self.scores), True, BLACK)
        score_pos = [(SCREEN_WIDTH // 2 - text_score.get_width() // 2), 0]
        self.all_sprites.draw(screen)
        screen.blit(text_score, score_pos)

#-----main game loop-----
def main():
    done = False
    pygame.init()
    clock = pygame.time.Clock()
    mgame = Game()
    while not done:
        done = mgame.process_events()
        screen.fill(WHITE)
        mgame.run_logic()
        mgame.display_frame()
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()