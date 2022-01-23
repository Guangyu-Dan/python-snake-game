import random
from turtle import Turtle, Screen
import time
screen = Screen()
screen_width = 800
screen_height = 800
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("My snack game")
screen.tracer(0)
allPos = [(0,0),(-20,0),(-40,0)]
segments=[]

for pos in allPos:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(pos)
    segments.append(segment)


def move_up():
    if segments[0].heading() == 0:segments[0].left(90)
    elif segments[0].heading() == 180:segments[0].right(90)
def move_down():
    if segments[0].heading() == 0:segments[0].right(90)
    elif segments[0].heading() == 180:segments[0].left(90)
def move_left():
    if segments[0].heading() == 90:segments[0].left(90)
    elif segments[0].heading() == 270:segments[0].right(90)
def move_right():
    if segments[0].heading() == 90:segments[0].right(90)
    elif segments[0].heading() == 270:segments[0].left(90)


xpos = random.randint(-screen_width/40,screen_width/40)*20
ypos = random.randint(-screen_height/40,screen_height/40)*20
seed = Turtle("square")
seed.color("yellow")
seed.penup()
seed.goto(xpos,ypos)

def update_seed():
    xpos = random.randint(-screen_width/40,screen_width/40)*20
    ypos = random.randint(-screen_height/40,screen_height/40)*20
    seed.goto(xpos,ypos)
    return seed


segments[0].speed("fastest")
game_is_on = True
ate_seed = True
while game_is_on:
    screen.update()
    if ate_seed:
        seed = update_seed()
        ate_seed = False
    time.sleep(.2)

    old_x = segments[-1].xcor()
    old_y = segments[-1].ycor()
    for seg_num in range(len(segments)-1,0,-1):
        new_x = int(segments[seg_num-1].xcor())
        new_y = int(segments[seg_num-1].ycor())
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

    # ---------------- hit wall ------------------------#
    if abs(segments[0].xcor())>screen_width/2 or abs(segments[0].ycor())>screen_height/2:
        game_is_on = False
    # ---------------- hit itself ----------------------#
    if sum([abs(segments[i].xcor()-segments[0].xcor())<1 and abs(segments[i].ycor()-segments[0].ycor())<1 for i in range(1,len(segments))]):
        game_is_on = False
    # ---------------- ate seed ------------------------#
    if abs(seed.xcor()-segments[0].xcor())<1 and abs(seed.ycor()-segments[0].ycor())<1:
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(old_x, old_y)
        segments.append(segment)
        seed.clear()
        ate_seed = True

    print(seed.xcor(),seed.ycor(),segments[0].xcor(),segments[0].ycor())

    screen.listen()
    screen.onkey(key="Up", fun=move_up)
    screen.onkey(key="Down", fun=move_down)
    screen.onkey(key="Right", fun=move_right)
    screen.onkey(key="Left", fun=move_left)



if not game_is_on:
    lose = Turtle("square")
    lose.goto(0, 0)
    lose.color("white")
    lose.write('Game over', align='center', font=('Arial', 50,'normal'))





screen.exitonclick()