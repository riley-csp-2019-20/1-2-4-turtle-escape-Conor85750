import turtle as trtl
import random

maze_rat = trtl.Turtle()
maze_rat.left(90)
maze_rat.ht()
maze_rat.pensize(5)
maze_rat.speed(0)
wall_width = 20
door_width = 15
barrier_width = 20
player = trtl.Turtle()
player.penup()
player.goto(0,-50)
player.pendown()
player.pencolor("green")
player.speed(0)
player.pensize(10)
# making the maze

for i in range(32):

    if (i > 4):
        door = random.randint(door_width, wall_width - door_width)
        barrier = random.randint(door_width, wall_width - door_width)
        if door < barrier:
            maze_rat.forward(door)
            #draw door
            maze_rat.penup()
            maze_rat.forward(door_width)
            maze_rat.pendown()

            maze_rat.forward(barrier - door - door_width)

            #barrier
            maze_rat.left(90)
            maze_rat.forward(barrier_width)
            maze_rat.backward(barrier_width)
            maze_rat.right(90)

            maze_rat.forward(wall_width - barrier)
        else:
            maze_rat.forward(barrier)
            #draw barrier
            maze_rat.right(90)
            maze_rat.forward(barrier_width)
            maze_rat.backward(barrier_width)
            maze_rat.left(90)

            maze_rat.forward(door - barrier)
            #door
            maze_rat.penup()
            maze_rat.forward(door_width)
            maze_rat.pendown()

            maze_rat.forward(wall_width - door - door_width)

    maze_rat.left(90)
    wall_width += door_width



def Up():
    player.seth(90)
    player.forward(10)
def Down():
    player.seth(90)
    player.backward(10)
def Left():
    player.seth(90)
    player.left(90)
    player.forward(10)
def Right():
    player.seth(90)
    player.right(90)
    player.forward(10)
wn = trtl.Screen()

wn.onkeypress(Up,"Up")
wn.onkeypress(Down,"Down")
wn.onkeypress(Left,"Left")
wn.onkeypress(Right,"Right")
wn.listen()

wn.mainloop()



