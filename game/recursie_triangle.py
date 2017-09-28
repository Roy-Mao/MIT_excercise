import pygame, math
def draw_tree(order, surface, color, t_sz, posn, direct, direct_adjut):
	length = 0.27 * t_sz
	t_sz = 0.73 * t_sz
	(u, v) = posn 
	delta_x = length * math.cos(direct)
	delta_y = length * math.sin(direct)
	new_posn = (u + delta_x, v + delta_y)
	pygame.draw.line(surface, color, posn, new_posn)
	if order > 0:
		draw_tree(order - 1, surface, color, t_sz, new_posn, direct + direct_adjut, direct_adjut)
		draw_tree(order - 1, surface, color, t_sz, new_posn, direct - direct_adjut, direct_adjut)

		

pygame.init()
surface_sz = 500
surface = pygame.display.set_mode((surface_sz, surface_sz))
while True:
	ev = pygame.event.poll()
	if ev.type == pygame.QUIT:
		break;
	draw_tree(8,surface, (255,0,0), (surface_sz * 0.85), (surface_sz / 2, surface_sz - 50), (-math.pi / 2 ), (math.pi/180 * 30))
	pygame.display.flip()
pygame.quit()
