import turtle
window = turtle.Screen()
alex = turtle.Turtle()
alex.penup()
alex.goto(-150, -80)
alex.pendown()
def koch_draw(length, order = 2):

	if order == 0:
		alex.forward(length)
	else:
		koch_draw(length / 3, order - 1)
		alex.left(60)
		koch_draw(length / 3, order - 1)
		alex.left(-120)
		koch_draw(length / 3, order - 1)
		alex.left(60)
		koch_draw(length / 3, order - 1)

def ex_koch(eorder,length):

	if eorder == 0:
		koch_draw(length)
	else:
		ex_koch(eorder - 1, length)
		alex.right(120)
		ex_koch(eorder - 1, length)
		alex.right(120)
		ex_koch(eorder - 1, length)
		alex.right(120)
ex_koch(1, 180)


turtle.mainloop()