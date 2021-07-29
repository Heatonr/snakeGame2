import turtle
import time
import random

# Creating objects and variables
head = turtle.Turtle()
food = turtle.Turtle()
body = []
window = turtle.Screen()
head.direction = "up"

score = 0

# Functions

def goUp():
    if(head.direction != "down"):
        head.direction = "up"

def goDown():
    if (head.direction != "up"):
        head.direction = "down"

def goLeft():
    if (head.direction != "right"):
        head.direction = "left"

def goRight():
    if (head.direction != "left"):
     head.direction = "right"

def move():
    xcor = head.xcor()
    ycor = head.ycor()

    if(head.direction == "up"):
        ycor = ycor + 20
    if(head.direction == "down"):
        ycor = ycor - 20
    if (head.direction == "left"):
        xcor = xcor - 20
    if (head.direction == "right"):
        xcor = xcor + 20

    head.goto(xcor, ycor)

def foodCollision(score):
    headX = head.xcor()
    headY = head.ycor()
    foodX = food.xcor()
    foodY = food.ycor()

    if(abs(headX - foodX) < 20 and abs(headY - foodY) < 20):
        score += 1
        food.goto(random.randint(-460,460), random.randint(-385,385))

        bodyPart = turtle.Turtle()
        bodyPart.shape("square")
        bodyPart.color("aquamarine")
        bodyPart.penup()
        bodyPart.speed(0)
        body.append(bodyPart)

    return score

def segmentMove():

    i = len(body) - 1
    if(len(body) > 1):
        while(i > 0):
            body[i].goto(body[i - 1].xcor(), body[i - 1].ycor())
            i = i - 1
    if(len(body) > 0):
        body[0].goto(head.xcor(), head.ycor())

def collision():
    if(abs(head.xcor()) >= 480 or abs(head.ycor()) >= 400):
        time.sleep(3)
        i = len(body) - 1
        while(i >= 0):
            body[i].color("black")
            body.remove(body[i])
            window.update()
            i -= 1
        head.goto(0,0)
        window.update()
        time.sleep(1)

    for segment in body:
        if(abs(head.xcor() - segment.xcor()) < 20 and abs(head.ycor() - segment.ycor()) < 20):
            time.sleep(3)
            i = len(body) - 1
            while (i >= 0):
                body[i].color("black")
                body.remove(body[i])
                window.update()
                i -= 1
            head.goto(0, 0)
            window.update()
            time.sleep(1)

# Setting up the window
window.title("Snake Game")
window.bgcolor("black")
window.screensize(500,500)
window.tracer(0)

window.listen()
window.onkeypress(goUp, "w")
window.onkeypress(goDown, "s")
window.onkeypress(goLeft, "a")
window.onkeypress(goRight, "d")

# Setting up the head object
head.shape("square")
head.color("aquamarine")
head.penup()
head.speed(0)

# Setting up the food object
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(random.randint(-460, 460), random.randint(-385, 385))

while(True):
    score = foodCollision(score)
    collision()
    segmentMove()
    move()
    window.update()
    time.sleep(0.05)