import turtle
import time
from random import *
def happyFace(x, y):
    t.penup()
    t.home()
    t.goto(x,y)
    t.color('black', 'yellow')
    t.pensize(10)
    t.pendown()
    t.begin_fill()
    for i in range(36):
        t.forward(30)
        t.left(10)
    t.end_fill()
    t.penup()

def drawEye(x, y):
    t.penup()
    t.home()
    t.goto(x,y)
    t.color('black')
    t.pensize(25)
    t.pendown()
    t.dot()
    t.penup()

def drawNose(x, y):
    t.penup()
    t.home()
    t.goto(x,y)
    t.color('black')
    t.pensize(30)
    t.pendown()
    t.dot()
    t.penup()

def drawMouth(x, y):
    t.penup()
    t.home()
    t.goto(x,y)
    t.color('black')
    t.pensize(10)
    t.pendown()
    t.right(60)
    t.circle(90, 120)
    t.penup()

def drawMouth2(x, y):
    t.penup()
    t.home()
    t.goto(x,y)
    t.forward(150)
    t.color('black')
    t.pensize(10)
    t.left(120)
    t.pendown()
    t.circle(90, 120)
    t.penup()

def drawMouth3(x, y):
    t.penup()
    t.home()
    t.goto(x,y)
    t.color('black')
    t.pensize(10)
    t.pendown()
    t.forward(150)
    t.penup()
    
t = turtle
t.speed(0)
count = 0

while True:
    t.home()
    happyFace(0,0)
    drawEye(-50, 250)
    drawEye(70, 250)
    drawNose(15, 150)
    if count%3 == 0:
        drawMouth(-60, 90)
    elif count%3 == 1:
        drawMouth3(-60, 90)
    else:
        drawMouth2(-60, 40)
    
    count += 1
    t.clear()


t.hideturtle()
t.done()
