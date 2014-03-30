# Flower excercise (4.2) from Week 0

# Name:


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
import math


# This is where you put code to move bob
def polyline (t, n, length, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def arc (t, r, angle):
	arc_length = 2 * math.pi * r * angle/360
	n = int (arc_length /3)+1
	step_length = arc_length/n
	step_angle = float(angle) / n
	polyline(t, n, step_length, step_angle)



def petal (t, r, angle):
	for i in range (2):
		arc(t, r, angle)
		lt (t, 180-angle)

def flower(t, n, r, angle):
	for i in range (n):
		petal (t, r, angle)
		lt(t, 360.0/n)

pu(bob)
fd(bob, -100)
pd(bob)
flower (bob, 7, 60.0, 60.0)

pu(bob)
fd(bob, 100)
pd(bob)

flower(bob, 10, 40.0, 80.0)

pu(bob)
fd(bob, 100)
pd(bob)

flower(bob, 20, 140.0, 20.0)
wait_for_user()					

