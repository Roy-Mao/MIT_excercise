import pygame
import random
class Sprite(pygame.sprite.Sprite):
	def __init__(self, img, target_pos):
		super(Sprite, self).__init__()
		self.image = img
		self.target_pos = target_pos
		self.target_x = target_pos[0]
		self.target_y = target_pos[1]
all_sprites_list = 

pygame.init()
alist = [1,2,3,4,5,6,7,8]
RED = [255, 0, 0]
BLACK = [0, 0, 0]
colors = [RED, BLACK]
done = False
SCREEN_SZ = 480
cute_image = pygame.image.load('cutie.png')
rc_index = 0
alength = len(alist)
sq_sz = SCREEN_SZ // alength
SCREEN_SZ = sq_sz * alength
for s in range(alength):
	asprite = Sprite(cute_image, [s*sq_sz, s*sq_sz])

asprite = Sprite(cute_image, [sq_sz, sq_sz])
surface = pygame.display.set_mode([SCREEN_SZ, SCREEN_SZ])
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	for row in range(alength):
		c_index = rc_index
		for column in range (alength):
			the_square = [sq_sz * row, sq_sz * column, sq_sz, sq_sz]
			surface.fill(colors[c_index], the_square)
			c_index = (c_index + 1) % 2
		rc_index = (rc_index + 1) % 2
	surface.blit(cute_image, asprite.target_pos)
	pygame.display.flip()
pygame.quit()

