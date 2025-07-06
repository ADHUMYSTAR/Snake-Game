from turtle import Turtle
positions=[(0,0),(-20,0),(-40,0)]

UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.createSnakes()
        self.speed=0.1

    def createSnakes(self):
        for position in positions:
            self.add_segment(position)
    
    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            x=self.segments[seg_num-1].xcor()
            y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x,y)
        self.head = self.segments[0]
        self.segments[0].forward(10)

    def up(self):
        if self.segments[0].heading()!=DOWN:
            self.segments[0].setheading(UP)
    
    def down(self):
        if self.segments[0].heading()!=UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading()!=RIGHT:
            self.segments[0].setheading(LEFT)
    
    def right(self):
        if self.segments[0].heading()!=LEFT:
            self.segments[0].setheading(RIGHT)