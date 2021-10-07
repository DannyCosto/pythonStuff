from turtle import *
screen = Screen()
screen.setup(800,800)
screen.colormode(255)
screen.bgcolor("black")
e = Turtle()
e.speed(0)
e.penup()
e.goto(-400,400)
length = 100
x = -400
def drawpixel(color):
  e.pendown()
  e.color(color)
  e.begin_fill()
  for i in range(4):
    e.fd(length)
    e.rt(90)
  e.end_fill()
  e.penup()
def drawpixel2(R, G, B):
  e.pendown()
  e.color(R, G, B)
  e.begin_fill()
  for i in range(4):
    e.fd(length)
    e.rt(90)
  e.end_fill()
  e.penup()

'''
1 = white
2 = tan
3 = tan
4 = red
5 = red
6 = black
7 = light blue

'''


grid = [[6,6,6,6,6,6,6,6],
        [6,4,4,4,4,4,6,6],
        [4,4,4,5,1,5,6,6],
        [4,6,4,2,2,2,6,6],
        [6,4,4,4,4,4,4,6],
        [6,4,4,2,2,2,4,6],
        [6,1,4,2,2,2,1,6],
        [6,6,6,3,6,3,6,6]]

for i in range(8):
  for j in range(8):
    color = grid[i][j]
    if color == 1:
      drawpixel("white")
    elif color == 2:
      drawpixel("tan")
    elif color == 3:
      drawpixel("red")
    elif color == 4:
      drawpixel("blue")
    elif color == 5:
      drawpixel("black")
    elif color == 6:
      drawpixel("light blue")
    
    e.setx(e.xcor()+length)
  e.sety(e.ycor()-length)
  e.setx(x)