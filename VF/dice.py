from turtle import Turtle

joe = Turtle()

def dice():
  joe.hideturtle()
  joe.speed(2)
  joe.pendown()
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.goto(0,0)

def dot(x,y):
  joe.penup()
  joe.goto(x,y)
  joe.pendown()   
  joe.color("black")
  joe.dot(10)
  
def erase():
  joe.penup()
  joe.goto(-50, 50)
  joe.color("#F7F9F9")
  joe.begin_fill()
  joe.circle(100)
  joe.end_fill()
  joe.color("black")
  joe.goto(0, 0)
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
  
def dice3():
  dice()
  dot(30,30)
  dot(50,50)
  dot(70,70)
  joe.hideturtle()
  erase()
  
def dice4():
  dice()
  dot(20,70)
  dot(65,70)
  dot(22,20)
  dot(65,20)
  joe.hideturtle()
  erase()
  
def dice5():
  dice()
  dot(50,50)
  dot(20,70)
  dot(70,70)
  dot(22,20)
  dot(70,20)
  joe.hideturtle()
  erase()
  
def dice6():
  dice()
  dot(20,70)
  dot(45,70)
  dot(70,70)
  dot(45,20)
  dot(22,20)
  dot(70,20)
  joe.hideturtle()
  erase()