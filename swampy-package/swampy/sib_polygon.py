# Polygon excercise from Week 0

# Name:


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

def polygon(turt, lengthturt, n):
	form(turt, lengthturt, 360, n)

#polygon(bob, 25, 4)
#polygon(bob, 25, 5)
#polygon(bob, 25, 6)
#polygon(bob, 25, 7)
#polygon(bob, 25, 8)
#polygon(bob, 25, 9)

def circle (turt, radius):
	form(turt, radius, 360, 360)
	


def arc (turt, radius, theta):
	form(turt, radius, theta, 360)
	

def form (turt, radius, theta, shape):
	import math
	x = 2.0*radius*radius*math.pi
	print x
	for i in range(theta):
		fd(turt, x/360.0)
		lt(turt, 360.0/shape)


polygon(bob, 40, 5)
#arc(bob, 5, 90)
#circle(bob, 5)



wait_for_user()					
