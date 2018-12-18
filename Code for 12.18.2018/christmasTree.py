## Christmas Tree Project
## Author: nmessa
## Date: 12/20/2016

import turtle

screen = turtle.Screen()
screen.setup(800,600)

#define a circle
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed(0)
circle.up()

#define a square
square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed(0)
square.up()

#go to top of tree and put a red ornament
circle.goto(0,280)
circle.stamp()

#generate the tree
# i represents the row and j represents the column
k = 0
for i in range(1, 17):
    y = 30*i
    for j in range(i-k):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()

    #place a red ornament
    if i % 4 == 0:
        x =  30*(j+1)
        circle.color('red')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()        
        k += 2

    #place a yellow ornament
    if i % 4 == 3:
        x =  30*(j+1)
        circle.color('yellow')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp() 

#Draw the stump
square.color('brown')
for i in range(17,20):
    y = 30*i
    for j in range(3):    
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()        
        
turtle.exitonclick()
