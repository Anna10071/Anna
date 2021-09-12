from turtle import *


def head(x, y):  # head
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3.5)  
            fd(a)  
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()


def ears(x, y):  
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()

    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


def eyes():  # eyes
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()

    color((255, 155, 192), "white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


def cheek(x, y):  
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x, y):  
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


def body(x, y):  
    color((255, 99, 71))
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(-130)
    circle(100, 10)
    circle(300, 30)
    setheading(0)
    forward(230)
    setheading(90)
    circle(300, 30)
    circle(100, 3)
    color((255, 155, 192), (255, 100, 100))
    setheading(-135)
    circle(-80, 63)
    circle(-150, 24)
    end_fill()


def hands(x, y):  
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    setheading(-160)
    circle(300, 15)
    penup()
    setheading(90)
    forward(15)
    setheading(0)
    forward(0)
    pendown()
    setheading(-10)
    circle(-20, 90)

    penup()
    setheading(90)
    forward(30)
    setheading(0)
    forward(237)
    pendown()
    setheading(-20)
    circle(-300, 15)
    penup()
    setheading(90)
    forward(20)
    setheading(0)
    forward(0)
    pendown()
    setheading(-170)
    circle(20, 90)


def foot(x, y):  
    pensize(10)
    color((240, 128, 128))
    penup()
    goto(x, y)
    pendown()
    setheading(-90)
    forward(40)
    setheading(-180)
    color("black")
    pensize(15)
    fd(20)

    pensize(10)
    color((240, 128, 128))
    penup()
    setheading(90)
    forward(40)
    setheading(0)
    forward(90)
    pendown()
    setheading(-90)
    forward(40)
    setheading(-180)
    color("black")
    pensize(15)
    fd(20)


def tail(x, y): 
    pensize(4)
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    seth(0)
    circle(70, 20)
    circle(10, 330)
    circle(70, 30)

def nose(x, y):  
    penup()  
    goto(x, y)  
    pendown()  
    setheading(-32) 
    begin_fill() 
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            left(3)  
            forward(a)  
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()  

    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    pencolor(255, 155, 192)  
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)  
    end_fill()

    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()

def setting():  
    pensize(4)
    hideturtle()  
    colormode(255) 
    color((255, 155, 192))
    setup(840, 500)
    speed(10)



setting()
nose(-100, 100) 
head(-69, 167)  
ears(0, 160)  
eyes()  
cheek(80, 10)  
mouth(-20, 30)
body(-32, -8)  
hands(-56, -45)  
foot(2, -177)  
tail(148, -155)  
done()



