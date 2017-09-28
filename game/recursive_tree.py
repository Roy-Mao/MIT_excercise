import pygame, math
def draw_tree(order, pos, dire, t_sz, dire_adj, surface, color = (255,0,0), deep = 0):
    colors = [(255,0,0), (0,255,0), (0,0,255)]
    c_index = deep % 3
    color = colors[c_index]
    (u, v) = pos
    length = 0.29 * t_sz
    delta_x = length * math.cos(dire)
    delta_y = length * math.sin(dire)
    new_pos = (u + delta_x, v + delta_y)
    pygame.draw.line(surface, color, pos, new_pos)
    if order > 0:
        t_sz = 0.68 * t_sz
        draw_tree(order - 1, new_pos, dire + dire_adj, t_sz, dire_adj, surface, color, deep + 1)
        draw_tree(order -1 , new_pos, dire - dire_adj, t_sz, dire_adj, surface, color, deep + 1)

pygame.init()
surface_sz = 700
surface = pygame.display.set_mode((surface_sz,surface_sz))
my_clock = pygame.time.Clock()
while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        break
    draw_tree(8,(surface_sz/2.0, surface_sz-50), (-math.pi/2), surface_sz, (math.pi/180*45),surface)
    pygame.display.flip()
    my_clock.tick(60)
pygame.quit()
