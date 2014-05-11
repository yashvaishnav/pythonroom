import turtle

t = turtle.Turtle()
t.shape("circle")

n = int(input("How many legs should this sprite have?"))
angle = 360 / n

for i in range(n):
	# draw the leg
	t.right(angle)
	t.forward(65)
	t.stamp()
	
	# turn around, go back to the middle & reset
	t.right(180)
	t.forward(65)
	t.right(180)