import turtle
window = turtle.Screen()
alex = turtle.Turtle()
alex.penup()
alex.goto(-100, 0)
alex.pendown()
def tear(order, length):
	if order == 0:
		alex.forward(length)
	else:
		tear(order - 1, length / 2)
		alex.right(85)
		tear(order - 1, length / 2)
		alex.left(170)
		tear(order - 1, length / 2)
		alex.right(85)
		tear(order - 1, length / 2)

def tear_sqaure(order, length):
		tear(order, length)
		alex.right(90)
		tear(order, length)
		alex.right(90)
		tear(order, length)
		alex.right(90)
		tear(order, length)
tear_sqaure(3, 250)
tear_sqaure(0, 250)

turtle.mainloop()