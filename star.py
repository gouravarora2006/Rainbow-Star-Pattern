import turtle
sc=turtle.Screen()
sc.setup(600,600)
spiral=turtle.Turtle()
spiral.speed(5)
sc.bgcolor("black")
col=["yellow","blue","white","pink"]
c=0
for i in range(50):
	spiral.forward(i*10)
	spiral.right(144)
	spiral.color(col[c])
	if c==3:
		c=0
	else:
			c+=1
	
