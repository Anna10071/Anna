import turtle
import datetime
screen = turtle.Screen()
screen.title('Clock ')
screen.setup(1000,800)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)
screen.bgcolor('sky blue')

class clock:
    def __init__(self,hour,minute,second):
        self.hour, self.minute, self.second = hour, minute, second
        self.face = turtle.Turtle()
        self.hand = turtle.Turtle()
        self.face.hideturtle()
        self.hand.hideturtle()

    def draw(self):
        self.draw_face()
        self.draw_hand()
        
    def draw_face(self):
        self.face.clear()
        self.face.up()
        self.face.goto(0,-700)
        self.face.pensize(5)
        self.face.down()
        self.face.fillcolor('white')
        self.face.begin_fill()
        self.face.circle(700)
        self.face.end_fill()
        self.face.up()
        self.face.goto(0,0)
        self.face.dot(10)
        self.face.pensize(2)
        for angle in range(0,360,6):
            self.face.up()
            self.face.goto(0,0)
            self.face.seth(90-angle)
            self.face.fd(620)
            self.face.down()
            self.face.fd(30)
        self.face.pensize(4)
        for angle in range(0,360,30):
            self.face.up()
            self.face.goto(0,0)
            self.face.seth(90-angle)
            self.face.fd(600)
            self.face.down()
            self.face.fd(50)
        
    def draw_hand(self):    
        self.hand.clear()       
        self.hand.up()
        self.hand.goto(0,0)
        self.hand.seth(90-self.hour%12*360//12)
        self.hand.down()
        self.hand.color('black')
        self.hand.pensize(6)
        self.hand.fd(300)

        self.hand.up()
        self.hand.goto(0,0)
        self.hand.seth(90-self.minute*6)
        self.hand.down()
        self.hand.color('black')
        self.hand.pensize(4)
        self.hand.fd(400)

        self.hand.up()
        self.hand.color('red')
        self.hand.goto(0,0)
        self.hand.dot(5)
        self.hand.seth(90-self.second*6)
        self.hand.down()
        self.hand.pensize(2)
        self.hand.fd(600)

def animate():
    global c
    d = datetime.datetime.now()
    c.hour, c.minute, c.second = d.hour, d.minute, d.second
    c.draw_hand()
    screen.update()
    screen.ontimer(animate,1000)
    
d = datetime.datetime.now()
c = clock(d.hour,d.minute,d.second)
c.draw_face()
screen.update()
while True:
    animate()

