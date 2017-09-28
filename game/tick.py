import pygame, time
gravity = 0.01

class Sprite(object):
	def __init__(self, img, target_posn):
		self.image = img
		self.target_posn = target_posn
		target_x, target_y = target_posn
		self.posn = (target_x, 0)
		self.y_velocity = 0

	def update(self):
		(x, y) = self.posn
		target_x, target_y = self.target_posn
		self.y_velocity += gravity
		new_y_posn = y + self.y_velocity
		dist_to_go = target_y - new_y_posn
		if dist_to_go < 0:
			self.y_velocity = -0.65 * self.y_velocity
			new_y_posn = target_y + dist_to_go
		self.posn = (x, new_y_posn)

	def draw(self, target_surface):
		target_surface.blit(self.image, self.posn)

	def handle_click(self):
		self.y_velocity += 0.3

	def contains_point(self, x, y):
		posn_x, posn_y = self.posn
		pic_width = self.image.get_width()
		pic_height = self.image.get_height()
		return x >= posn_x and x < posn_x + pic_width and y >= posn_y and y < posn_y + pic_height


class Dukesprite(object):
	def __init__(self, img, target_posn):
		self.image = img
		self.posn = target_posn
		self.should_change= 0
		self.frame_show_num = 0
		self.area = (self.frame_show_num*50,0,50,self.image.get_height())
		self.count = 0
	def update(self):
		if self.should_change == 1:
			self.count += 1
			div1 = self.count % 60
			self.frame_show_num = div1 // 6
			self.area = (self.frame_show_num*50, 0, 50, self.image.get_height())
			if div1 == 0:
				self.frame_show_num = 0
				self.should_change = 0 
				self.count = 0


	def draw(self, target_surface):
		target_surface.blit(self.image, self.posn, self.area)

	def contains_point(self, x, y):
		posn_x, posn_y = self.posn
		pic_width = 50
		pic_height = self.image.get_height()
		return x >= posn_x and x < posn_x + pic_width and y >= posn_y and y < posn_y + pic_height

	def handle_click(self):
		self.should_change = 1
		






def chess_board(the_board):
	pygame.init()
	surface_sz = 480
	should_change = 0
	my_pic = pygame.image.load('cutie.png')
	duke_pic = pygame.image.load('duke_spritesheet.png')
	colors = [(255,0,0),(0,0,0)]
	n = len(the_board)
	sq_sz = surface_sz / n
	surface_sz = sq_sz * n
	all_sprites = []
	for i,v in enumerate(the_board):
			a_sprite = Sprite(my_pic, (i*sq_sz, v*sq_sz))
			all_sprites.append(a_sprite)
	duke_sprite1 = Dukesprite(duke_pic, (2*sq_sz, 2*sq_sz))
	duke_sprite2 = Dukesprite(duke_pic, (3*sq_sz, 3*sq_sz))
	all_sprites.append(duke_sprite1)
	all_sprites.append(duke_sprite2)
	surface = pygame.display.set_mode((surface_sz, surface_sz))
	frame_count = 0
	frame_rate = 0
	t0 = time.time()
	count = 0
	while True:

		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			break;
		if ev.type == pygame.KEYDOWN:
			key = ev.dict['key']
			if key == ord('r'):
				colors[0] = (255,0,0)
			if key == ord('g'):
				colors[0] = (0,255,0)
			if key == ord('b'):
				colors[0] = (0,0,255)
		if ev.type == pygame.MOUSEBUTTONDOWN:
			pos = ev.dict['pos']
			(x, y) = pos
			for sprite in all_sprites:
				(sprite_x, sprite_y) = sprite.posn
				if sprite.contains_point(x, y): 
					sprite.handle_click()
		for row in range(n):
			c_index = row % 2
			for col in range(n):
				the_square = (row*sq_sz, col*sq_sz, sq_sz, sq_sz)
				surface.fill(colors[c_index], the_square)
				c_index = (c_index + 1) % 2
		for sprite in all_sprites:
			sprite.draw(surface)
		for sprite in all_sprites:
			sprite.update()
		pygame.display.flip()
		clock = pygame.time.Clock()
		clock.tick(60)
	pygame.quit()

chess_board([1,2,3,4,5,6,7])
