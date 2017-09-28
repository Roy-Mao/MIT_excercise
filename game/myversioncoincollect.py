import pygame, random
class B_block(object):
	def __init__(self, color, x, y):
		self.width = 25
		self.height = 15
		self.x = x
		self.y = y
		self.color = color
def my_game():
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	RED = (255,0,0)
	done = False
	surface_sz = [500, 450]
	surface = pygame.display.set_mode(surface_sz)
	block_list = []
	sample_block = B_block(BLACK, 0, 0)
	my_block = B_block(RED, 0, 0)
	tot = 0
	for i in range(30):
		x = random.randrange(0,(surface_sz[0] - sample_block.width), sample_block.width)
		y = random.randrange(0,(surface_sz[1] - sample_block.height), sample_block.height)
		a_block = B_block(BLACK, x, y)

		block_list.append(a_block)

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		(m_x, m_y) = pygame.mouse.get_pos()
		if m_x > surface_sz[0] - my_block.width:
			m_x = surface_sz[0] - my_block.width
		if m_y > surface_sz[1] - my_block.height:
			m_y = surface_sz[1] - my_block.height
		my_block.x = m_x
		my_block.y = m_y
		surface.fill(WHITE)
		for block in block_list:
			if my_block.x > block.x and my_block.x < block.x + block.width and my_block.y > block.y and my_block.y < block.y + block.height:
				block_list.remove(block)
				tot += 1
				print tot
			pygame.draw.rect(surface, block.color, [block.x, block.y, block.width, block.height])
		pygame.draw.rect(surface, my_block.color, [my_block.x, my_block.y, my_block.width, my_block.height])
		pygame.display.flip()
	pygame.quit()

my_game()