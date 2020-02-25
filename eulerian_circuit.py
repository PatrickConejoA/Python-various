import turtle as tt


## Definitions
tt.title('Eurelian Circuit')
window = tt.Screen()
tt.bgcolor("black")
t = tt.Turtle()
t.color("blue")
t.pensize(3)
t.speed(3)
ang = 120
amount = 6 # Amount of triangles
long_ = 15 # Long of the sides of the triangles

## Draw
for x in range(amount):
	# Draw triangle
	for y in range(3):
		t.right(ang)
		t.forward(long_)
	# Change direction
	if x != (amount-1):
		t.right(60)
		t.forward(long_)
		long_ *= 2

## Solve
t.color("green")
t.right(ang)
t.speed(1)
t.dot(10)

# Getting in
for x in range(amount):
	for y in range(2):
		t.forward(long_)
		t.right(ang)
	if x != (amount-1):
		long_ = long_ / 2
		t.forward(long_)
		t.right(ang)
		ang = ang * -1

# Getting out
for x in range(amount):
	ang = ang * -1
	t.forward(long_)
	if x != (amount-1):
		t.right(ang)
	if x != 0:
		long_ = long_ * 2

window.exitonclick() # Don't close when finish

# It draws a graph and then proceeds to create a eulerian circuit
# It just follows a pattern.
