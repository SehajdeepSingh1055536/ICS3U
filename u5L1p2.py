import turtle

t = turtle.Turtle()

for i in range(3):
  t.forward(100)
  t.left(120)
  # this code will end up making triangle.

# modify
import turtle

t = turtle.Turtle()

for i in range(60):
  t.forward(100)
  t.left(123)
# The code work but it has 3 degree error. instead of making triangle the lines start making another lines because of 3 degree error.

# modify2
import turtle
t = turtle.Turtle()
for i in range(80):
    t.forward(100)
    t.left(93) # Slight over-turn to create a spiral
    
    
import turtle
t = turtle.Turtle()
for i in range(80):
    t.forward(100)
    t.left(87) # Slight under-turn to create a spiral 
