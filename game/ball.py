import pygame

def ex():
	radius = 50
	data1 = 2 * [radius * 2]
	data2 = 2 * (radius,)
	ball = pygame.Surface(data1)
	surface1 = pygame.display.set_mode((450,450))
	posn_x = 0
	posn_y = 0
	velocity_x = 10
	velocity_y = 5
	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			break
		surface1.fill((0,0,0))
		posn = (posn_x,posn_y)
		posn_x += velocity_x
		posn_y += velocity_y
		if posn_x > 350 or posn_x < 0:
			velocity_x *= -1
		if posn_y > 350 or posn_y < 0:
			velocity_y *= -1
		surface1.blit(ball, posn)
		pygame.draw.circle(ball, (0,0,255), 2 * (radius,), radius)
		pygame.display.flip()
	pygame.quit()


	