from turtle import *
screen = Screen()
screen.setup(800,800)
screen.colormode(255)
screen.bgcolor("black")
sonic = Turtle()
sonic.speed(0)
sonic.penup()
sonic.goto(-400,400)
length = 100
x = -400
def drawpixel(color):
  sonic.pendown()
  sonic.color(color)
  sonic.begin_fill()
  for i in range(4):
    sonic.fd(length)
    sonic.rt(90)
  sonic.end_fill()
  sonic.penup()
  """
  This is for rbg colors
def drawpixel2(R, G, B):
  sonic.pendown()
  sonic.color(R, G, B)
  sonic.begin_fill()
  for i in range(4):
    sonic.fd(length)
    sonic.rt(90)
  sonic.end_fill()
  sonic.penup()
"""
'''
1 = white
2 = tan
3 = red
4 = blue
5 = black
6 = light blue
'''


grid = [[6,6,6,6,6,6,6,6],
        [6,4,4,4,4,4,6,6],
        [4,4,4,5,1,5,6,6],
        [4,6,4,2,2,2,6,6],
        [6,4,4,4,4,4,4,6],
        [6,4,4,2,2,2,4,6],
        [6,1,4,2,2,2,1,6],
        [6,6,6,3,6,3,6,6]]

"""
loops through grid
"""
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
    
    sonic.setx(sonic.xcor()+length)
  sonic.sety(sonic.ycor()-length)
  sonic.setx(x)