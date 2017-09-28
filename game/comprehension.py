import pygame
#-----some CONSTANTS------
done = False
surface_sz = 255
surface = pygame.display.set_mode([surface_sz, surface_sz])
width = 20
height = 20
margin = 5
WHITE = [255, 255, 255]
BLACK = [0,0,0]
GREEN = [0, 255, 0]
colors = [WHITE, GREEN]
grid = [[0 for x in range(10)]for y in range(10)]
grid[1][5] = 1

#------Useful Functions-------
def convert_to_int(atuple):
	global margin, width, height
	x_num = (atuple[0] - margin) // (width + margin)
	y_num = (atuple[1] - margin) // (width + margin)
	return (x_num, y_num)
# always for get this
clock = pygame.time.Clock()
pygame.init()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			#can also do pos = pygame.mouse.get_pos()
			mouse_pos = event.dict['pos']
			atuple = convert_to_int(mouse_pos)
			grid[atuple[1]][atuple[0]] = 1
			print 'Row: ' + str(atuple[1]) + ' Column: ' + str(atuple[0])
	# This is also very important but often forgotten
	surface.fill(BLACK)
	for column in range(10):
		for row in range(10):
			column_pos = margin + column * (width + margin)
			row_pos = margin + row * (height + margin)
			place = [column_pos, row_pos, width, height]
			if grid[row][column] == 1:
				color = colors[1]
			else:
				color = colors[0]
			surface.fill(color, place)
	clock.tick()
	pygame.display.flip()

pygame.quit()
