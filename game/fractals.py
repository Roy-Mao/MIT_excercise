# 10.22
import pygame
# some constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
done = False
MOVE_DIST = 50
direct = [1, -1]
clock = pygame.time.Clock()
# recursive function
def draw_tree(order, length, center_x, center_y):
	if order == 0:
		for d in direct:
			pygame.draw.line(surface, BLACK, [center_x, center_y], [center_x + d * length, center_y])
			for i in direct:
				pygame.draw.line(surface, BLACK, [center_x + d * length, center_y],[center_x + d * length, center_y + i * length])
	if order > 0:
		draw_tree(0, length, center_x, center_y)
		draw_tree(order - 1, length * 0.45, center_x + length, center_y + length  )
		draw_tree(order - 1, length * 0.45, center_x + length, center_y - length  )
		draw_tree(order - 1, length * 0.45, center_x - length, center_y + length  )
		draw_tree(order - 1, length * 0.45, center_x - length, center_y - length  )








pygame.init()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	surface.fill(WHITE)
	draw_tree(3, 100, SCREEN_WIDTH / 2.0, SCREEN_HEIGHT / 2.0)
	




	clock.tick(60)
	pygame.display.flip()
pygame.quit()
