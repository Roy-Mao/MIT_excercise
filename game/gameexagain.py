import pygame
alist = [1,2,3,4,5,6,7,8]
gravity = 0.01
class Sprite(object):
	def __init__(self, img, target_posn):
		self.image = img
		self.target_posn = target_posn
		(self.target_x, self.target_y) = target_posn
		self.current_posn = (self.target_x, -5)
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.y_velocity = 0

	def update(self):
		(cx, cy) = self.current_posn
		self.y_velocity += gravity
		new_y = cy + self.y_velocity
		self.current_posn = (cx, new_y)
		if new_y > self.target_y:
			self.y_velocity = 0.65 * -self.y_velocity
			new_y = cy + self.y_velocity
			self.current_posn = (cx, new_y)

	def within(self, coords):
		coord_x, coord_y = coords
		current_x, current_y = self.current_posn
		return (coord_x >= current_x and coord_x < current_x + self.width and coord_y >= current_y and coord_y < current_y + self.height)


	def handle_click(self):
		self.y_velocity += 0.3

class Duke(object):
	def __init__(self, img, target_posn):
		self.image = img
		self.target_posn = target_posn
		self.current_posn = target_posn
		self.height = self.image.get_height()
		self.animate_frame_num = 0
		self.start_or_not = 0
		self.count = 0
	def update(self):
		if self.start_or_not == 1:
			self.count += 1
			div1 = self.count % 60
			print div1
			if div1 == 0:
				self.animate_frame_num = 0
				self.start_or_not = 0
				self.count = 0
			else:
				div2 = div1 % 6
				if div2 == 0:
					self.animate_frame_num += 1


	def within(self, coords):
		coord_x, coord_y = coords
		current_x, current_y = self.current_posn
		return (coord_x >= current_x and coord_x < current_x + 50 and coord_y >= current_y and coord_y < current_y + self.height)

	def handle_click(self):
		self.start_or_not = 1


def ex_game(alist):
	pygame.init()
	colors = [(255,0,0), (0,0,0)]
	my_pic = pygame.image.load('cutie.png')
	duke_pic = pygame.image.load('duke_spritesheet.png')
	pic_width = my_pic.get_width()
	pic_heigth = my_pic.get_height()
	duke_width = duke_pic.get_width()
	duke_height = duke_pic.get_height()
	surface_sz = 480
	n = len(alist)
	sq_sz = surface_sz / n
	pic_xa = (sq_sz - pic_width) / 2.0
	pic_ya = (sq_sz - pic_heigth) / 2.0
	duke_xa = (sq_sz - 43) / 2.0
	duke_ya = (sq_sz - duke_height) / 2.0
	sprites = []
	for i, v in enumerate(alist):
		asprite = Sprite(my_pic, (i * sq_sz + pic_xa, v * sq_sz + pic_ya))
		sprites.append(asprite)
	duke1 = Duke(duke_pic, (2 * sq_sz + duke_xa, 3 * sq_sz + duke_ya))
	duke2 = Duke(duke_pic, (3 * sq_sz + duke_xa, 6 * sq_sz + duke_ya))
	sprites.append(duke1)
	sprites.append(duke2)
	surface = pygame.display.set_mode((surface_sz, surface_sz))
	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			break
		if ev.type == pygame.KEYDOWN:
			key = ev.dict['key']
			if key == ord('r'):
				colors[0] = (255,0,0)
			elif key == ord('g'):
				colors[0] = (0,255,0)
			elif key == ord('b'):
				colors[0] = (0,0,255)
		if ev.type == pygame.MOUSEBUTTONDOWN:
			m_posn = ev.dict['pos']
			for sprite in sprites:
				if sprite.within(m_posn):
					sprite.handle_click()
		for row in range(n):
			c_index = row % 2
			for col in range(n):
				the_square = (row * sq_sz, col * sq_sz, sq_sz, sq_sz)
				surface.fill(colors[c_index], the_square)
				c_index = (c_index + 1) % 2
		for sprite in sprites:
			if type(sprite) == type(sprites[0]):
				surface.blit(sprite.image, sprite.current_posn)
			else:
				area = (sprite.animate_frame_num * 50, 0, 50, sprite.height)
				surface.blit(sprite.image, sprite.current_posn, area)
			sprite.update()

		pygame.display.flip()
		my_clock = pygame.time.Clock()
		my_clock.tick(60)
	pygame.quit()

ex_game([0,1,2,3,4,5,6,7])
