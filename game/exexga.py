import pygame
pygame.init()
alist = [1,2,3,4,5,6,7,8]
surface_sz = 480
n = len(alist)
sq_sz = surface_sz / n
surface_sz = sq_sz * n
surface = pygame.display.set_mode((surface_sz, surface_sz))
while True:
	ev = pygame.event.poll()
	if ev.type == pygame.QUIT:
		break
	pygame.display.flip()
pygame.quit()






