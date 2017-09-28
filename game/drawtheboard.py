#test [6, 4, 2, 0, 5, 7, 1, 3]
import pygame, time
gravity = 0.01

class QueenSprite(object):
	def __init__(self, img, target_posn):
		self.image = img
		self.target_posn = target_posn
		(x, y) = target_posn
		self.posn = (x, 0)
		self.y_velocity = 0

	def update(self):
		(x, y) = self.posn
		self.y_velocity += gravity
		new_y_posn = y + self.y_velocity
		(tartet_x, target_y) = self.target_posn
		dist_to_go = target_y - new_y_posn
		if dist_to_go < 0:
			self.y_velocity = -0.65 * self.y_velocity
			new_y_posn = target_y + dist_to_go
		self.posn = (x, new_y_posn)

	def draw(self, target_surface):
		target_surface.blit(self.image, self.posn)

	def contains_point(self, pt):
		(my_x, my_y) = self.posn
		my_width = self.image.get_width()
		my_height = self.image.get_height()
		(x, y) = pt
		return (x >= my_x and x < my_x + my_width and y >= my_y and y < my_y + my_height)

	def handle_click(self):
		self.y_velocity += -0.3

class DukeSprite(object):
	def __init__(self, img, target_posn):
		self.image = img
		self.posn = target_posn
		self.anim_frame_count = 0
		self.curr_patch_num = 0
	def draw(self, target_surface,):
		patch_rect = (self.curr_patch_num * 50, 0, 50, self.image.get_height())
		target_surface.blit(self.image, self.posn, patch_rect)

	def update(self):
		if self.anim_frame_count > 0:
			self.anim_frame_count = (self.anim_frame_count + 1) % 60
			self.curr_patch_num = self.anim_frame_count // 6

	def handle_click(self):
		if self.anim_frame_count == 0:
			self.anim_frame_count = 5

	def contains_point(self, pt):
		(x, y) = pt
		(duke_x, duke_y) = self.posn
		duke_height = self.image.get_height()
		duke_width = self.image.get_width()
		return (x >= duke_x and x < duke_x + 50 and y >= duke_y and y < duke_y + duke_height)



def draw_board(the_board):
	my_clock = pygame.time.Clock()
	frame_count = 0
	frame_rate = 0
	n = len(the_board)
	t0 = time.clock()
	my_pic = pygame.image.load('cutie.png')
	duke_sprite_shit = pygame.image.load('duke_spritesheet.png')
	all_sprites = []
	pygame.init()
	colors = [(255,0,0),(0,0,0)]
	surface_sz = 480
	sq_sz = surface_sz // n
	pic_offset = (sq_sz - my_pic.get_width()) / 2
	duke_offset_x = (sq_sz - 50) / 2 + 3
	duke_offset_y = (sq_sz - duke_sprite_shit.get_height()) / 2 - 3
	surface_sz = sq_sz * n
	duke1 = DukeSprite(duke_sprite_shit, (sq_sz*2 + duke_offset_x, 0 + duke_offset_y))
	duke2 = DukeSprite(duke_sprite_shit,(sq_sz*5 + duke_offset_x, sq_sz + duke_offset_y))
	all_sprites.append(duke1)
	all_sprites.append(duke2)
	for i, v in enumerate(the_board):
		a_queen = QueenSprite(my_pic, (i*sq_sz + pic_offset, v*sq_sz + pic_offset))
		all_sprites.append(a_queen)
	surface = pygame.display.set_mode((surface_sz,surface_sz))
	while True:
		frame_count += 1
		if frame_count % 500 == 0:
			t1 = time.clock()
			td = t1 - t0
			print td
			frame_rate = frame_count / td
			t0 = t1
			frame_count = 0
			print frame_rate
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			break;
		if ev.type == pygame.KEYDOWN:
			key = ev.dict['key']
			if key == 27:
				break
			if key == ord('r'):
				colors[0] = (255,0,0)
			elif key == ord('g'):
				colors[0] = (0,255,0)
			elif key == ord('b'):
				colors[0] = (0,0,255)
		if ev.type == pygame.MOUSEBUTTONDOWN:
			posn_of_click = ev.dict['pos']
			for sprite in all_sprites:
				if sprite.contains_point(posn_of_click):
					sprite.handle_click()
		for sprite in all_sprites:
			sprite.update()
		for row in range(n):
			c_index = row % 2
			for col in range(n):
				the_square = (row*sq_sz, col*sq_sz, sq_sz, sq_sz)
				surface.fill(colors[c_index], the_square)
				c_index = (c_index + 1) % 2
		for sprite in all_sprites:
			sprite.draw(surface)
		my_clock.tick(60)
		pygame.display.flip()

	pygame.quit()
draw_board([1,2,3,4,5,6,7,8])


