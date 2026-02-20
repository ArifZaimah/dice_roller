from turtle import Turtle

joe = Turtle()

def dice():
  joe.pendown()
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)

def dot(x,y):
  joe.penup()
  joe.goto(x,y)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  
def erase():
  joe.penup()
  joe.goto(-50,50)
  joe.color('#F8F8FF')
  joe.begin_fill()
  joe.circle(100)
  joe.end_fill()
  joe.color('black')
  joe.goto(0,0)
  joe.left(90)
  
def dice1():
  dice()
  dot(50,50)
  joe.hideturtle()
  erase()
  
def dice2():
  dice()
  dot(30,50)
  dot(60,50)
  joe.hideturtle()
  erase()
  
  