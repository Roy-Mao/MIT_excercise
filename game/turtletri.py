import turtle
window = turtle.Screen()
alex = turtle.Turtle()
alex.penup()
alex.bk(100)
alex.goto(-150, -100)
alex.pendown()
# def koch(order, length):
# 	if order == 0:
# 		alex.forward(length)
# 	else:
# 		koch(order - 1, length / 2)
# 		alex.right(85)
# 		koch(order - 1, length / 2)
# 		alex.left(170)
# 		koch(order - 1, length / 2)
# 		alex.right(85)
# 		koch(order - 1, length / 2)

# def e_koch(num):
# 	for n in range(num):
# 		koch(3,200)
# 		alex.right(90)
# e_koch(4)
def r_triangle(order, length):
	if order == 0:
		for i in range(3):
			alex.forward(length)
			alex.left(120)
	if order > 0:
		r_triangle(order - 1, length / 2)
		alex.forward(length / 2)
		r_triangle(order - 1, length / 2)
		alex.bk(length / 2)
		alex.left(60)
		alex.forward(length / 2)
		alex.right(60)
		r_triangle(order - 1, length / 2)
		alex.right(120)
		alex.forward(length / 2)
		alex.left(120)

r_triangle(5, 200)




turtle.mainloop()