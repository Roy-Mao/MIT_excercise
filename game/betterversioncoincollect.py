# 1254  108
import pygame, random

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
screen_width = 700
screen_height = 400
score = 0

class Block(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super(Block, self).__init__()
		self.color = color
		self.width = width
		self.height = height
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.y_velocity = 1
		self.x_velocity = 0

	def update(self):
		self.rect.y += self.y_velocity
		if self.rect.y > screen_height - self.height or self.rect.y < 0:
			self.y_velocity = -1 * self.y_velocity

	def circle_update(self, length):
		center_pos_x = self.rect.x + length
		center_pos_y = self.rect.y



		

sprite_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
	asprite = Block(BLACK, 20, 15)
	asprite.rect.x = random.randrange(screen_width - asprite.width)
	asprite.rect.y = random.randrange(screen_height - asprite.height)

	sprite_list.add(asprite)
	all_sprite_list.add(asprite)
player = Block(RED, 20, 15)
all_sprite_list.add(player)

pygame.init()
surface = pygame.display.set_mode([screen_width, screen_height])
done = False
clock = pygame.time.Clock()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pos = pygame.mouse.get_pos()
	player.rect.x = pos[0]
	player.rect.y = pos[1]
	block_hit_list = pygame.sprite.spritecollide(player, sprite_list, True)
	for b in block_hit_list:
		score += 1
		print 
	sprite_list.update()
	surface.fill(WHITE)
	all_sprite_list.draw(surface)
	pygame.display.flip()
	clock.tick(60)
pygame.quit()
